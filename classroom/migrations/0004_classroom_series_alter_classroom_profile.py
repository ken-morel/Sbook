# Generated by Django 5.0.6 on 2024-06-11 18:20

import profile_images
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("classroom", "0003_alter_classroom_description"),
        ("sbook", "0014_remove_serie_levels_course_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="classroom",
            name="series",
            field=models.ManyToManyField(related_name="classrooms", to="sbook.serie"),
        ),
        migrations.AlterField(
            model_name="classroom",
            name="profile",
            field=models.ImageField(
                default=profile_images.get_random_file, upload_to="media/profiles"
            ),
        ),
    ]
