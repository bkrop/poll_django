# Generated by Django 3.1.3 on 2020-11-07 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_auto_20201107_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='answer1',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='poll',
            name='answer2',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='poll',
            name='answer3',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='poll',
            name='answer4',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='poll',
            name='answer5',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='choice1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='choice2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='choice3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='choice4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='choice5',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]