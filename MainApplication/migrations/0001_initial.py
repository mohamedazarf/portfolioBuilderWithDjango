# Generated by Django 4.1.3 on 2022-11-20 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('accountId', models.IntegerField(primary_key=True, serialize=False)),
                ('login', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'compte',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whoisyou', models.TextField(blank=True, max_length=1000, null=True)),
                ('whatdoesyoudo', models.TextField(blank=True, max_length=1000, null=True)),
                ('His_career_summary', models.TextField(blank=True, max_length=1000, null=True)),
                ('A_short_biography', models.TextField(blank=True, max_length=1000, null=True)),
                ('Professional_accomplishments', models.TextField(blank=True, max_length=1000, null=True)),
                ('Awards_and_honors', models.TextField(blank=True, max_length=1000, null=True)),
                ('Transcripts_degrees_licenses_certifications', models.TextField(blank=True, max_length=1000, null=True)),
                ('Volunteering_community_service', models.TextField(blank=True, max_length=1000, null=True)),
                ('References_testimonials', models.TextField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'portfeuille',
            },
        ),
    ]
