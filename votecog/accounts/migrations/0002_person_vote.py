# Generated by Django 3.1 on 2020-10-26 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
