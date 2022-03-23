# Generated by Django 4.0.3 on 2022-03-22 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_alter_user_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='bio',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='contact',
            field=models.TextField(max_length=15),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='country',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='email',
            field=models.EmailField(max_length=35),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='profile_pic',
            field=models.ImageField(upload_to='Images', verbose_name='Profile Picture'),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='quote',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='zip_code',
            field=models.CharField(max_length=10),
        ),
    ]