# Generated by Django 2.2.6 on 2020-01-18 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_articles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.CharField(default='https://thumbs.dreamstime.com/z/article-icon-trendy-design-style-isolated-white-background-vector-simple-modern-flat-symbol-web-site-mobile-logo-app-135744229.jpg', max_length=100000),
        ),
    ]
