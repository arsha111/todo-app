# Generated by Django 5.0.1 on 2024-02-17 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserTBL',
            fields=[
                ('Name', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]