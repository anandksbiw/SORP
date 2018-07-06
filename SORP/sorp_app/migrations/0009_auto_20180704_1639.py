# Generated by Django 2.0.6 on 2018-07-04 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorp_app', '0008_auto_20180702_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='area',
            field=models.CharField(choices=[('---------', '---------'), ('Rural', 'Rural'), ('Urban', 'Urban')], max_length=16),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='gender',
            field=models.CharField(choices=[('---------', '---------'), ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=8),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='int_school_area',
            field=models.CharField(choices=[('---------', '---------'), ('Rural', 'Rural'), ('Urban', 'Urban')], db_column='12th School Area', max_length=8),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='int_school_type',
            field=models.CharField(choices=[('---------', '---------'), ('Government', 'Government School'), ('Private', 'Private School')], db_column='12th School type', max_length=16),
        ),
    ]
