# Generated by Django 3.0.8 on 2020-11-25 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20201126_0224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='category',
            new_name='mcategory',
        ),
    ]
