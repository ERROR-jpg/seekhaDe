# Generated by Django 4.0.3 on 2022-03-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_alter_user_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]