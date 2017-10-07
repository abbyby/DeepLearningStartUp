import re
from collections import Counter

word_lst = []
double_lst = []

with open("/Users/luoxi/DeepLearningStartUp/happiness_seg.txt","r", encoding='utf-8') as f:
    newf = re.sub("，－《》（）！。？、：“”", " ", f.read())
    words = newf.strip().split(" ")
    for word in words:
        word_lst.append(word)

for i in range(len(word_lst)):
    if len(word_lst[i]) > 1 and len(word_lst[i+1]) > 1:
        double_word = word_lst[i] + " " + word_lst[i+1]
        double_lst.append(double_word)

c = Counter(double_lst).most_common(10)
for top_word in c:
    print(top_word[0], ":", top_word[1])
    
