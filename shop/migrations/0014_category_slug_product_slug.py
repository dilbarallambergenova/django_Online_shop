# Generated by Django 5.2.4 on 2025-07-23 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0013_remove_category_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name="product",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
