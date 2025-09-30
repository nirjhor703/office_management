# Accounts/models/user_info.py

from django.db import models

class UserInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=255, db_index=True)
    login_user_id = models.CharField(max_length=255, null=True, blank=True)  # FK to login__users
    title = models.CharField(max_length=255, null=True, blank=True)
    user_name = models.CharField(max_length=255, null=True, blank=True)
    user_email = models.CharField(max_length=255, null=True, blank=True)
    user_phone = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    loc_id = models.BigIntegerField(null=True, blank=True)  # FK to locations
    user_role = models.BigIntegerField()  # FK to roles
    tran_user_type = models.BigIntegerField(null=True, blank=True, db_index=True)
    dob = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    religion = models.CharField(max_length=255, null=True, blank=True)
    nid = models.CharField(max_length=255, null=True, blank=True)
    passport = models.CharField(max_length=255, null=True, blank=True)
    driving_lisence = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    corporate_id = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    store_id = models.BigIntegerField(null=True, blank=True, db_index=True)
    company_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.SmallIntegerField(default=1)  # 1 = Active, 0 = Inactive
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        db_table = "user_info"

    def __str__(self):
        return f"{self.user_name or self.user_id} ({self.id})"
