from django.db import models

# Create your models here.


class UserData(models.Model):
    description = models.CharField(max_length=100)
    amount = models.IntegerField(null=True, blank=True, default=None)
    from_age = models.IntegerField(null=True, blank=True, default=None)
    to_age = models.IntegerField(null=True, blank=True, default=None)
    income_grows = models.IntegerField(null=True, blank=True, default=None)

    class Meta:
        db_table = 'user_data'