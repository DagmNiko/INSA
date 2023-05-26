# Generated by Django 4.2 on 2023-05-24 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0017_proofimages_talentapplication'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talentapplication',
            name='applied',
        ),
        migrations.AlterField(
            model_name='talentapplication',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
