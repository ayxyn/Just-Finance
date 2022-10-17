# Generated by Django 4.0.4 on 2022-10-16 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_excell_template_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='email_address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Email Address'),
        ),
        migrations.AddField(
            model_name='setting',
            name='telegram',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Telegram'),
        ),
    ]
