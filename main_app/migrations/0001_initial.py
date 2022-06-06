# Generated by Django 4.0.4 on 2022-06-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=500)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
