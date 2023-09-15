# Generated by Django 4.2.5 on 2023-09-15 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('cover', models.ImageField(upload_to='thumbnails/%y/%m/%d/')),
                ('logo', models.ImageField(upload_to='logos/%y/%m/%d')),
                ('behance', models.CharField(max_length=10000)),
            ],
        ),
    ]