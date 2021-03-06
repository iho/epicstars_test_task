# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-07 15:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('debit', models.DecimalField(
                    decimal_places=6, default=0, max_digits=18)),
                ('credit', models.DecimalField(
                    decimal_places=6, default=0, max_digits=18)),
            ],
        ),
        migrations.CreateModel(
            name='AccountingTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('amount', models.DecimalField(
                    decimal_places=6, default=0, max_digits=16)),
                ('credit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                             related_name='credit_transactions', to='modelsapp.Account')),
                ('debit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                            related_name='debit_transactions', to='modelsapp.Account')),
            ],
        ),
    ]
