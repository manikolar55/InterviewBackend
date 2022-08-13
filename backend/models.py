from django.db import models

# Create your models here.


class UserData(models.Model):
    description = models.CharField(max_length=100)
    amount = models.IntegerField(null=True, blank=True)
    from_age = models.IntegerField(null=True, blank=True)
    to_age = models.IntegerField(null=True, blank=True)
    income_grows = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'user_data'