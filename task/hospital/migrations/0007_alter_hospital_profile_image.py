# Generated by Django 4.0.5 on 2022-06-08 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_alter_hospital_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
