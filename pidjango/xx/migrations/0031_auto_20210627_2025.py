# Generated by Django 3.2.2 on 2021-06-27 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xx', '0030_auto_20210603_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpi',
            name='gateway',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='rpi',
            name='nameserver',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='rpi',
            name='ssh_port',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='rpi',
            name='subnetEth',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='rpi',
            name='subnetWlan',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
        migrations.AlterField(
            model_name='xuser',
            name='password',
            field=models.CharField(blank=True, help_text='at least 8 long, one capital, one special character', max_length=12, null=True),
        ),
    ]
