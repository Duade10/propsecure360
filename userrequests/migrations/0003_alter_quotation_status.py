# Generated by Django 5.0 on 2023-12-09 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userrequests', '0002_userrequest_price_quotation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='status',
            field=models.CharField(choices=[('accepted', 'Accepted'), ('declined', 'Declined'), ('negociate', 'Negociate'), ('pending', 'Pending')], max_length=20),
        ),
    ]
