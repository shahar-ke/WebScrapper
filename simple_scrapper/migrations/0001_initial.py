# Generated by Django 2.2.7 on 2019-11-28 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapResult',
            fields=[
                ('key', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('expected', models.IntegerField()),
                ('found', models.IntegerField()),
            ],
        ),
    ]