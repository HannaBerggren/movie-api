# Generated by Django 3.2.19 on 2023-06-11 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_image_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../movie-post', upload_to='images/'),
        ),
    ]
