# Generated by Django 2.1.8 on 2019-05-10 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuanto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(db_column='TeamName', max_length=50)),
                ('cuanto_url', models.TextField(db_column='cuantoURL')),
                ('db_ip', models.CharField(max_length=50)),
                ('db_pass', models.CharField(max_length=50)),
                ('db_user', models.CharField(max_length=50)),
                ('db_port', models.CharField(max_length=10)),
                ('db_name', models.CharField(max_length=50)),
                ('db_connection_status', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'cuanto',
            },
        ),
    ]