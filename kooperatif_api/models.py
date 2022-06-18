from django.db import models


class Payer(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    shares = models.IntegerField()
    phone_number = models.CharField(max_length=11)
    added_time = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return "{}. {} {} - {} Hisse".format(self.pk, self.first_name, self.second_name, self.shares)


class PayRecord(models.Model):
    payer = models.ForeignKey(Payer, on_delete=models.CASCADE)
    paid_shares = models.IntegerField(default=1)
    pay_date = models.DateTimeField()

    def __str__(self):
        return "{} - {}".format(self.payer, self.pay_date)
