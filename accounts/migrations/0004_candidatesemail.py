# Generated by Django 3.0.8 on 2021-02-12 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_candidate_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidatesEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]