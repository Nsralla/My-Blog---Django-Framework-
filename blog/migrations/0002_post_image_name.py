# Generated by Django 4.2.20 on 2025-04-02 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
