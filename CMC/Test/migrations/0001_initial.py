# Generated by Django 2.2.15 on 2020-08-08 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=250)),
                ('tz', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(max_length=260)),
                ('end_time', models.CharField(max_length=250)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to='Test.User')),
            ],
        ),
    ]
