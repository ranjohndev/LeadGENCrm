# Generated by Django 5.0.1 on 2024-02-14 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0013_lead_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='years_in_business',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Years in Business'),
        ),
    ]
