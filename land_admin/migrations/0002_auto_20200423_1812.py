# Generated by Django 3.0.4 on 2020-04-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landadminbarcodescanner',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
