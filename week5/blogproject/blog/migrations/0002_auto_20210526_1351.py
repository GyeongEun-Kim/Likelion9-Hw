# Generated by Django 3.2.3 on 2021-05-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='blog',
            name='writer',
            field=models.CharField(default='', max_length=100),
        ),
    ]
