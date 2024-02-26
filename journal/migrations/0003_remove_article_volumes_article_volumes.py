# Generated by Django 5.0.2 on 2024-02-25 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_article_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='volumes',
        ),
        migrations.AddField(
            model_name='article',
            name='volumes',
            field=models.ManyToManyField(to='journal.volume'),
        ),
    ]
