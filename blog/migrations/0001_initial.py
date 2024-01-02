# Generated by Django 5.0 on 2024-01-02 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('content', models.TextField()),
                ('counted_views', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('published_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]