# Generated by Django 4.2 on 2023-05-11 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_tableofcontent_alter_blog_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tableofcontent',
            name='forContent',
        ),
        migrations.AddField(
            model_name='tableofcontent',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.blog'),
        ),
    ]
