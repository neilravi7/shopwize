# Generated by Django 4.0.5 on 2023-04-26 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='priduct',
            new_name='product',
        ),
    ]
