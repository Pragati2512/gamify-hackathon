# Generated by Django 4.2.6 on 2023-10-18 19:24

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="person",
            name="pw",
        ),
        migrations.AddField(
            model_name="person",
            name="emer_email",
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name="person",
            name="emer_name",
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name="person",
            name="emer_phone",
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AddField(
            model_name="person",
            name="emer_relation",
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name="person",
            name="gender",
            field=models.CharField(
                choices=[("Male", "Male"), ("Female", "Female"), ("Secret", "Secret")],
                default=home.models.Gender["Male"],
                max_length=10,
            ),
        ),
    ]
