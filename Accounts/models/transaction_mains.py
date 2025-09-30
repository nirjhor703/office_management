# Accounts/models/transaction_mains.py

from django.db import models

class TransactionMain(models.Model):
    id = models.BigAutoField(primary_key=True)
    tran_id = models.CharField(max_length=255, db_index=True)
    tran_type = models.BigIntegerField()  # FK to transaction__main__heads
    tran_method = models.CharField(max_length=255)
    invoice = models.CharField(max_length=255, null=True, blank=True)
    loc_id = models.BigIntegerField(null=True, blank=True)  # FK to location__infos
    tran_type_with = models.BigIntegerField(null=True, blank=True, db_index=True)
    tran_bank = models.CharField(max_length=255, null=True, blank=True)
    tran_user = models.CharField(max_length=255, null=True, blank=True)
    ptn_id = models.CharField(max_length=255, null=True, blank=True)
    user_name = models.CharField(max_length=255, null=True, blank=True)
    user_phone = models.CharField(max_length=255, null=True, blank=True)
    user_address = models.CharField(max_length=255, null=True, blank=True)
    bill_amount = models.FloatField(null=True, blank=True)
    discount = models.FloatField(default=0)
    net_amount = models.FloatField(null=True, blank=True)
    receive = models.FloatField(null=True, blank=True)
    payment = models.FloatField(null=True, blank=True)
    due = models.FloatField(null=True, blank=True)
    due_col = models.FloatField(null=True, blank=True, default=0)
    due_disc = models.FloatField(null=True, blank=True, default=0)
    doc_id = models.CharField(max_length=255, null=True, blank=True)
    sr_id = models.CharField(max_length=255, null=True, blank=True)
    store_id = models.BigIntegerField(null=True, blank=True, db_index=True)
    payment_mode = models.BigIntegerField(null=True, blank=True)
    booking_id = models.CharField(max_length=255, null=True, blank=True)
    tran_date = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(default=1)  # 1 = Active, 0 = Inactive
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        db_table = "transaction__mains"

    def __str__(self):
        return f"{self.tran_id} ({self.id})"
