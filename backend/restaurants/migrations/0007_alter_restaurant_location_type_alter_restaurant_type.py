# Generated by Django 4.1.3 on 2022-11-19 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_alter_restaurant_location_type_alter_restaurant_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='location_type',
            field=models.CharField(choices=[('south_gate', '남문'), ('front_gate', '정문'), ('sinchon', '신촌'), ('daeheung', '대흥'), ('back_gate', '후문')], max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='type',
            field=models.CharField(choices=[('japanese', '일식'), ('korean', '한식'), ('chinese', '중식'), ('western', '양식')], max_length=20),
        ),
    ]
