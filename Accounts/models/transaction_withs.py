# Accounts/models/transaction_withs.py

from django.db import models

class TransactionWith(models.Model):
    id = models.BigAutoField(primary_key=True)
    tran_with_name = models.CharField(max_length=255)
    user_role = models.BigIntegerField()  # FK to roles
    tran_type = models.BigIntegerField()  # FK to transaction__main__heads
    tran_method = models.CharField(max_length=255)
    status = models.SmallIntegerField(default=1)  # 1 = Active, 0 = Inactive
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        db_table = "transaction__withs"

    def __str__(self):
        return f"{self.tran_with_name} ({self.id})"
