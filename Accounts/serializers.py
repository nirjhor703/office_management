from rest_framework import serializers
from .models import *

# Create your models here.
class TransactionMainSerializer(serializers.ModelSerializer):
    class Meta: 
        model = TransactionMain
        # fields = ['id','name','email','subject','roll']
        fields = '__all__'

class TransactionHeadSerializer(serializers.ModelSerializer):
    class Meta: 
        model = TransactionHead
        # fields = ['id','name','email','subject','roll']
        fields = '__all__'

class TransactionGroupeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = TransactionGroupe
        # fields = ['id','name','email','subject','roll']
        fields = '__all__'