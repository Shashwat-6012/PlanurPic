# Generated by Django 4.0.4 on 2022-08-09 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_category_name_category_cat_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=8)),
            ],
        ),
    ]
