# Generated by Django 4.0.6 on 2022-09-17 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0008_savingplan_is_fixed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savingplan',
            name='allowed_withdraw_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='savingplan',
            name='create_time',
            field=models.DateField(auto_now=True),
        ),
    ]
