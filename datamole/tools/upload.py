# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import os
import datetime


@csrf_exempt  # 取消csrf验证，否则会有403错误
def file_upload(request):
    files = request.FILES.get('upload_file')  # 得到文件对象

    today = datetime.datetime.today()
    today_dir = '/%d/%d/%d/' % (today.year, today.month, today.day)

    file_dir = settings.MEDIA_ROOT + today_dir
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    file_path = file_dir + files.name

    open(file_path, 'wb+').write(files.read())  # 上传文件

    # 得到JSON格式的返回值
    upload_info = {"success": True, 'file_path': settings.MEDIA_URL + today_dir + files.name}
    upload_info = json.dumps(upload_info)

    return HttpResponse(upload_info, content_type="application/json")
