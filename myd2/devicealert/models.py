from django.db import models

# Create your models here.
class Device_type(models.Model):
    """设备类型类"""
    tdno = models.IntegerField(primary_key=True, db_column='dtno', verbose_name='设备编号')
    name = models.CharField(max_length=20, db_column='dtname', verbose_name='设备名称')
    class Meta:
        db_table = 'tb_devtype'
    def __str__(self):
        return self.name

class Log_type(models.Model):
    """记录类型类"""
    no = models.IntegerField(primary_key=True, db_column='ltno', verbose_name='提醒编号')
    name = models.CharField(max_length=20, db_column='ltname', verbose_name='提醒类型')
    class Meta:
        db_table = 'tb_logtype'

    def __str__(self):
        return self.name

class Device_sheet(models.Model):
    """设备类"""

    no = models.IntegerField(primary_key=True, db_column='dno', verbose_name='设备编号')
    name = models.CharField(max_length=20, db_column='dname', verbose_name='设备名称')
    describtion = models.CharField(max_length=10, db_column='ddes', verbose_name='设备描述')
    #d_type= models.CharField(max_length=10, db_column='dtype', verbose_name='设备类型')
    dtype = models.ForeignKey(to=Device_type, to_field='tdno', null=True, on_delete=models.PROTECT, verbose_name='设备类型',db_column='dtno')

    class Meta:
        db_table = 'tb_dev'

    def __str__(self):
        return self.name

class Log_sheet(models.Model):
    """记录类"""
    no = models.IntegerField(primary_key=True, db_column='lno', verbose_name='记录编号')
    name = models.CharField(max_length=20, db_column='lname', verbose_name='记录名称')
    logdate=models.DateTimeField(db_column='ldate',verbose_name='记录日期')
    reminddate = models.DateTimeField(db_column='rdate', verbose_name='提醒日期')
    # 自参照完整性多对一外键关联
    '''
    mgr = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='主管编号')
    sal = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='月薪')
    comm = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='补贴')
    '''
    # 多对一外键关联
    dept = models.ForeignKey(Device_sheet, db_column='dno', on_delete=models.PROTECT, verbose_name='记录设备编号')

    class Meta:
        db_table = 'tb_log'

    def __str__(self):
        return self.name

class Device_Log_Type(models.Model):

    no = models.IntegerField(primary_key=True, db_column='lno', verbose_name='链接编号')
    device = models.IntegerField(db_column='device', verbose_name='设备编号')
    types = models.IntegerField(db_column='types', verbose_name='类型编号')

    class Meta:
        db_table = 'tb_device_log_type_link'

    def __str__(self):
        return self.name