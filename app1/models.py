from django.db import models
from django.contrib.auth.models import User

class Referral_system(models.Model):
    referrer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrer_referral_set', null=True)
    refree = models.ForeignKey(User, on_delete=models.CASCADE, related_name='refree_referral_set', null=True)
    referral_code = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.referral_code