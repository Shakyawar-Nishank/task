# Generated by Django 4.0.5 on 2022-06-09 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0008_alter_hospital_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.CharField(choices=[('Mental Health', 'Mental Health'), ('Hearth Disease', 'Hearth Disease'), ('Covid-19', 'Covid-19'), ('Immunization', 'Immunization')], max_length=200)),
                ('summary', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital')),
            ],
        ),
    ]
