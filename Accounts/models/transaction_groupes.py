# Accounts/models/transaction_groupes.py

from django.db import models

class TransactionGroupe(models.Model):
    id = models.BigAutoField(primary_key=True)
    tran_groupe_name = models.CharField(max_length=255)
    tran_groupe_type = models.BigIntegerField()
    tran_method = models.CharField(max_length=255)
    company_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.SmallIntegerField(default=1)  # 1 = Active, 0 = Inactive
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        db_table = "transaction__groupes"

    def __str__(self):
        return f"{self.tran_groupe_name} ({self.id})"
