# Generated by Django 3.0.2 on 2020-01-30 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200130_2035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newscomment',
            old_name='post',
            new_name='news',
        ),
    ]
