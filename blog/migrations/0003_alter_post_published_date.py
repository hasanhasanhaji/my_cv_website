# Generated by Django 5.0 on 2024-01-02 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_alter_post_options_post_author_post_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(),
        ),
    ]
