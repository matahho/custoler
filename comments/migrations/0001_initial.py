# Generated by Django 4.2.9 on 2024-03-07 18:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField()),
                ('username', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('answers', models.JSONField()),
            ],
        ),
    ]
