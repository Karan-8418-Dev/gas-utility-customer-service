# Generated by Django 5.1.5 on 2025-01-18 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer_portal", "0002_servicerequest_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="servicerequest",
            name="address",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
