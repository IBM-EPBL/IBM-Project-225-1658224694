# Generated by Django 4.1.2 on 2022-11-05 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rsim', '0002_delete_dataset'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mart_name', models.CharField(blank=True, max_length=9, null=True)),
                ('name', models.CharField(blank=True, max_length=15, null=True)),
                ('product_id', models.CharField(blank=True, max_length=10, null=True)),
                ('expirydate', models.CharField(blank=True, db_column='Expirydate', max_length=11, null=True)),
                ('cp', models.CharField(blank=True, max_length=4, null=True)),
                ('sp', models.CharField(blank=True, max_length=4, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dataset',
            },
        ),
    ]
