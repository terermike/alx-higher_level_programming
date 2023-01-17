#!/usr/bin/python3
import sys
from urllib.request import urlopen

def fetch_url(url):
    with urlopen(url) as response:
        headers = response.headers
        request_id = headers.get('X-Request-Id')
        print(request_id)

if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
