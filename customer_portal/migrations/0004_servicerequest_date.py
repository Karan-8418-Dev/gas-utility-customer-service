# Generated by Django 5.1.5 on 2025-01-18 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer_portal", "0003_servicerequest_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="servicerequest",
            name="date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
