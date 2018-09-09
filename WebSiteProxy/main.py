#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup

from flask import Flask
from flask import render_template

app = Flask(__name__)

base_url = "http://3g.wenxuem.com"
url = "http://3g.wenxuem.com/wapbook/73495_20440850.html"


@app.route('/proxy')
def proxy_open():
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')

    title = soup.find_all("div", {"class": "header"})[0]
    print(title)
    prenext = soup.find_all("div", {"class": "nr_page"})[0]
    print(prenext)
    # content = soup.select('#content')[0]
    content = soup.find_all("div", {"class": "nr_nr"})[0]
    # print(content)
    return render_template("website.html", title=title, content=content, prenext=prenext)


@app.route('/wapbook/<path:chapter_url>')
def chapter_open(chapter_url):
    full_url = "/".join([base_url, "wapbook", chapter_url])
    html = urllib.request.urlopen(full_url).read()
    soup = BeautifulSoup(html, 'lxml')

    title = soup.find_all("div", {"class": "header"})[0]
    # print(title)
    prenext = soup.find_all("div", {"class": "nr_page"})[0]
    # print(prenext)
    content = soup.find_all("div", {"class": "nr_nr"})[0]
    # print(content)
    return render_template("website.html", title=title, content=content, prenext=prenext)


@app.route('/170266/')
def contents_open():
    html = urllib.request.urlopen("https://m.qxs.la/170266/").read()
    soup = BeautifulSoup(html, 'lxml')
    contents = soup.find_all("div", {"class": "n-chapter"})[5]
    # print(contents)
    return render_template("contents.html", contents=contents)


def main():
    app.run(host="0.0.0.0")


if __name__ == '__main__':
    main()
