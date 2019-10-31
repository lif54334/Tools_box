import json
import re

import simplejson

with open("paper_title.txt", "r", encoding="utf8")as f_title:
    titles = f_title.readlines()

with open("paper.txt", "a", encoding="utf8")as f_paper:
    with open("xueshu.txt", "r", encoding="utf8")as f_xueshu:
        xueshu = f_xueshu.readlines()
        for i in titles:
            for j in xueshu:
                n=str(j)
                m= re.sub('\'', '\"', n)
                m = re.sub('\n', '\\n', m)
                p = simplejson.loads(m)
                if str(i).strip() == str(p["title"]).strip():
                    print("yes")
                    f_paper.write(m)
                else:
                    pass
