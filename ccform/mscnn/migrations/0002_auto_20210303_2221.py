# Generated by Django 3.1.7 on 2021-03-03 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mscnn', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countprediction',
            old_name='CrowdLimit',
            new_name='CrowCount',
        ),
    ]
