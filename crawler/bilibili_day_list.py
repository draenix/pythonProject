# -*-coding:utf8-*-
# except exception as e 看出是py3

import argparse
import json

import spider_utils as su


def process(json_dict, output_file_path):
    tag_fo = open(file=output_file_path, mode='w', encoding='utf-8')
    content = json_dict.text
    j = json.loads(content)
    ctt = j["data"]["list"]
    i = 1
    for c in ctt:
        con = str(i) + "\t" + c['title'] + "\n"
        tag_fo.write(con)
        print(con)
        i += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='bilibili_top_list process')
    parser.add_argument('--out-path', type=str, default=None)
    args = parser.parse_args()
    url = "https://api.bilibili.com/x/web-interface/ranking?rid=0&day=1&type=1&arc_type=0"
    json_content = su.spider.get_response(url=url)
    process(json_content, args.out_path)

