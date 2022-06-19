from django.urls import path

from .views import *

urlpatterns = [
    # API paths
    path('api/payers', get_payers),
    path('api/payer/<payer_id>', get_single_payer),
    path('api/pay-records', get_pay_records),
    path('api/pay-record/<payer_id>', get_single_pay_record),

    # TEMPLATE paths
    path('payers', payers_page),
    path('pay-records', pay_records_page),
]
