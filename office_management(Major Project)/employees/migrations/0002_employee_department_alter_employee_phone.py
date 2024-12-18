# Generated by Django 5.1.3 on 2024-12-13 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.CharField(default='Information Technology', max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]