# Generated by Django 2.2.18 on 2021-05-04 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findings', '0008_findingoverride'),
    ]

    operations = [
        migrations.AlterField(
            model_name='findingoverride',
            name='action',
            field=models.CharField(choices=[('set-status', 'Set custom status'), ('set-severity', 'Set custom severity')], default='set-status', max_length=32),
        ),
    ]
