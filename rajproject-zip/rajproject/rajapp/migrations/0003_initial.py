# Generated by Django 4.2.2 on 2023-08-05 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rajapp', '0002_delete_customer_delete_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('Address', models.TextField()),
                ('account', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=50)),
                ('parent_selection', models.CharField(max_length=100)),
            ],
        ),
    ]
