# Generated by Django 3.2.9 on 2022-06-20 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booklist', '0003_alter_booktask_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='booktask',
            name='book',
            field=models.FileField(null=True, upload_to='static/book'),
        ),
    ]
