# Generated by Django 4.2.16 on 2024-09-14 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_post"),
    ]

    operations = [
        migrations.CreateModel(
            name="LikePost",
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
                ("psot_id", models.CharField(max_length=500)),
                ("username", models.CharField(max_length=100)),
            ],
        ),
    ]
