# Generated by Django 3.0.5 on 2020-04-30 13:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('itreporting', '0007_auto_20200427_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='productname',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
