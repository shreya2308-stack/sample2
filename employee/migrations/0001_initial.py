# Generated by Django 3.2 on 2021-04-28 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('ename', models.CharField(max_length=100)),
                ('eemail', models.EmailField(max_length=254)),
                ('econtact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name ='GeeksModel',
            fields =[
                ('id', 
                  models.AutoField(
                  auto_created = True,
                  primary_key = True,
                  serialize = False, 
                  verbose_name ='ID'
                )),
                ('geeks_field', 
                  models.FloatField()),
                ('geeks_field1', 
                  models.DateField()),
                ('geeks_field2', 
                  models.BooleanField()),
                ('geeks_field3', 
                  models.IntegerField()),
            ],
        ),
      
    ]
