# Generated by Django 3.1.8 on 2021-04-25 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(max_length=100)),
                ('address_2', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('postcode', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=30)),
                ('mobile_no', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=100)),
                ('department', models.CharField(blank=True, max_length=100)),
                ('position', models.CharField(blank=True, max_length=100)),
                ('designation', models.CharField(blank=True, max_length=50)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.addressinfo')),
                ('contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.contactdetail')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
