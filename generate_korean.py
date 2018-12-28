import re

def isEnglish(chr):
    if not re.search(r'[a-zA-Z]+', chr):
        return False
    else:
        return True


lines = ""
file = open("littleprince.txt", "r", encoding="utf-8")
for line in file:
    lines += line
file.close()
lines = lines.replace(" ", "").replace("\n", "")

from collections import Counter

counter = Counter(list(lines))
counter_adj = counter.copy()

for k, v in counter.items():
    if k.isdigit():
        counter_adj.pop(k)
    elif not k.isalnum():
        counter_adj.pop(k)
    elif isEnglish(k):
        counter_adj.pop(k)

print(len(counter_adj))
print(counter_adj)
#
# chr_list = list(lines)
#
# chr_set = set(chr_list)
#
# remove_digits = [x for x in chr_set if not x.isdigit()]
# remove_specials = [x for x in remove_digits if x.isalnum()]
# remove_eng = [x for x in remove_specials if not isEnglish(x)]
#
# # return remove_eng