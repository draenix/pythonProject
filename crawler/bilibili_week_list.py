# -*-coding:utf8-*-
import json
import logging
import argparse
import spider_utils as su

logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def get_new_week_number():
    weekly_select = "https://app.bilibili.com/x/v2/show/popular/selected/series?type=weekly_selected"
    txt = su.spider.get_response(weekly_select).text
    jon = json.loads(txt)
    return jon['data'][0]['number']


def process_week_list(json_dict, output_file_path):
    tag_fo = open(file=output_file_path, mode='w', encoding='utf-8')
    content = json_dict.text
    j = json.loads(content)
    ctt = j["data"]["list"]
    i = 1
    for c in ctt:
        con = str(i) + "\t" + c['title'] + "\n"
        print(con)
        tag_fo.write(con)
        i += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='bilibili_top_list process')
    parser.add_argument('--out-path', type=str, default=None)
    args = parser.parse_args()
    week_url = "https://app.bilibili.com/x/v2/show/popular/selected?type=weekly_selected&number=" \
               + str(get_new_week_number())
    week_json = su.spider.get_response(url=week_url)
    process_week_list(week_json, args.out_path)
    print("“𝙔𝙤𝙪'𝙧𝙚 𝙨𝙤 𝙗𝙚𝙖𝙪𝙩𝙞𝙛𝙪𝙡”")
