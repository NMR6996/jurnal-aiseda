# Generated by Django 5.0.2 on 2024-02-26 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0005_volume_contents'),
    ]

    operations = [
        migrations.AddField(
            model_name='volume',
            name='click_count',
            field=models.IntegerField(default=0),
        ),
    ]
