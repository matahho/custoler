# Generated by Django 4.2.9 on 2024-03-07 18:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("comments", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="post_id",
            field=models.CharField(default=None, max_length=255),
        ),
    ]
