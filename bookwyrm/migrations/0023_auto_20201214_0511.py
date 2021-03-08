# Generated by Django 3.0.7 on 2020-12-14 05:11

import bookwyrm.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0022_auto_20201212_1744"),
    ]

    operations = [
        migrations.AlterField(
            model_name="status",
            name="privacy",
            field=bookwyrm.models.fields.PrivacyField(
                choices=[
                    ("public", "Public"),
                    ("unlisted", "Unlisted"),
                    ("followers", "Followers"),
                    ("direct", "Direct"),
                ],
                default="public",
                max_length=255,
            ),
        ),
    ]
