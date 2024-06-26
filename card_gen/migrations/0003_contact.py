# Generated by Django 5.0.4 on 2024-05-02 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_gen', '0002_config_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=9)),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
    ]
