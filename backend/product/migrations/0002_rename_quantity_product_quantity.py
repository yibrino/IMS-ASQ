# Generated by Django 5.0.1 on 2024-01-14 10:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="quantity",
            new_name="Quantity",
        ),
    ]
