# Generated by Django 3.0.3 on 2021-04-04 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='automate_text',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
