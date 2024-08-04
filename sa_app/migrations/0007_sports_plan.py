# Generated by Django 5.0.2 on 2024-03-18 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sa_app', '0006_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sports_Plan',
            fields=[
                ('plan_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('plan_duration', models.CharField(max_length=100)),
                ('facilities', models.TextField(max_length=500)),
                ('charges', models.IntegerField()),
            ],
        ),
    ]