# Generated by Django 3.0.8 on 2020-11-25 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_subcategory_image'),
        ('orders', '0002_auto_20201022_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='categoryy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.Category'),
            preserve_default=False,
        ),
    ]