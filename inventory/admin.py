from django.contrib import admin

from .models.item_categories import ItemCategory

from .models.item_forms import ItemForm
from .models.item_manufacturers import ItemManufacturer
from .models.item_units import ItemUnit


admin.site.register(ItemCategory)
admin.site.register(ItemForm)
admin.site.register(ItemManufacturer)
admin.site.register(ItemUnit)

