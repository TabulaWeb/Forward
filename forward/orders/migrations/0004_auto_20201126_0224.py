# Generated by Django 3.0.8 on 2020-11-25 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_orderitem_categoryy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='categoryy',
            new_name='category',
        ),
    ]
