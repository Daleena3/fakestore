# Generated by Django 4.1.3 on 2022-12-08 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modeles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('band', models.CharField(max_length=200)),
                ('specs', models.CharField(max_length=230)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
