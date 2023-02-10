# Generated by Django 4.1.3 on 2023-02-09 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="body",
        ),
        migrations.RemoveField(
            model_name="post",
            name="pub_date",
        ),
        migrations.AddField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                default=django.utils.timezone.now,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="post",
            name="content",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="post",
            name="created_date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="post",
            name="published_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]