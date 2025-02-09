import datetime
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRacer',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name')),
                ('patronymic', models.CharField(max_length=30, null=True, verbose_name='Patronymic')),
                ('team', models.CharField(max_length=30, null=True, verbose_name='Team')),
                ('member_descr', models.TextField(null=True, verbose_name='Team member description')),
                ('car_descr', models.TextField(null=True, verbose_name='Car description')),
                ('experience_years', models.IntegerField(null=True, verbose_name='Experience in years')),
                ('user_class', models.CharField(choices=[('C', 'Non-pro'), ('B', 'Experienced'), ('A', 'Professional'), ('L', 'Another')], default='L', max_length=30, verbose_name="User's class")),
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Username')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('num_race', models.AutoField(primary_key=True, serialize=False, verbose_name='Race number')),
                ('name_race', models.CharField(max_length=50, verbose_name='Race name')),
                ('date_race', models.DateTimeField(unique=True, verbose_name='Race date')),
                ('place_race', models.CharField(max_length=50, verbose_name='Race place')),
                ('first_place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('second_place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sec_place', to=settings.AUTH_USER_MODEL)),
                ('third_place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='th_pace', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('num_reg', models.AutoField(primary_key=True, serialize=False, verbose_name='Registration number')),
                ('num_race_reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='race_winners_app.race')),
                ('num_user_reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id_review', models.AutoField(primary_key=True, serialize=False)),
                ('time_race', models.DateTimeField(verbose_name='Race date and time')),
                ('comment_time', models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 26, 15, 43, 17, 235222))),
                ('rate', models.IntegerField(blank=True, default=10, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Rating')),
                ('comment_type', models.CharField(choices=[('RACE_Q', 'Question about race'), ('COLLAB_Q', 'Question about collaboration'), ('OTHER', 'Other')], max_length=30, verbose_name='Comment type')),
                ('text', models.TextField(verbose_name='Comment')),
                ('num_race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='race_winners_app.race')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
