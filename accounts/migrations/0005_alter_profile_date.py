# Generated by Django 3.2.6 on 2023-06-29 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.FloatField(default=1688026672.6205463),
        ),
    ]
