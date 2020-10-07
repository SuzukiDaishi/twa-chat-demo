
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

chat_doc = 'これ ➡︎ Sakura has been around since the Warring States period!!'
out = spotSortByDocuments(chat_doc, spotsData)

print(out)