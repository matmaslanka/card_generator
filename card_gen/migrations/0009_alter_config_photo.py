# Generated by Django 5.0.4 on 2024-05-04 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_gen', '0008_alter_config_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='photo',
            field=models.ImageField(upload_to='photos'),
        ),
    ]