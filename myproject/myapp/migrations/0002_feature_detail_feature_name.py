# Generated by Django 4.0.5 on 2022-07-12 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='detail',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
