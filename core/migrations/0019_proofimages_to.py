# Generated by Django 4.2 on 2023-05-24 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_remove_talentapplication_applied_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proofimages',
            name='to',
            field=models.CharField(blank=True, max_length=230),
        ),
    ]
