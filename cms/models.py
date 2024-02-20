from django.db import models

from cms import settings


class BaseModel(models.Model):
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='操作id', related_name='+', null=True, blank=True)
    remarks = models.TextField(blank=True, null=True, verbose_name='备注')
    extra_info = models.TextField(blank=True, null=True, verbose_name='补充信息')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='上次修改')

    class Meta(object):
        abstract = True


class Customer(BaseModel):
    name = models.CharField(max_length=64, unique=True, blank=False, verbose_name='客户名称', help_text='客户名称')
    address = models.CharField(max_length=128, blank=True, null=True, verbose_name='地址')
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name='电话')
    email = models.EmailField(blank=True, null=True, verbose_name='电子邮件')

    class Meta:
        verbose_name = "客户信息"
        verbose_name_plural = verbose_name
        ordering = ['id']
        db_table = 'customer'

    def __str__(self):
        return self.name


class Project(BaseModel):
    name = models.CharField(max_length=64, blank=False, verbose_name='项目名称', unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name='客户', related_name='projects')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='作者', related_name='projects')
    description = models.TextField(blank=True, null=True, verbose_name='需求描述')
    attachment = models.FileField(upload_to='project/%Y', verbose_name='客户附件')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='价格', default=0)
    hub = models.CharField(max_length=128, blank=True, null=True, verbose_name='代码仓库')
    online = models.CharField(max_length=128, blank=True, null=True, verbose_name='线上地址')
    manifests = models.FileField(blank=True, null=True, verbose_name='交付产物')

    class Meta:
        verbose_name = "项目信息"
        verbose_name_plural = verbose_name
        ordering = ['id']
        db_table = 'project'

    def __str__(self):
        return self.name


priorities = (
    (0, "一般"),
    (1, "较高"),
    (2, "高"),
    (3, "紧急"),
)

status = (
    (0, "未开始"),
    (1, "进行中"),
    (2, "已完成"),
)


class Task(BaseModel):
    name = models.CharField(max_length=64, blank=False, verbose_name='任务名称')
    project = models.ForeignKey(Project, on_delete=models.PROTECT, verbose_name='所属项目', related_name='tasks')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='作者', related_name='tasks')
    description = models.TextField(blank=True, null=True, verbose_name='任务描述')
    priority = models.IntegerField(default=0, verbose_name='优先级', choices=priorities)
    hours = models.FloatField(default=3, verbose_name='工时', null=False, blank=False)
    status = models.IntegerField(default=0, verbose_name='任务状态', choices=status)

    class Meta:
        verbose_name = "任务"
        verbose_name_plural = verbose_name
        ordering = ['create_time', 'project', 'author']
        db_table = 'task'
        unique_together = ('project', 'author', 'name')

    def __str__(self):
        return self.name
