
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

chat_doc = '桜は戦国時代からあった'
out = spotSortByDocuments(chat_doc, spotsData)

print(out)