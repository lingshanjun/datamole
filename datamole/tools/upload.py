# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import os
import datetime

import cloudinary
import cloudinary.uploader
import cloudinary.api

from datamole.settings.safe_data import cloudinary_data
print cloudinary_data

# use to upload file to local media folders
# @csrf_exempt  # 取消csrf验证，否则会有403错误
# def file_upload(request):
#     files = request.FILES.get('upload_file')  # 得到文件对象
#
#     today = datetime.datetime.today()
#     today_dir = '/%d/%d/%d/' % (today.year, today.month, today.day)
#
#     file_dir = settings.MEDIA_ROOT + today_dir
#     if not os.path.exists(file_dir):
#         os.makedirs(file_dir)
#     file_path = file_dir + files.name
#
#     open(file_path, 'wb+').write(files.read())  # 上传文件
#
#     # 得到JSON格式的返回值
#     upload_info = {"success": True, 'file_path': settings.MEDIA_URL + today_dir + files.name}
#     upload_info = json.dumps(upload_info)
#
#     return HttpResponse(upload_info, content_type="application/json")


cloudinary.config(
    cloud_name=cloudinary_data['cloud_name'],
    api_key=cloudinary_data['api_key'],
    api_secret=cloudinary_data['api_secret']
)


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

    data = cloudinary.uploader.upload(file_path)

    # 得到JSON格式的返回值
    upload_info = {"success": True, 'file_path': data['url']}
    upload_info = json.dumps(upload_info)

    # 删除本地图片
    os.remove(file_path)
    os.removedirs(file_dir)
    return HttpResponse(upload_info, content_type="application/json")
