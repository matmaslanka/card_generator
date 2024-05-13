# Generated by Django 5.0.4 on 2024-05-08 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_gen', '0012_alter_contact_company_alter_contact_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
        migrations.AddField(
            model_name='config',
            name='slug',
            field=models.SlugField(blank=True, default='', unique=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='topic',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='config',
            name='phone_number',
            field=models.CharField(default='', max_length=9),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email_address',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
