# Generated by Django 5.0.6 on 2024-05-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Members", "0002_alter_myuser_userphoto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myuser",
            name="part",
            field=models.CharField(
                choices=[("BE", "BE"), ("FE", "FE"), ("공통", "공통")], max_length=100
            ),
        ),
    ]