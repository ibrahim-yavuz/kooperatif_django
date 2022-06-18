from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


@api_view(['GET', 'POST'])
def payers(request):
    if request.method == 'GET':
        # context = {"payers": Payer.objects.all()}
        # return render(request, 'payers.html', context=context)
        all_payers = Payer.objects.all()
        serializer = PayerSerializer(all_payers, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_single_payer(request, payer_id):
    get_payer = Payer.objects.get(pk=payer_id)
    serializer = PayerSerializer(get_payer)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def get_pay_records(request):
    if request.method == "GET":
        pay_records = PayRecord.objects.all()
        serializer = PayRecordSerializer(pay_records, many=True)
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
