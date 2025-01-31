# Generated by Django 4.2.17 on 2025-01-31 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("commitfest", "0008_move_mail_thread_many_to_many"),
    ]

    operations = [
        migrations.AddField(
            model_name='cfbotbranch',
            name='all_additions',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cfbotbranch',
            name='all_deletions',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cfbotbranch',
            name='first_additions',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cfbotbranch',
            name='first_deletions',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cfbotbranch',
            name='patch_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cfbotbranch',
            name='version',
            field=models.TextField(blank=True, null=True),
        ),
    ]
