# Generated by Django 5.0.1 on 2024-02-17 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_photo',
            field=models.URLField(max_length=500),
        ),
    ]