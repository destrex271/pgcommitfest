# Generated by Django 4.2.17 on 2025-01-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("commitfest", "0007_needs_rebase_emails"),
    ]

    operations = [
        migrations.RunSQL(
            migrations.RunSQL.noop,
            reverse_sql=migrations.RunSQL.noop,
            state_operations=[
                migrations.RemoveField(
                    model_name="mailthread",
                    name="patches",
                ),
                migrations.AddField(
                    model_name="patch",
                    name="mailthread_set",
                    field=models.ManyToManyField(
                        db_table="commitfest_mailthread_patches",
                        related_name="patches",
                        to="commitfest.mailthread",
                    ),
                ),
            ],
        )
    ]
