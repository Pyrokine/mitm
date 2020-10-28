import json
import time
import mitmproxy.http
from mitmproxy import ctx
import os


def request(flow: mitmproxy.http.HTTPFlow):
    pass


def response(flow: mitmproxy.http.HTTPFlow):
    # ctx.log.info(flow.request.url)
    if 'profile_ext' in flow.request.url:
        ctx.log.info("gotcha")
        result = json.loads(flow.response.get_text())
        general_msg_list = result.get('general_msg_list')

        data = {}
        for i in json.loads(general_msg_list).get('list'):
            app_msg_ext_info = i.get('app_msg_ext_info')
            title = app_msg_ext_info.get('title')
            content_url = app_msg_ext_info.get('content_url')
            author = app_msg_ext_info.get('author')
            comm_msg_info = i.get('comm_msg_info')
            datetime = comm_msg_info.get('datetime')
            publish_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(datetime))
            data.update({title: {"time": publish_time, "author": author, "url": content_url}})

        # 改成公众号的名字用于保存爬取到的内容
        nickname = "CSDN"
        file_path = "content/" + nickname + ".json"
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump({}, f, ensure_ascii=False)

        with open(file_path, "r", encoding="utf-8") as f:
            content = json.load(f)

        content = dict(content, **data)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(content, f, ensure_ascii=False)
