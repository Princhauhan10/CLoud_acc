# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import boto3
from rest_framework.exceptions import ValidationError




class CloudAccount(models.Model):
    ACCOUNT_TYPE_CHOICES = (
        ('Azure', 'Azure'),
        ('AWS', 'AWS'),
    )
    
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES)
    account_id = models.CharField(max_length=255)
    access_key = models.TextField()  # Encrypted with JWT
    secret_key = models.TextField()  # Encrypted with JWT
    region = models.CharField(max_length=255, null=True, blank=True)
    app_id = models.CharField(max_length=255, null=True, blank=True)
    client_id = models.CharField(max_length=255, null=True, blank=True)
    secret_id = models.CharField(max_length=255, null=True, blank=True)
    tenant_id = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
   
        if self.account_type == 'Azure':
            self.access_key = ''
            self.secret_key = ''
        elif self.account_type == 'AWS':
            self.client_id = ''
            self.secret_id = ''
            self.tenant_id = ''
        super(CloudAccount, self).save(*args, **kwargs)
    
    
    def __str__(self):
        return f'{self.account_type} Account ({self.account_id})'
    
    class Meta:
        db_table = 'cloud_accounts'
        indexes = [
            models.Index(fields=['account_id', 'account_type'])
        ]