# Generated by Django 3.2.9 on 2022-06-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booklist', '0007_alter_booktask_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktask',
            name='book',
            field=models.FileField(null=True, upload_to='book'),
        ),
    ]