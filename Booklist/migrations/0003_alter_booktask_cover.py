# Generated by Django 3.2.9 on 2022-06-20 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booklist', '0002_booktask_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktask',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='static'),
        ),
    ]