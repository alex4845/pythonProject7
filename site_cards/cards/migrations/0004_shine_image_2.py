# Generated by Django 4.1.3 on 2022-12-07 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_remove_shine_image_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='shine',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='media/media/site_cards'),
        ),
    ]