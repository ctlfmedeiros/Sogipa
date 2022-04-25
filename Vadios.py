import re
import pandas as pd
import matplotlib.pyplot as plt

file = open(r'./txopen.txt',mode='r',encoding="utf8")
data = file.read()
file.close()
data

pattern = re.compile('\d+:\d+\s+-\s+([a-zA-Z0-9]+\s?[a-zA-Z0-9]+\s?[a-zA-Z0-9]+\s?):\s+')
messengers = re.findall(pattern,data)

count_messages={}
for each in messengers:
    if each in count_messages.keys():
        count_messages[each]+=1
    else:
        count_messages[each]=1

sorted_values = sorted(count_messages.values(), reverse=True) # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in count_messages.keys():
        if count_messages[k] == i:
            sorted_dict[k] = count_messages[k]
            break

print(sorted_dict)