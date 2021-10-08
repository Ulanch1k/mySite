# Generated by Django 3.2.7 on 2021-10-06 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=40)),
                ('description', models.TextField(null=True)),
                ('release_date', models.DateField()),
                ('director', models.CharField(max_length=40)),
            ],
        ),
    ]