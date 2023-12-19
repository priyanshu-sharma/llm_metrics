# Generated by Django 4.2.8 on 2023-12-19 08:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Prompt',
            fields=[
                ('install_ts', models.DateTimeField(auto_now_add=True)),
                ('update_ts', models.DateTimeField(auto_now=True)),
                ('created_by_id', models.IntegerField(blank=True, null=True)),
                ('updated_by_id', models.IntegerField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('run_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('sentence', models.TextField()),
                (
                    'llm_models',
                    models.TextField(
                        choices=[('BARD', 'BARD'), ('BART', 'BART'), ('CHAT_GPT', 'CHAT_GPT')], default='CHAT_GPT'
                    ),
                ),
                (
                    'prompt_status',
                    models.TextField(
                        choices=[('COMPLETED', 'COMPLETED'), ('CREATED', 'CREATED'), ('RETRIGGERED', 'RETRIGGERED')],
                        default='CREATED',
                    ),
                ),
                ('meta', models.JSONField(default=dict)),
                ('active', models.BooleanField()),
            ],
            options={
                'db_table': 'prompt',
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('install_ts', models.DateTimeField(auto_now_add=True)),
                ('update_ts', models.DateTimeField(auto_now=True)),
                ('created_by_id', models.IntegerField(blank=True, null=True)),
                ('updated_by_id', models.IntegerField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('result', models.TextField()),
                ('overall_metrics', models.JSONField(default=dict)),
                ('meta', models.JSONField(default=dict)),
                ('active', models.BooleanField()),
                (
                    'prompt',
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluation_domain.prompt'),
                ),
            ],
            options={
                'db_table': 'response',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('install_ts', models.DateTimeField(auto_now_add=True)),
                ('update_ts', models.DateTimeField(auto_now=True)),
                ('created_by_id', models.IntegerField(blank=True, null=True)),
                ('updated_by_id', models.IntegerField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                (
                    'rating_type',
                    models.TextField(
                        choices=[('LLM_ASSISTED', 'LLM_ASSISTED'), ('MANUAL', 'MANUAL')], default='LLM_ASSISTED'
                    ),
                ),
                ('metrics', models.JSONField(default=dict)),
                ('meta', models.JSONField(default=dict)),
                (
                    'response',
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluation_domain.response'),
                ),
            ],
            options={
                'db_table': 'rating',
            },
        ),
        migrations.AddIndex(
            model_name='prompt',
            index=models.Index(fields=['run_id'], name='prompt_run_id_776f46_idx'),
        ),
    ]
