# Generated by Django 4.1.7 on 2023-04-03 17:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kitchen", "0002_alter_cook_years_of_experience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]
