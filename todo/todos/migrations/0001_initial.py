# Generated by Django 5.1.1 on 2024-09-19 16:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField(max_length=256)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_date', models.DateTimeField()),
                ('prority', models.CharField(choices=[('LO', 'LOW'), ('MD', 'MEDIUM'), ('HI', 'HIGH')], default='LO', max_length=2)),
            ],
        ),
    ]
