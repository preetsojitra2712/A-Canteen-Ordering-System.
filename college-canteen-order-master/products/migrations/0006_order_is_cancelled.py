# Generated by Django 2.2.1 on 2019-10-20 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_order_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_cancelled',
            field=models.BooleanField(default=False),
        ),
    ]
