# Generated by Django 4.0 on 2021-12-22 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0006_rename_name_of_trainee_trainee_trainee_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('category', models.CharField(choices=[('Yoga', 'Yoga'), ('Gym', 'Gym'), ('Balanced Nutrition Diet', 'Balanced Nutrition Diet')], max_length=200, null=True)),
                ('date_of_enrolment', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
