import time

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *


@api_view(['GET', 'POST'])
def get_payers(request):
    if request.method == 'GET':
        all_payers = Payer.objects.all()
        serializer = PayerSerializer(all_payers, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_single_payer(request, payer_id):
    get_payer = Payer.objects.get(pk=payer_id)
    pay_records = PayRecord.objects.filter(payer=get_payer)

    pay_records_serializer = PayRecordSerializer(pay_records, many=True)
    serializer = PayerSerializer(get_payer)

    result = serializer.data
    result['pay-records'] = pay_records_serializer.data
    return Response(result)


@api_view(['GET', 'POST'])
def get_pay_records(request):
    if request.method == "GET":
        date = request.GET.get('date', '')
        pay_records = []
        if date != '':
            date_datetime = time.strptime(date, '%Y-%m-%d')
            pay_records = PayRecord.objects.filter(pay_date__year=date_datetime.tm_year,
                                                   pay_date__month=date_datetime.tm_mon,
                                                   pay_date__day=date_datetime.tm_mday)
        else:
            pay_records = PayRecord.objects.all()

        serializer = PayRecordSerializer(pay_records, many=True)

        for i, pay_record in enumerate(pay_records):
            serializer.data[i]['payer-info'] = PayerSerializer(pay_record.payer).data

        return Response(serializer.data)


@api_view(['GET'])
def get_single_pay_record(request, payer_id):
    payer = Payer.objects.get(pk=payer_id)
    pay_records = PayRecord.objects.filter(payer=payer)
    serializer = PayRecordSerializer(pay_records, many=True)
    payer_serializer = PayerSerializer(payer)

    for i, pay_record in enumerate(pay_records):
        serializer.data[i]['payer-info'] = payer_serializer.data

    return Response(serializer.data)


def payers_page(request):
    payers = Payer.objects.all()
    context = {
        'payers': payers
    }
    return render(request, 'payers.html', context=context)


def pay_records_page(request):
    pay_records = PayRecord.objects.all().order_by("pay_date")
    context = {
        'pay_records': pay_records
    }
    return render(request, 'pay-records.html', context=context)
