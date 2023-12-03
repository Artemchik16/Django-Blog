# Generated by Django 4.2.7 on 2023-12-03 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="posts",
            name="tags",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="Blog.tags",
                verbose_name="Теги",
            ),
        ),
    ]
