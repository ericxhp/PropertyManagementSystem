from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse



class Asset(models.Model):
    STATUS_CHOICES = (
        ('in stock', 'InStock'),
        ('in use', 'InUse'),
        ('in repair', 'InRepair'),
        ('broken', 'Broken'),
    )
    asset_num =  models.CharField(max_length=250, verbose_name='asset number')
    desciption = models.CharField(max_length=250, verbose_name='description')
    serial_num = models.CharField(max_length=250, verbose_name='serial number')    
    asset_type = models.CharField(max_length=250, verbose_name='asset type')
    location = models.CharField(max_length=250, verbose_name='location')
    status = models.CharField(max_length=10, verbose_name='asset status',
                                choices=STATUS_CHOICES,
                                default='in stock')
    owner = models.CharField(max_length=250, verbose_name='asset owner')
    assignee = models.CharField(max_length=250, verbose_name='asset assignee')
    order_num = models.CharField(max_length=250, verbose_name='asset order num')
    note = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    operator = models.ForeignKey(User,
                                related_name='asset_operate')