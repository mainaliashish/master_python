from pprint import pprint

sentence = "This is the most common interview question."
sentence = sentence.replace(" ", "")

results = {}

for letter in sentence:
    if letter in results:
        results[letter] += 1
    else:
        results[letter] = 1

pprint(results, width=1)

res_tuples = sorted(results.items(), key=lambda kv:kv[1], reverse=True)
print(res_tuples)

import pandas as pd

print(pd.Series(list(sentence)).value_counts())

def check_freq(x):
    freq = {}
    x = x.replace(" ", "")
    for c in set(x):
       freq[c] = x.count(c)
    return freq

x = check_freq("This is the most common interview question.")
print(x)
