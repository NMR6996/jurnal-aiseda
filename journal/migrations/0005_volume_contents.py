# Generated by Django 5.0.2 on 2024-02-25 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_volume_is_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='volume',
            name='contents',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]