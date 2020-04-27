# Generated by Django 3.0.5 on 2020-04-25 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itreporting', '0003_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.TextField()),
                ('brand', models.TextField()),
                ('averagecost', models.CharField(max_length=1000)),
                ('dateofrelease', models.DateTimeField()),
                ('description', models.TextField()),
            ],
        ),
    ]
