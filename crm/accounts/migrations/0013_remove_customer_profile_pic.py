# Generated by Django 3.1.3 on 2020-11-20 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_remove_order_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
    ]
