# Generated by Django 5.0.6 on 2024-05-25 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbook', '0010_alter_course_levels_alter_course_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='levels',
            field=models.ManyToManyField(default=[], null=True, related_name='courses', to='sbook.level'),
        ),
        migrations.AlterField(
            model_name='course',
            name='series',
            field=models.ManyToManyField(default=[], null=True, related_name='courses', to='sbook.serie'),
        ),
    ]