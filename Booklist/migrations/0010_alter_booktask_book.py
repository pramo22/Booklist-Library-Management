# Generated by Django 3.2.9 on 2022-06-22 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booklist', '0009_alter_booktask_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktask',
            name='book',
            field=models.FileField(max_length=1000, null=True, upload_to='static/book'),
        ),
    ]
