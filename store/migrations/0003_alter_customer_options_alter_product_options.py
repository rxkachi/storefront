# Generated by Django 5.0.2 on 2024-02-20 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_collection_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ('first_name', 'last_name')},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('title',)},
        ),
    ]
