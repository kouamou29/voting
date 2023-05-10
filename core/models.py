from django.db import models
from django.utils import timezone

from django.conf import settings
# Create your models here.


class PartiPolic(models.Model):
    CHOICES_PARTI =[
        ('RDPC', 'RDPC'),
        ('MRC', 'MRC'),
        ('UDC', 'UDC'),
    ]
    user         = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    name         = models.CharField(max_length=200,unique=True)
    choices_pati = models.CharField(max_length=200, choices=CHOICES_PARTI)
    
    def __str__(self):
        return self.name
    
class Mility(models.Model):
    user_mility = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE, unique=True)
    party      = models.ForeignKey(PartiPolic, on_delete=models.CASCADE)
    contry     = models.CharField(max_length=200, blank=True, null=True)
    city       = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.user_mility.username
    

class Voting(models.Model):
    name           = models.CharField(max_length=200,)
    vote           = models.ManyToManyField(Mility)
    number_voting  = models.IntegerField()
    date_create    = models.DateTimeField(auto_now_add=False, default=timezone.now)
    
    def __str__(self):
        return self.name
    


   

















