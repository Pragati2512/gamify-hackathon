# Generated by Django 4.2.6 on 2023-10-19 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_goals_bp_track_badge"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bp_track",
            name="prsn",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="home.person"
            ),
        ),
    ]