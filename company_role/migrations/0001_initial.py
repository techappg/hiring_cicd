# Generated by Django 4.0.4 on 2022-05-31 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Interviewee_role', '0001_initial'),
        ('Sample_Paper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_Name', models.CharField(max_length=255)),
                ('company_address', models.CharField(blank=True, max_length=255, null=True)),
                ('company_phone_no', models.CharField(blank=True, max_length=12, null=True)),
                ('company_email', models.EmailField(max_length=254)),
                ('company_Password', models.CharField(max_length=255)),
                ('company_state', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('added_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='IntervieweeTestDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateTimeField(blank=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('answer', models.CharField(blank=True, max_length=255, null=True)),
                ('is_completed_by_computer', models.BooleanField(default=False)),
                ('status', models.CharField(default='pending', max_length=15)),
                ('remarks', models.TextField(default='')),
                ('send_email', models.BooleanField(default=False)),
                ('interviewee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Interviewee_role.interviwee_profile')),
                ('interviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('test', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Sample_Paper.samplepaper')),
            ],
        ),
        migrations.CreateModel(
            name='Hr_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='company_role.company_profile')),
            ],
        ),
    ]
