from datetime import datetime

from django.db import models

# Create your models here.
# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.timezone import now

class Test(models.Model):
    name = models.CharField(max_length=20)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

class Report(models.Model):
    # 报告编号 - 假设每个报告都有一个唯一的编号
    report_number = models.CharField(max_length=100, unique=True,default='0000')
   # 用户 ID - 假设这是指向 Patient 模型的外键

    # 姓名
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=timezone.now)
    # 性别
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    # 年龄 - 假设以年为单位
    age = models.IntegerField(default=0)

    # 报告状态
    STATUS_CHOICES = (
        ('CREATED', 'Created'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('ARCHIVED', 'Archived'),
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES,default='CREATED')
    # vision_normal,三个选项，分别是裸眼视力正常， 矫正视力正常，不正常
    vision_normal_choices = (
        ('N', 'Normal'),
        ('C', 'Corrected'),
        ('A', 'Abnormal'),
    )
    vision_normal = models.CharField(max_length=100, choices=vision_normal_choices,default='N')
    eye_diseases_choices = (
        ('None', 'None'),
        ('Blindness', 'Blindness'),
        ('Nystagmus', 'Nystagmus'),
        ('Amblyopia', 'Amblyopia'),
        ('Amblyopia', 'Amblyopia'),
        ('Strabismus', 'Strabismus'),
        ('Ptosis', 'Ptosis'),
        ('Epiphora', 'Epiphora'),
        ('Other', 'Other Eye Diseases'),
    )
    eye_diseases = models.CharField(max_length=50, choices=eye_diseases_choices,default='None')
    # 监护人姓名和电话
    guardian_name = models.CharField(max_length=100)
    guardian_phone = models.CharField(max_length=20)
    guardian_email = models.EmailField(default= None)
    # 参试日期
    test_date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    # 主试人
    principal_investigator = models.CharField(max_length=100,default='zhangsan')

    # 创建时间和更新时间
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    pdf_path = models.CharField(max_length=1000, blank=True)
    def __str__(self):
        return f"Report {self.report_number} - {self.name}"

class Employee(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100, default='123456')
    gonghao = models.CharField(max_length=100, default='00000000')
    status = models.CharField(max_length=50, default='启用中')  # 假设“启用中”和“禁用中”
    position = models.CharField(max_length=50)  # 职位
    phone = models.CharField(max_length=15)  # 手机号
    create_time = models.DateTimeField(default=datetime.now)  # 创建时间并提供默认值
    signature = models.ImageField(upload_to='signatures/', default='/media/sign.jpg')  # 签名图片

def user_directory_path(instance, filename):
    # 文件将被上传到 MEDIA_ROOT/user_<id>/<日期>/<filename>
    return 'user_{0}/{1}/{2}'.format(instance.patient.id, now().strftime("%Y%m%d"), filename)
