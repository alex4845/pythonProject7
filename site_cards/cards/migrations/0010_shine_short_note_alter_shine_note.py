# Generated by Django 4.1.3 on 2022-12-14 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0009_shine_diametr'),
    ]

    operations = [
        migrations.AddField(
            model_name='shine',
            name='short_note',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='shine',
            name='note',
            field=models.TextField(blank=True, max_length=120, null=True),
        ),
    ]
