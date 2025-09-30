from django.db import models
from .item_categories import ItemCategory


class ItemForm(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.ForeignKey(ItemCategory, on_delete=models.SET_NULL, null=True, blank=True, db_column="type_id")
    form_name = models.CharField(max_length=255)
    company_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=True)   # since tinyint(4) usually means boolean
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = "item_forms"

    def _str_(self):
        return self.form_name