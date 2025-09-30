from django.contrib import admin
from .models.transaction_details import TransactionDetail
from .models.transaction_details_temps import TransactionDetailTemp
from .models.transaction_groupes import TransactionGroupe
from .models.transaction_heads import TransactionHead
from .models.transaction_mains import TransactionMain
from .models.transaction_mains_temps import TransactionMainTemp
from .models.transaction_withs import TransactionWith
from .models.user_info import UserInfo
from .models.party_payment_recieves import PartyPaymentRecieve


admin.site.register(TransactionDetail)
admin.site.register(TransactionDetailTemp)
admin.site.register(TransactionGroupe)
admin.site.register(TransactionHead)
admin.site.register(TransactionMain)
admin.site.register(TransactionMainTemp)
admin.site.register(TransactionWith)
admin.site.register(UserInfo)
admin.site.register(PartyPaymentRecieve)
