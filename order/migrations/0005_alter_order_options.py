# Generated by Django 4.0.5 on 2023-05-01 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_orderitem_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created_at',)},
        ),
    ]