# Accounts/models/party_payment_recieves.py

from django.db import models

class PartyPaymentRecieve(models.Model):
    id = models.BigAutoField(primary_key=True)
    tran_id = models.CharField(max_length=255)
    tran_type = models.BigIntegerField()  # FK to transaction__main__heads
    tran_method = models.CharField(max_length=255)
    invoice = models.CharField(max_length=255, null=True, blank=True)
    loc_id = models.BigIntegerField(null=True, blank=True)  # FK to location__infos
    tran_type_with = models.BigIntegerField(null=True, blank=True, db_index=True)
    tran_user = models.CharField(max_length=255, null=True, blank=True)
    user_name = models.CharField(max_length=255, null=True, blank=True)
    user_phone = models.CharField(max_length=255, null=True, blank=True)
    user_address = models.CharField(max_length=255, null=True, blank=True)
    tran_groupe_id = models.BigIntegerField(null=True, blank=True)  # FK to transaction__groupes
    tran_head_id = models.BigIntegerField(null=True, blank=True)    # FK to transaction__heads
    quantity = models.FloatField(default=1)
    bill_amount = models.FloatField()
    discount = models.FloatField(default=0)
    net_amount = models.FloatField()
    receive = models.FloatField(null=True, blank=True)
    payment = models.FloatField(null=True, blank=True)
    due = models.FloatField(default=0)
    party_amount = models.FloatField(null=True, blank=True)
    batch_id = models.CharField(max_length=255, null=True, blank=True)
    tran_date = models.DateTimeField(auto_now_add=True)
    store_id = models.BigIntegerField(null=True, blank=True, db_index=True)
    payment_mode = models.BigIntegerField(null=True, blank=True)
    status = models.SmallIntegerField(default=1)  # 1 = Active, 0 = Inactive
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        db_table = "party_payment_recieves"

    def __str__(self):
        return f"{self.tran_id} ({self.id})"
