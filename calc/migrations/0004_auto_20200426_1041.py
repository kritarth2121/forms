# Generated by Django 3.0.4 on 2020-04-26 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_auto_20200426_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BasicChecku', models.CharField(max_length=100)),
                ('ElectricalChecku', models.CharField(max_length=100)),
                ('MechanicalChecku', models.CharField(max_length=100)),
                ('InstallationChecku', models.CharField(max_length=100)),
                ('ChilledwaterChecku', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='BasicChecku',
        ),
        migrations.DeleteModel(
            name='ChilledwaterChecku',
        ),
        migrations.DeleteModel(
            name='ElectricalChecku',
        ),
        migrations.DeleteModel(
            name='InstallationChecku',
        ),
        migrations.DeleteModel(
            name='MechanicalChecku',
        ),
        migrations.DeleteModel(
            name='Name',
        ),
    ]
