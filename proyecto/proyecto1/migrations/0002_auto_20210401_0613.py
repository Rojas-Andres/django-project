# Generated by Django 3.1.7 on 2021-04-01 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]