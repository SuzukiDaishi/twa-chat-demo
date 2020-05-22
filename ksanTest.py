
""" 
# けーさんがspotsSearchで作った関数をテストする場所 

実行方法は下記のようにする

```
cd <このファイルのあるディレクトリ>
python ksanTest.py
```

"""

from  spotsSearch import *
import json


json_open = open('database/database.json', 'r',encoding='utf-8_sig')
spotsData = json.load(json_open)

print(spotsData)

'''
test_array_A = words_to_sep(spotsData[0]["description"])
test_out_A = words_to_freqdict(test_array_A)
print(test_out_A)

test_array_B = words_to_sep(spotsData[1]["description"])
test_out_B = words_to_freqdict(test_array_B)
print(test_out_B)

test_word = '桜を見たいな～'
word_array = words_to_sep(test_word)
word_out = words_to_freqdict(word_array)
print(word_out)

out_cosA = calc_cos(test_out_A,word_out)
out_cosB = calc_cos(test_out_B,word_out)
print(out_cosA)
print(out_cosB)
'''