# Generated by Django 3.1.7 on 2021-03-22 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210322_1039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='length',
            new_name='height',
        ),
    ]