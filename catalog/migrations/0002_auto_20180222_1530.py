# Generated by Django 2.0.1 on 2018-02-22 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.TextField(choices=[('I', 'Inactive'), ('A', 'Active')], default='A'),
        ),
    ]
