# Generated by Django 3.1.2 on 2020-10-19 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0007_auto_20201019_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('credit_limit', models.FloatField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('date', models.DateField(null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('vat', models.FloatField(blank=True, null=True)),
                ('amount_due', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'invoice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('units', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InvoiceLineItem',
            fields=[
                ('invoice_no', models.ForeignKey(db_column='invoice_no', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='report.invoice')),
                ('quantity', models.IntegerField(null=True)),
                ('unit_price', models.FloatField(null=True)),
                ('extended_price', models.FloatField(null=True)),
            ],
            options={
                'db_table': 'invoice_line_item',
                'managed': False,
            },
        ),
    ]
