# Generated by Django 4.2 on 2023-05-20 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_video_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='tableofcontent',
            name='news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.news'),
        ),
    ]