# Generated by Django 5.0.6 on 2024-05-30 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persons',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
