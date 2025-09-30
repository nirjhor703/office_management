from django.db import models

class ItemCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    type_id = models.BigIntegerField(null=True, blank=True)  # FK to another table?
    category_name = models.CharField(max_length=255)
    company_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.SmallIntegerField(default=1)  # 1 = Active, 0 = Inactive
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = "item_categories"

    def _str_(self):
        return self.category_name