# Generated by Django 5.1.4 on 2024-12-27 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_user_hackthon_participant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='hackthon_participant',
            new_name='hackathon_participant',
        ),
    ]
