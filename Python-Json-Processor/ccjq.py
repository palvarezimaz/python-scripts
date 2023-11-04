#!/usr/bin/env python3
import io
import json

import sys
import re

print("Hello there!")

curl_response = sys.stdin.read()
json_object = json.loads(curl_response);
print(f"{str(sys.argv)}")

array_pattern = re.compile(r'\[(\d+)\]')

#All
if len(sys.argv) < 2 or sys.argv[1] == ".":
    split_response = json.dumps(json_object, indent=4);
    print(split_response)
    print('...done!')
#Array element
elif array_pattern.match(sys.argv[1]):
    strip = int(re.search(array_pattern, sys.argv[1]).group(1))
    print(strip)
    print('we are asking for an array here')
    try:
        result = json.dumps(json_object[strip], indent=4)
        print(result)
    except:
        print('null')
        print('...done!')
# KV pairs
else:
    try:
        result = json.dumps(json_object[sys.argv[1]], indent=4)
        print(result)
    except:
        print('null')
    finally:
        print('...done!')



