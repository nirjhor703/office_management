# Accounts/models/transaction_details.py

from django.db import models


class TransactionDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    tran_id = models.CharField(max_length=255)
    tran_type = models.BigIntegerField()
    tran_method = models.CharField(max_length=255)
    invoice = models.CharField(max_length=255, null=True, blank=True)
    loc_id = models.BigIntegerField(null=True, blank=True)
    tran_type_with = models.BigIntegerField(null=True, blank=True)
    tran_bank = models.CharField(max_length=255, null=True, blank=True)
    tran_user = models.CharField(max_length=255, null=True, blank=True)
    ptn_id = models.CharField(max_length=255, null=True, blank=True)
    user_name = models.CharField(max_length=255, null=True, blank=True)
    user_phone = models.CharField(max_length=255, null=True, blank=True)
    user_address = models.CharField(max_length=255, null=True, blank=True)
    tran_groupe_id = models.BigIntegerField(null=True, blank=True)
    tran_head_id = models.BigIntegerField(null=True, blank=True)
    quantity_actual = models.FloatField(default=1)
    quantity = models.FloatField(default=1)
    quantity_issue = models.FloatField(default=0)
    quantity_return = models.FloatField(default=0)
    unit_id = models.BigIntegerField(null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    tot_amount = models.FloatField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    cp = models.FloatField(null=True, blank=True)
    mrp = models.FloatField(null=True, blank=True)
    receive = models.FloatField(null=True, blank=True)
    payment = models.FloatField(null=True, blank=True)
    due = models.FloatField(null=True, blank=True)
    due_col = models.FloatField(null=True, blank=True, default=0)
    due_disc = models.FloatField(null=True, blank=True, default=0)
    expiry_date = models.DateField(null=True, blank=True)
    doc_id = models.CharField(max_length=255, null=True, blank=True)
    sr_id = models.CharField(max_length=255, null=True, blank=True)
    store_id = models.BigIntegerField(null=True, blank=True)
    payment_mode = models.BigIntegerField(null=True, blank=True)
    batch_id = models.CharField(max_length=255, null=True, blank=True)
    booking_id = models.CharField(max_length=255, null=True, blank=True)
    tran_date = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(default=1)  # 1 = Active, 0 = Inactive
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "transaction__details"

    def __str__(self):
        return f"TransactionDetail {self.id} - {self.tran_id}"
