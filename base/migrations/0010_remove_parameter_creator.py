# Generated by Django 4.0.4 on 2022-12-03 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_parameter_away_resultsint_parameter_home_resulsint_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parameter',
            name='creator',
        ),
    ]
