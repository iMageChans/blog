from django.db import models


class Main(models.Model):

    dateTime = models.CharField(
        '日期',
        max_length=70,
        help_text='日期'
    )

    regMember = models.CharField(
        '注册人数',
        max_length=70,
        help_text='注册人数'
    )

    toDayActivity = models.CharField(
        '总日活',
        max_length=70,
        help_text='总日活'
    )

    memberToDayActivity = models.CharField(
        '会员日活',
        max_length=70,
        help_text='会员日活'
    )

    memberQuantityPaid = models.CharField(
        '会员付费人数',
        max_length=70,
        help_text='会员付费人数'
    )

    totalMemberPayments = models.CharField(
        '会员付费金额',
        max_length=70,
        help_text='会员付费金额'
    )

    candyPaymentQuantity = models.CharField(
        '糖果付费人数',
        max_length=70,
        help_text='糖果付费人数'
    )

    totalCandyPayment = models.CharField(
        '糖果付费金额',
        max_length=70,
        help_text='糖果付费金额'
    )

    memberConversionRate = models.CharField(
        '会员转化率',
        max_length=70,
        help_text='会员转化率',
        null=True,
        blank=True
    )

    candyConversion = models.CharField(
        '糖果转化率',
        max_length=70,
        help_text='糖果转化率',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = '详细统计'
        verbose_name_plural = verbose_name


class Simple(models.Model):

    memberAdd = models.CharField(
        '新增用户',
        max_length=70,
        help_text='新增用户'
    )

    activeUsers = models.CharField(
        '活跃用户',
        max_length=70,
        help_text='活跃用户'
    )

    quantityPaid = models.CharField(
        '充值人数',
        max_length=70,
        help_text='充值人数'
    )

    totalRecharge = models.CharField(
        '充值金额',
        max_length=70,
        help_text='充值金额'
    )

    class Meta:
        verbose_name = '概况'
        verbose_name_plural = verbose_name
