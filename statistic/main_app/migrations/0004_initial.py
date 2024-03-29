# Generated by Django 4.2.10 on 2024-02-13 09:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_app', '0003_delete_daily_works_delete_habits_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habits_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Daily_Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('day_work', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('workduration', models.DurationField(default=datetime.timedelta(0))),
                ('works_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_works', to='main_app.habits_category')),
            ],
        ),
    ]
