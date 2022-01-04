# Generated by Django 4.0 on 2022-01-04 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0004_trainernotification'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotifTrainerStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('notif_msg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.trainernotification')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.trainer')),
            ],
            options={
                'verbose_name_plural': 'Trainer Notification Status',
            },
        ),
    ]