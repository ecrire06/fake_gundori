# Generated by Django 4.1.3 on 2022-11-27 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fake_gundori', '0006_soldier_password_alter_soldier_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldier',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='password',
            field=models.CharField(default='password', max_length=20),
        ),
    ]
