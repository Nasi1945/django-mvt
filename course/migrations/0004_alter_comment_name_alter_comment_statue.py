# Generated by Django 4.2 on 2024-08-31 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='comment',
            name='statue',
            field=models.BooleanField(default=False),
        ),
    ]
