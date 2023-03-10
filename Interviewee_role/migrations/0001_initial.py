# Generated by Django 4.0.4 on 2022-05-31 10:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interviwee_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('cv', models.FileField(blank=True, null=True, upload_to='')),
                ('is_active', models.BooleanField(default=True)),
                ('added_on', models.DateField(auto_now_add=True)),
                ('link_time', models.DateField(blank=True, null=True)),
                ('language', models.CharField(default='', max_length=255)),
                ('level', models.CharField(default='', max_length=255)),
                ('interviwer_mail', models.EmailField(blank=True, max_length=200, null=True)),
                ('link', models.UUIDField(blank=True, default=uuid.uuid4, null=True)),
                ('sample_paper', models.CharField(blank=True, max_length=255, null=True)),
                ('addedby_superuser', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
