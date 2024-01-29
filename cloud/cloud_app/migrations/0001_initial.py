# Generated by Django 4.2.4 on 2024-01-28 07:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CloudAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(choices=[('Azure', 'Azure'), ('AWS', 'AWS')], max_length=10)),
                ('account_id', models.CharField(max_length=255)),
                ('access_key', models.TextField()),
                ('secret_key', models.TextField()),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('app_id', models.CharField(blank=True, max_length=255, null=True)),
                ('client_id', models.CharField(blank=True, max_length=255, null=True)),
                ('secret_id', models.CharField(blank=True, max_length=255, null=True)),
                ('tenant_id', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'cloud_accounts',
                'indexes': [models.Index(fields=['account_id', 'account_type'], name='cloud_accou_account_8231a1_idx')],
            },
        ),
    ]