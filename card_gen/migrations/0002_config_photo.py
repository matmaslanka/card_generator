# Generated by Django 5.0.4 on 2024-05-01 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_gen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='photo',
            field=models.CharField(max_length=9, null=True),
        ),
    ]