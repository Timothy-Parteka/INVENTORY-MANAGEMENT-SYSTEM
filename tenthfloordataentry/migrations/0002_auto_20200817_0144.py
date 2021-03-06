# Generated by Django 3.0.8 on 2020-08-16 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenthfloordataentry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FloorLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='tenthfloordataentrydesktop',
            name='location',
        ),
        migrations.AddField(
            model_name='tenthfloordataentrydesktop',
            name='floor_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tenthfloordataentry.FloorLocation'),
        ),
    ]
