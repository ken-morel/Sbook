# Generated by Django 4.0.6 on 2024-05-10 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sbook", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(max_length=255)),
                ("password", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name="Account",
        ),
    ]
