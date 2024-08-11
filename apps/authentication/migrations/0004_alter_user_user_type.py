# Generated by Django 5.0.7 on 2024-08-07 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Admin'), (2, 'Manager'), (3, 'Accountant')], default=1),
        ),
    ]
