# Generated by Django 4.2.6 on 2023-11-01 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0008_tbl_addingcoloring'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_addinghair',
            name='haircuts',
        ),
        migrations.RemoveField(
            model_name='tbl_addinghair',
            name='typesofhair',
        ),
        migrations.RemoveField(
            model_name='tbl_addingstyles',
            name='typesof',
        ),
        migrations.DeleteModel(
            name='tbl_addingcoloring',
        ),
        migrations.DeleteModel(
            name='tbl_addinghair',
        ),
        migrations.DeleteModel(
            name='tbl_addingstyles',
        ),
    ]
