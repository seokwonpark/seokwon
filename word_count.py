import sys
f = open('test.txt', 'r', encoding='euc-kr')

a = f.readlines()
next_list = []

for x in a:
    list_x=x.split('\t')
    next_list.append(list_x)

out=[]
for n in next_list:
    out.append(n[-1].strip())

from collections import Counter
wordDict = Counter()

import re
x = re.compile('[가-힣]+')
output = x.findall(str(out))

for sentence in output:
    for word in sentence.split():
        wordDict[word] += 1

for word, freq in wordDict.most_common(10):
    print(word, freq)

