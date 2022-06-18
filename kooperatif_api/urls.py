from django.urls import path, include
from .views import *


urlpatterns = [
    path('payers', payers),
    path('payer/<payer_id>', get_single_payer),
    path('pay-records', get_pay_records),
    path('pay-record/<payer_id>', get_single_pay_record),
]
