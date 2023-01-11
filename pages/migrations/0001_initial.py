# Generated by Django 4.1.4 on 2023-01-10 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('permalink', models.CharField(max_length=50, unique=True)),
                ('update_date', models.DateField(auto_now_add=True)),
                ('bodytext', models.TextField(blank=True)),
            ],
        ),
    ]
