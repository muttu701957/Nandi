# Generated by Django 5.1.6 on 2025-03-03 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_billing_master_balance_billing_master_bill_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing_master',
            name='balance',
            field=models.CharField(default=0, max_length=50, null=True),
        ),
    ]
