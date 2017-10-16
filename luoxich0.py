import jieba 
import re 
from collections import Counter 

loadfile = open('/deeplearning1022/happiness_seg.txt', 'r')
text = loadfile.read().decode('utf-8')
loadfile.close()

dict = []
words = jieba.cut(text)
for word in words:
    if re.match(u'([\u4e00-\u9fff]+)', word):
        dict.append(word)

sorted_list = sorted(Counter(dict).items(), key=lambda x:x[1], reverse=True)

for i in sorted_list[:10]:
    print " '%s' : %d " % (i[0], i[1])