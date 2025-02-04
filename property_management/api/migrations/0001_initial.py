# Generated by Django 5.0.6 on 2024-07-01 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('property_type', models.CharField(choices=[('house', 'House'), ('apartment', 'Apartment'), ('office', 'Office')], max_length=20)),
                ('surface', models.FloatField()),
            ],
        ),
    ]
