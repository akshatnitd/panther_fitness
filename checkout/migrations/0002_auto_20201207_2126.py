# Generated by Django 3.1.3 on 2020-12-07 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='line_item_total',
            new_name='lineitem_total',
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(max_length=50),
        ),
    ]