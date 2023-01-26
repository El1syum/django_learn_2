# Generated by Django 4.1.5 on 2023-01-26 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='women',
            old_name='time_create',
            new_name='time_created',
        ),
        migrations.RenameField(
            model_name='women',
            old_name='time_update',
            new_name='time_updated',
        ),
        migrations.AlterField(
            model_name='women',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='women',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d'),
        ),
    ]