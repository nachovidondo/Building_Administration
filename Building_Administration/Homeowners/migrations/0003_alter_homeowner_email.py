# Generated by Django 3.2 on 2021-04-29 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homeowners', '0002_auto_20210429_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeowner',
            name='email',
            field=models.EmailField(blank=True, default='abc@gmail.com', max_length=254, null=True),
        ),
    ]
