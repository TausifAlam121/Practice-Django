# Generated by Django 3.1.4 on 2021-01-02 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210102_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='pub_date',
            new_name='publish_date',
        ),
    ]