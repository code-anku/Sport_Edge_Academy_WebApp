# Generated by Django 5.0.2 on 2024-03-04 09:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sa_app', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_name', models.CharField(max_length=55, primary_key=True, serialize=False)),
                ('event_venue', models.CharField(default='Auditorium', max_length=100)),
                ('event_date', models.DateField(default=django.utils.timezone.now)),
                ('event_description', models.TextField()),
                ('event_pic', models.FileField(default='', upload_to='sa_app/event_images')),
            ],
        ),
    ]
