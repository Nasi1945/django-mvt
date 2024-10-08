# Generated by Django 4.2 on 2024-08-23 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='events',
            options={'ordering': ('created_at',)},
        ),
    ]
