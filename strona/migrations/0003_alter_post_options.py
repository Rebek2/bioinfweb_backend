# Generated by Django 4.0.2 on 2022-04-03 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0002_auto_20220224_0030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-date_created',)},
        ),
    ]
