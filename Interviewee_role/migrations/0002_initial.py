# Generated by Django 4.0.4 on 2022-05-31 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company_role', '0001_initial'),
        ('Interviewee_role', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviwee_profile',
            name='addedby_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company_role.company_profile'),
        ),
    ]
