import requests, os, time
import pandas as pd

from parsel import Selector
from datetime import datetime, timedelta

import multiprocessing, urllib
import gzip, shutil
import socket

# 设置超时时间为30s
socket.setdefaulttimeout(30)

# pip install parsel

start_date = datetime(year=2014, month=11, day=22)


def print_date(date):
    return date.strftime("%Y%m%d")


def create_dates(starting_from):
    delta = datetime.today() - timedelta(days=2) - start_date  # timedelta # 最多爬取到当前时间的前天
    date_list = [start_date + timedelta(days=x) for x in range(0, delta.days)]
    return date_list


def save_links(dl_folder, links, starting_from, base_url):
    date_list = create_dates(starting_from)
    for i in map(print_date, date_list):
        links.append(base_url + i + ".csv.gz")
        print(base_url + i + ".csv.gz")
    return links


def process_url(link):
    print(link)

    if not (".gz" in link or ".zip" in link):
        print("not a dl link")
        return

    filename = link.split("/")[-1]
    dl_folder = link.split("/")[-2]
    filepath = os.path.join(dl_folder, filename)
    try:
        csvpath = os.path.join(dl_folder, filepath.split("gz")[0][:-1])
    except:
        csvpath = os.path.join(dl_folder, filepath.split("zip")[0][:-1])

    if filename in os.listdir(dl_folder):
        print("already downloaded")
        return
    elif csvpath in os.listdir(dl_folder):
        print("csv already downloaded")
    else:
        try:
            urllib.request.urlretrieve(link, filepath)
            print("downloading")
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        except socket.timeout:
            count = 1
            while count <= 5:
                try:
                    urllib.request.urlretrieve(link, filepath)
                    break
                except socket.timeout:
                    err_info = 'Reloading for %d time' % count if count == 1 else 'Reloading for %d times' % count
                    print(err_info)
                    count += 1
            if count > 5:
                print("downloading picture fialed!")
    return


def unzip(zipfile, dl_folder, zcount):
    print(zcount, zipfile)
    zcount += 1
    if not (".gz" in zipfile or ".zip" in zipfile):
        print("Skipped\n")
        return zcount
    else:
        zippath = os.path.join(dl_folder, zipfile)
        try:
            csvpath = os.path.join(dl_folder, zipfile.split("gz")[0][:-1])
        except:
            csvpath = os.path.join(dl_folder, zipfile.split("zip")[0][:-1])
        if csvpath in os.listdir(dl_folder):
            print("csv already exists")
            return zcount

        with gzip.open(zippath, 'rb') as f_in:
            with open(csvpath, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print("Extracted")
        os.remove(zippath)
        print("Zipfile removed\n")
        return zcount


# 数据页面 https://public.bitmex.com/?prefix=data/trade/
def main():
    dl_types = ["quote", "trade"]
    # start_date = datetime(year = 2014, month = 11, day = 22)
    for dl_type in dl_types:
        dl_folder = dl_type
        if dl_folder not in os.listdir():
            os.mkdir(dl_folder)
        base_url = "https://s3-eu-west-1.amazonaws.com/public.bitmex.com/data/" + dl_folder + "/"
        href_links = []
        href_links = save_links(dl_folder, href_links, start_date, base_url)

        count = 1
        pool = multiprocessing.Pool(processes=4)
        count = pool.map(process_url, href_links)
        # pool = multiprocessing.Pool(4)
        # pool.apply_async(process_url, href_links)

        # pool.close()
        # pool.join()
        # print("finished download: " + str(count))
        # print("finished download: ")

        # cl = CreateLogger(process_url)
        # pool = multiprocessing.Pool(processes=4)
        # pool.map(cl.func, href_links)

        # pool = multiprocessing.Pool(processes=4)
        # for i in range len(href_links):
        #     pool.apply_async(process_url, href_links[i])

        # pool.close()
        # pool.join()
        print("finished download: ")

        # zcount = 0
        # for zipfile in os.listdir(dl_folder):
        # zcount = unzip(zipfile, dl_folder, zcount)

        # print("zcount: " + str(zcount))


if __name__ == "__main__":
    main()
