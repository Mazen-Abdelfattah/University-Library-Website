# Generated by Django 5.0.6 on 2024-05-12 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_profile_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
