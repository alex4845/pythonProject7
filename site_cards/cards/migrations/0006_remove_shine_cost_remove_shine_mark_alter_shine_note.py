# Generated by Django 4.1.3 on 2022-12-13 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_shine_image_3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shine',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='shine',
            name='mark',
        ),
        migrations.AlterField(
            model_name='shine',
            name='note',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
