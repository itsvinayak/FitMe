from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'trainee',
            },
        ),
        migrations.CreateModel(
            name='TraineeAddress',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('house_no', models.IntegerField()),
                ('street_no', models.IntegerField()),
                ('village', models.CharField(max_length=30)),
                ('post', models.CharField(max_length=30)),
                ('dist_city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
            ],
            options={
                'db_table': 'trainee_address',
            },
        ),
        migrations.CreateModel(
            name='TraineePhy',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('height', models.DecimalField(decimal_places=2, max_digits=3)),
                ('age', models.IntegerField()),
                ('current_weight', models.DecimalField(decimal_places=2, max_digits=3)),
                ('goal_weight', models.DecimalField(decimal_places=2, max_digits=3)),
                ('health_condition', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'trainee_phy',
            },
        ),
    ]
