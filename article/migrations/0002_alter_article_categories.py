# Generated by Django 5.2.1 on 2025-06-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='categories.category'),
        ),
    ]
