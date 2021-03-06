# Generated by Django 3.0.8 on 2020-10-23 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourprojects',
            name='five_slide',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='ourprojects',
            name='four_slide',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='ourprojects',
            name='one_slide',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='ourprojects',
            name='three_slide',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='ourprojects',
            name='two_slide',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Имя'),
        ),
    ]
