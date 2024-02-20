# Generated by Django 4.2.3 on 2024-02-20 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('extra_info', models.TextField(blank=True, null=True, verbose_name='补充信息')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='上次修改')),
                ('name', models.CharField(help_text='客户名称', max_length=64, unique=True, verbose_name='客户名称')),
                ('address', models.CharField(blank=True, max_length=128, null=True, verbose_name='地址')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='电话')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='电子邮件')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='操作id')),
            ],
            options={
                'verbose_name': '客户信息',
                'verbose_name_plural': '客户信息',
                'db_table': 'customer',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('extra_info', models.TextField(blank=True, null=True, verbose_name='补充信息')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='上次修改')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='项目名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='需求描述')),
                ('attachment', models.FileField(upload_to='project/%Y', verbose_name='客户附件')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='价格')),
                ('hub', models.CharField(blank=True, max_length=128, null=True, verbose_name='代码仓库')),
                ('online', models.CharField(blank=True, max_length=128, null=True, verbose_name='线上地址')),
                ('manifests', models.FileField(blank=True, null=True, upload_to='', verbose_name='交付产物')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='操作id')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='cms.customer', verbose_name='客户')),
            ],
            options={
                'verbose_name': '项目信息',
                'verbose_name_plural': '项目信息',
                'db_table': 'project',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('extra_info', models.TextField(blank=True, null=True, verbose_name='补充信息')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='上次修改')),
                ('name', models.CharField(max_length=64, verbose_name='任务名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='任务描述')),
                ('priority', models.IntegerField(choices=[(0, '一般'), (1, '较高'), (2, '高'), (3, '紧急')], default=0, verbose_name='优先级')),
                ('hours', models.FloatField(default=3, verbose_name='工时')),
                ('status', models.IntegerField(choices=[(0, '未开始'), (1, '进行中'), (2, '已完成')], default=0, verbose_name='任务状态')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='操作id')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='cms.project', verbose_name='所属项目')),
            ],
            options={
                'verbose_name': '任务',
                'verbose_name_plural': '任务',
                'db_table': 'task',
                'ordering': ['create_time', 'project', 'author'],
                'unique_together': {('project', 'author', 'name')},
            },
        ),
    ]