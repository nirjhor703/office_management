# Accounts/models/transaction_heads.py

from django.db import models

class TransactionHead(models.Model):
    id = models.BigAutoField(primary_key=True)
    tran_head_name = models.CharField(max_length=255)
    groupe_id = models.BigIntegerField()  # FK to transaction__groupes
    category_id = models.BigIntegerField(null=True, blank=True)
    manufacturer_id = models.BigIntegerField(null=True, blank=True)
    form_id = models.BigIntegerField(null=True, blank=True)
    unit_id = models.BigIntegerField(default=1)  # FK to item__units
    quantity = models.FloatField(default=0)
    cp = models.FloatField(default=0)
    mrp = models.FloatField(default=0)
    expiry_date = models.DateField(null=True, blank=True)
    editable = models.BooleanField(default=False)
    company_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.SmallIntegerField(default=1)  # 1 = Active, 0 = Inactive
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        db_table = "transaction__heads"

    def __str__(self):
        return f"{self.tran_head_name} ({self.id})"
