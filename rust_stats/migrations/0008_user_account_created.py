# Generated by Django 3.0.6 on 2020-06-18 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rust_stats', '0007_user_friends_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_created',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]