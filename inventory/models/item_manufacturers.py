from django.db import models
from .item_categories import ItemCategory

class ItemManufacturer(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.ForeignKey(ItemCategory, on_delete=models.SET_NULL, null=True, blank=True, db_column="type_id")
    manufacturer_name = models.CharField(max_length=255)
    company_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=True)  # tinyint(4) used as boolean
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = "item_manufacturers"

    def _str_(self):
        return self.manufacturer_name