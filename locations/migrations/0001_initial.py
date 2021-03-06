# Generated by Django 2.2.10 on 2020-03-03 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('iso2', models.CharField(max_length=2, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('cid', models.IntegerField(unique=True)),
                ('latitude', models.CharField(max_length=25)),
                ('longitude', models.CharField(max_length=25)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='locations.Country')),
            ],
            options={
                'verbose_name_plural': 'Cities',
                'ordering': ('country', 'name'),
                'unique_together': {('name', 'latitude', 'longitude')},
            },
        ),
    ]
