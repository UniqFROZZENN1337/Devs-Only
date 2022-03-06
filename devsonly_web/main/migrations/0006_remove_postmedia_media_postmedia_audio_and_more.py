# Generated by Django 4.0.2 on 2022-02-19 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_postmedia_post_text_delete_postelement_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmedia',
            name='media',
        ),
        migrations.AddField(
            model_name='postmedia',
            name='audio',
            field=models.FileField(null=True, upload_to='post/audios/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='postmedia',
            name='file',
            field=models.FileField(null=True, upload_to='post/files/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='postmedia',
            name='image',
            field=models.ImageField(null=True, upload_to='post/images/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='postmedia',
            name='video',
            field=models.FileField(null=True, upload_to='post/videos/%Y/%m/%d/'),
        ),
    ]