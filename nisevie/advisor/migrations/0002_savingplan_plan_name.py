# Generated by Django 4.0.6 on 2022-09-15 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='savingplan',
            name='plan_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
