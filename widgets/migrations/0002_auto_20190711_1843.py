# Generated by Django 2.1.3 on 2019-07-11 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widget',
            name='desc',
            field=models.TextField(max_length=200),
        ),
    ]