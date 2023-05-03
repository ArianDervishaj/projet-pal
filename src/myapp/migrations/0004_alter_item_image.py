# Generated by Django 4.2 on 2023-05-03 08:15

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=myapp.models.generate_filename),
        ),
    ]