# Generated by Django 4.2.10 on 2024-03-25 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection_system', '0007_companyprofile_company_contact_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GarbageCollectionRequest',
        ),
    ]
