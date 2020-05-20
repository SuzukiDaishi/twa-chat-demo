
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

test_word = '桜が見たいでやんす'
test_out  = spotSortByDocuments(test_word, spotsData)
print(test_out)
