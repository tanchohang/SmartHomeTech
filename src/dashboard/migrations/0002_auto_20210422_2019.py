# Generated by Django 3.1.8 on 2021-04-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagefiles',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
