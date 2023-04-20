# Generated by Django 3.2.3 on 2021-06-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('receiver', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('period', models.DateField()),
                ('month', models.IntegerField()),
            ],
        ),
    ]
