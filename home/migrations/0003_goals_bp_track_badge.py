# Generated by Django 4.2.6 on 2023-10-19 02:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_remove_person_pw_person_emer_email_person_emer_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="goals",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("goal1", models.BooleanField(default=True)),
                ("goal2", models.BooleanField(default=True)),
                ("goal3", models.BooleanField(default=True)),
                ("goal4", models.BooleanField(default=False)),
                ("goal5", models.BooleanField(default=False)),
                ("goal6", models.BooleanField(default=False)),
                ("goal7", models.BooleanField(default=False)),
                (
                    "prsn",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="home.person"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="bp_track",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(default=datetime.date.today)),
                ("sys", models.IntegerField(default=-1)),
                ("dia", models.IntegerField(default=-1)),
                (
                    "prsn",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="home.person"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="badge",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(default=datetime.date.today)),
                ("badge_name", models.CharField(max_length=25)),
                (
                    "prsn",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="home.person"
                    ),
                ),
            ],
        ),
    ]
