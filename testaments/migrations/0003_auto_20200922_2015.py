# Generated by Django 3.1.1 on 2020-09-22 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testaments', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='comment',
            name='testament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='testaments.testament'),
        ),
    ]