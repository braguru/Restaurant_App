# Generated by Django 4.1.2 on 2023-05-19 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu_items',
            options={'ordering': ('Title',), 'verbose_name_plural': 'Menu Items'},
        ),
        migrations.RenameField(
            model_name='menu_items',
            old_name='price',
            new_name='Price',
        ),
        migrations.RenameField(
            model_name='menu_items',
            old_name='title',
            new_name='Title',
        ),
    ]
