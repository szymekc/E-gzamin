# Generated by Django 3.0.7 on 2020-06-20 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_gzamin_app', '0004_auto_20200607_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testresult',
            name='completedAt',
        ),
        migrations.AlterField(
            model_name='testresult',
            name='finishedAt',
            field=models.DateTimeField(null=True),
        ),
    ]
