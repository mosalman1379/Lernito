# Generated by Django 3.2.7 on 2021-09-12 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_auto_20210912_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='page',
            field=models.PositiveIntegerField(default=1, verbose_name='تعداد صفحات کتاب'),
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='نام فصل')),
                ('number', models.PositiveSmallIntegerField(verbose_name='شماره فصل')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lesson.book', unique=True)),
            ],
            options={
                'verbose_name_plural': 'فصول کتاب',
                'ordering': ('number',),
            },
        ),
    ]
