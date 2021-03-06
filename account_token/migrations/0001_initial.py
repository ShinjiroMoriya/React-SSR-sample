# Generated by Django 2.0.6 on 2018-06-21 12:04

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountToken',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('token', models.CharField(max_length=255)),
                ('expire', models.DateTimeField(default=datetime.datetime.now)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Account')),
            ],
            options={
                'db_table': '"public"."account_token"',
                'ordering': ['-created_date'],
            },
        ),
    ]
