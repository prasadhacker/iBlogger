# Generated by Django 3.1.2 on 2020-10-26 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0002_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]