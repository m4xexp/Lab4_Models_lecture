# Generated by Django 3.1.2 on 2020-10-19 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20201019_0848'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.RemoveField(
            model_name='invoicelineitem',
            name='invoice_no',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
        migrations.DeleteModel(
            name='InvoiceLineItem',
        ),
    ]
