# Generated by Django 3.0.4 on 2020-04-26 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_auto_20200425_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='ElectricalCheckup',
            new_name='ChilledwaterChecku',
        ),
        migrations.RenameModel(
            old_name='ChilledwaterCheckup',
            new_name='ElectricalChecku',
        ),
        migrations.RenameModel(
            old_name='InstallationCheckup',
            new_name='InstallationChecku',
        ),
        migrations.RenameModel(
            old_name='MechanicalCheckup',
            new_name='MechanicalChecku',
        ),
    ]
