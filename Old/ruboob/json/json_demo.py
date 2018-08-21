# -*- coding:utf-8 -*-
import json
dumps = json.dumps(['foo',{'bar':('baz',None,1.0,2)}])
print(dumps)

print(json.dumps("\"foo\bar"))
print(json.dumps('\u1234'))
print(json.dumps('\\'))
print(json.dumps({"c":0,"b":0,"a":0}, sort_keys=True))

from io import StringIO
io = StringIO()
json.dump(['streaming Api'], io)
print(io.getvalue())
