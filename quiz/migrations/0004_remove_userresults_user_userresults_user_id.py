# Generated by Django 4.1.7 on 2023-04-02 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0003_alter_userresults_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userresults',
            name='user',
        ),
        migrations.AddField(
            model_name='userresults',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]