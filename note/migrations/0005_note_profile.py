# Generated by Django 5.0.6 on 2024-05-23 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("note", "0004_note_is_private"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="profile",
            field=models.ImageField(null=True, upload_to="profiles"),
        ),
    ]
