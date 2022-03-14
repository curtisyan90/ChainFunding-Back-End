# Generated by Django 3.2.5 on 2022-03-13 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprojectapp', '0002_transferlogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundingProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nftId', models.PositiveIntegerField()),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('token', models.CharField(max_length=100)),
                ('buyPrice', models.DecimalField(decimal_places=4, max_digits=4)),
                ('sellPrice', models.DecimalField(decimal_places=4, max_digits=4)),
                ('gasPrice', models.DecimalField(decimal_places=4, max_digits=4)),
                ('fundraiser', models.CharField(max_length=100)),
            ],
        ),
    ]
