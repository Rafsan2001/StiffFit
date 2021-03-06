# Generated by Django 4.0 on 2021-12-21 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0003_trainer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('age', models.FloatField(null=True)),
                ('height', models.FloatField(null=True)),
                ('weight', models.FloatField(null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('profile_picture', models.ImageField(blank=True, default='default_profile.jpg', null=True, upload_to='')),
            ],
        ),
    ]
