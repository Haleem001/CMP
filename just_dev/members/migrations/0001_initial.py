# Generated by Django 4.0.5 on 2022-07-03 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('address', models.TextField(max_length=500)),
                ('phone_no', models.IntegerField(max_length=14)),
                ('nok_first_name', models.CharField(max_length=255)),
                ('nok_last_name', models.CharField(max_length=255)),
                ('nok_surname', models.CharField(max_length=255)),
                ('nok_address', models.TextField(max_length=500)),
                ('nok_phone_no', models.IntegerField(max_length=14)),
                ('nok_relationship', models.CharField(max_length=25)),
            ],
        ),
    ]