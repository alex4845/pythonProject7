# Generated by Django 4.1.3 on 2022-12-14 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_remove_shine_enter_date_shine_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='shine',
            name='diametr',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]