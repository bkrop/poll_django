# Generated by Django 3.1.3 on 2020-11-07 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20201107_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='choice1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='poll',
            name='choice2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='poll',
            name='choice3',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='poll',
            name='choice4',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='poll',
            name='choice5',
            field=models.IntegerField(default=0),
        ),
    ]
