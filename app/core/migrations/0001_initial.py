# Generated by Django 3.1.7 on 2021-02-25 07:12

import core.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_better_admin_arrayfield.models.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=24)),
                ('days', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thuresday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sanday')]), blank=True, null=True, size=7)),
                ('time', models.TimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habits', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
                ('color', models.IntegerField(choices=[(0, 'Grey'), (1, 'Red'), (2, 'Green'), (3, 'Blue'), (4, 'Yellow'), (5, 'Pink'), (6, 'Orange')], default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('note', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('reminder', models.DateTimeField(blank=True, null=True, validators=[core.validators.FutureDateTimeValidator()])),
                ('deadline', models.DateTimeField(blank=True, null=True, validators=[core.validators.FutureDateTimeValidator()])),
                ('done_at', models.DateTimeField(blank=True, null=True)),
                ('priority', models.IntegerField(choices=[(0, 'P0'), (1, 'P1'), (2, 'P2'), (3, 'P3')], default=0, validators=[core.validators.BothIncludedRangeValidator(0, 3)])),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='TaskTag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tag')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.task')),
            ],
            options={
                'ordering': ['tag'],
            },
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(related_name='tasks', through='core.TaskTag', to='core.Tag'),
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('done', models.BooleanField(default=False)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checklist', to='core.task')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HabitLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('done_at', models.DateTimeField(auto_now_add=True)),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='core.habit')),
            ],
        ),
        migrations.AddIndex(
            model_name='tasktag',
            index=models.Index(fields=['task'], name='core_taskta_task_id_75177e_idx'),
        ),
        migrations.AddIndex(
            model_name='tasktag',
            index=models.Index(fields=['tag'], name='core_taskta_tag_id_3ea7d4_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='tasktag',
            unique_together={('task', 'tag')},
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['user'], name='core_task_user_id_d25a04_idx'),
        ),
        migrations.AddConstraint(
            model_name='task',
            constraint=models.CheckConstraint(check=models.Q(('priority__gte', 0), ('priority__lte', 3)), name='valid_priority'),
        ),
        migrations.AddIndex(
            model_name='tag',
            index=models.Index(fields=['user'], name='core_tag_user_id_03846b_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together={('user', 'name')},
        ),
        migrations.AddIndex(
            model_name='habitlog',
            index=models.Index(fields=['habit'], name='core_habitl_habit_i_a968a4_idx'),
        ),
        migrations.AddIndex(
            model_name='habit',
            index=models.Index(fields=['user'], name='core_habit_user_id_24b84d_idx'),
        ),
    ]
