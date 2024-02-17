# Generated by Django 5.0.1 on 2024-02-17 18:39

import petstagram.photos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_petphoto_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphoto',
            name='photo',
            field=models.ImageField(upload_to='pet/photos', validators=[petstagram.photos.models.MaxFileSizeValidator(limit_value=5242880)]),
        ),
    ]
