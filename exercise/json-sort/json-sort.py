#!/usr/bin/python
# -*- coding:utf-8 -*-

import json
import difflib
import jsonpatch
from json2html import *
import webbrowser
from jinja2 import Template
from jinja2 import Environment, PackageLoader

with open("a.json", "r") as fs_a:
    src_doc = json.load(fs_a)
    src_lines = json.dumps(src_doc, sort_keys=True, indent=4, separators=(',', ': ')).splitlines()

with open("b.json", "r") as fs_b:
    dst_doc = json.load(fs_b)
    dst_lines = json.dumps(dst_doc, sort_keys=True, indent=4, separators=(',', ': ')).splitlines()


patch_doc = jsonpatch.make_patch(src_doc, dst_doc)
print("json patch: {}".format(patch_doc.patch))

# json_patch = [
#     {'op': 'replace', 'path': '/pear/fourth/0/second', 'value': 'another'},
#     {'op': 'replace', 'path': '/pear/fourth/0/first', 'value': 'value'},
#     {'op': 'remove', 'path': '/pear/fourth/1/second', 'value': ''},
#     {'op': 'remove', 'path': '/pear/fourth/1/first', 'value': ''},
# ]
#
# with open("patch.html", "w") as fp_patch:
#     fp_patch.write(json2html.convert(json_patch))
#     webbrowser.open("patch.html", new=1)

json_patch = [
    {'op': 'show', 'path': 'diff.html', 'value': ''}
]

env = Environment(loader=PackageLoader("json-sort", "templates"))
template = env.get_template("report.html")
html_content = template.render(summary=json_patch)
print("template content: {}".format(html_content))
with open("patch.html", "w") as fp_patch:
    fp_patch.write(html_content)

# webbrowser.open("patch.html", 0, False)


diff = difflib.ndiff(src_lines, dst_lines)
print("ndiff: \n{}".format('\n'.join(diff)))

print("unified_diff")
diff = list(difflib.unified_diff(src_lines, dst_lines, fromfile="a.json", tofile="b.json"))
print(diff)
if diff:
    print("unified_diff: \n{}".format('\n'.join(diff)))
else:
    print("Same")

print("HtmlDiff make_file")
diff = difflib.HtmlDiff(tabsize=8, wrapcolumn=132).make_file(src_lines, dst_lines)
with open("diff.html", "w") as fs_diff:
    fs_diff.write(diff)

