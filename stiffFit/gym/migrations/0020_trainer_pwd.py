# Generated by Django 3.2.9 on 2022-01-02 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0019_auto_20220102_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='pwd',
            field=models.CharField(max_length=50, null=True),
        ),
    ]