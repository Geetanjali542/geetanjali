# Generated by Django 5.1 on 2024-08-10 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_file', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='summary_image',
            field=models.ImageField(blank=True, null=True, upload_to='summaries/'),
        ),
    ]
