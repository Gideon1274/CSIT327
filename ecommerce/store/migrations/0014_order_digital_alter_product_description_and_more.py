# Generated by Django 5.1.1 on 2024-12-09 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_category_name_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='digital',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
