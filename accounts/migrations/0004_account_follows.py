# Generated by Django 4.2 on 2023-05-23 19:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_account_first_name_account_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='followed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]