# Generated by Django 4.1.3 on 2022-11-20 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApplication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('userId', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('adminCheck', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'admin',
            },
        ),
        migrations.CreateModel(
            name='SimpleUser',
            fields=[
                ('userId', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'utilisateur',
            },
        ),
    ]