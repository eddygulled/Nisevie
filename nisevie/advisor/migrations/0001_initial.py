# Generated by Django 4.0.6 on 2022-09-12 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bankCredentials', '0002_savingaccount_create_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StreamCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
                ('create_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('amount', models.FloatField(default=0)),
                ('frequency', models.IntegerField()),
                ('time_interval', models.IntegerField(verbose_name='time interval in months')),
                ('can_save_amount', models.FloatField(default=0)),
                ('least_expenditure', models.FloatField(default=0)),
                ('time_delay', models.IntegerField(default=0, verbose_name='Time delay for the expenditure to occur in months')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advisor.streamcategory')),
                ('linked_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankCredentials.bankaccount')),
            ],
        ),
        migrations.CreateModel(
            name='SavingPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('time_interval', models.IntegerField(default=0)),
                ('initial_amount', models.BigIntegerField(default=0)),
                ('current_amount', models.BigIntegerField(default=0)),
                ('allowed_withdraw_date', models.DateTimeField()),
                ('is_frequency_allowed', models.BooleanField(default=False)),
                ('deposit_frequency', models.IntegerField(default=1)),
                ('frequency_deposit_amount', models.BigIntegerField(default=0)),
                ('next_action_date', models.DateField(null=True)),
                ('is_current', models.BooleanField(default=False)),
                ('income_stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advisor.stream')),
                ('target_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankCredentials.bankaccount', verbose_name='target account')),
            ],
        ),
    ]
