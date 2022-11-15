# Generated by Django 4.1.3 on 2022-11-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='contacts',
        ),
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]