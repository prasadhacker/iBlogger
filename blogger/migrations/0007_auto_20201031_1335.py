# Generated by Django 3.1.2 on 2020-10-31 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0006_auto_20201031_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
