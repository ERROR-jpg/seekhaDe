# Generated by Django 4.0.3 on 2022-03-30 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_posts_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='posts/images'),
        ),
    ]
