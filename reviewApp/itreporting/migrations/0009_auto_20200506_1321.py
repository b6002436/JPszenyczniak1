# Generated by Django 3.0.5 on 2020-05-06 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itreporting', '0008_review_productname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='dateofrelease',
            field=models.DateField(),
        ),
    ]
