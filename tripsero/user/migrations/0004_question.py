# Generated by Django 3.2.4 on 2021-06-16 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_mymodel_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('QNo', models.IntegerField(default=0)),
                ('Question', models.CharField(max_length=200)),
                ('A1', models.CharField(max_length=200)),
                ('A2', models.CharField(max_length=200)),
                ('A3', models.CharField(max_length=200)),
                ('A4', models.CharField(max_length=200)),
            ],
        ),
    ]