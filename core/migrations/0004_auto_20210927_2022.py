# Generated by Django 3.2.7 on 2021-09-27 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_student_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='th2',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='th3',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='th4',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='th5',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
