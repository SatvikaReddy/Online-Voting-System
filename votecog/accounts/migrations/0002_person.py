# Generated by Django 3.1 on 2020-09-24 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('year', models.CharField(choices=[('1st', '1ST'), ('2nd', '2ND'), ('3rd', '3RD'), ('4th', '4TH')], default='1st', max_length=6)),
                ('bio', models.TextField(blank=True)),
            ],
        ),
    ]