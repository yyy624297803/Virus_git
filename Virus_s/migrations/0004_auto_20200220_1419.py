# Generated by Django 3.0.3 on 2020-02-20 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Virus_s', '0003_auto_20200220_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areacity',
            name='cityEnglishName',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='areacity',
            name='provinceName',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='city',
            name='continentEnglishName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='city',
            name='continentName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='city',
            name='countryEnglishName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='city',
            name='countryName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='city',
            name='provinceEnglishName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='city',
            name='provinceName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='city',
            name='provinceShortName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='news',
            name='provinceName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='rumors',
            name='mainSummary',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='rumors',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
