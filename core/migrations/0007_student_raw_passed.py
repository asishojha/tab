# Generated by Django 3.2.7 on 2021-10-02 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_student_sylb'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='raw_passed',
            field=models.BooleanField(default=False),
        ),
    ]
