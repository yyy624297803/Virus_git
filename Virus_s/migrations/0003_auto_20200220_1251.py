# Generated by Django 3.0.3 on 2020-02-20 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Virus_s', '0002_auto_20200220_1139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='overall',
            old_name='seriousConfirmedIncr',
            new_name='currentConfirmedIncr',
        ),
    ]