# Generated by Django 5.2 on 2025-04-18 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_comment_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='news_videos/'),
        ),
    ]
