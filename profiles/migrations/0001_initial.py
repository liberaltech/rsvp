# Generated by Django 3.1.2 on 2020-10-14 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=256, null=True)),
                ('Address', models.CharField(blank=True, help_text='Address', max_length=150)),
                ('city', models.CharField(blank=True, help_text='City / Town / Village', max_length=50)),
                ('province', models.CharField(blank=True, help_text='County / State / Province', max_length=50)),
                ('country', models.CharField(blank=True, help_text='City / Town / Village', max_length=50)),
                ('postal_code', models.CharField(blank=True, help_text='Postal Code / Eircode', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
