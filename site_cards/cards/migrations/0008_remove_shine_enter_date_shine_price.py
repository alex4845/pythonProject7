# Generated by Django 4.1.3 on 2022-12-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_remove_shine_radius_shine_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shine',
            name='enter_date',
        ),
        migrations.AddField(
            model_name='shine',
            name='price',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
