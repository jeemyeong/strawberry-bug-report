# Generated by Django 4.1.5 on 2023-01-20 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='name',
            field=models.CharField(default='', max_length=127),
        ),
        migrations.AddField(
            model_name='slot',
            name='name',
            field=models.CharField(default='', max_length=127),
        ),
    ]
