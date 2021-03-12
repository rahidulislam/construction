# Generated by Django 3.1.4 on 2020-12-02 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201202_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_title', models.CharField(max_length=100)),
                ('slider_subtitle', models.CharField(max_length=255)),
                ('slider_tag', models.CharField(max_length=50)),
            ],
        ),
    ]