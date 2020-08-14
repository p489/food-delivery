# Generated by Django 3.0.8 on 2020-08-07 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='thing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thing_title', models.CharField(max_length=250)),
                ('thing_price', models.IntegerField()),
                ('thing_description', models.CharField(max_length=500)),
                ('thing_buy', models.BooleanField(default=False)),
                ('thing_photo', models.FileField(upload_to='')),
            ],
        ),
    ]