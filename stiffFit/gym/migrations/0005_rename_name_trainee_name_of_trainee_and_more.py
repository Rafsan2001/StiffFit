# Generated by Django 4.0 on 2021-12-22 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0004_trainee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainee',
            old_name='name',
            new_name='name_of_trainee',
        ),
        migrations.RenameField(
            model_name='trainer',
            old_name='name',
            new_name='name_of_trainer',
        ),
    ]
