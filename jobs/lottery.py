import requests
from celery import shared_task


@shared_task
def super_lottery():
    """
    定期检查大乐透开奖结果
    """
    pass
