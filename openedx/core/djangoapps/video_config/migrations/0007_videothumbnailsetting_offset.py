# Generated by Django 1.11.15 on 2018-09-25 13:41


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_config', '0006_videothumbnailetting_updatedcoursevideos'),
    ]

    operations = [
        migrations.AddField(
            model_name='videothumbnailsetting',
            name='offset',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
