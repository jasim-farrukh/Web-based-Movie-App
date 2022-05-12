# Generated by Django 4.0.4 on 2022-05-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1048)),
                ('image', models.ImageField(upload_to='foodItem_pics')),
                ('duration', models.IntegerField()),
                ('genre', models.CharField(max_length=40)),
                ('language', models.CharField(max_length=44)),
                ('type', models.CharField(max_length=20)),
                ('label', models.CharField(max_length=255)),
                ('userRating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
