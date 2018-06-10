#!/usr/bin/python
# -*- coding:utf-8 -*-

import json
import difflib

with open("a.json", "r") as fs_a:
    src_doc = json.load(fs_a)
    src_lines = json.dumps(src_doc, sort_keys=True, indent=4, separators=(',', ': ')).splitlines()

with open("b.json", "r") as fs_b:
    dst_doc = json.load(fs_b)
    dst_lines = json.dumps(dst_doc, sort_keys=True, indent=4, separators=(',', ': ')).splitlines()


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
