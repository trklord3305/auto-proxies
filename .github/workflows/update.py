import urllib.request

sources = [
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/https.txt',
    'https://api.proxyscrape.com/v4/free-proxy-list/get?proxy_format=text&format=text'
]

proxies = set()
for src in sources:
    try:
        req = urllib.request.Request(src, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            lines = response.read().decode('utf-8').splitlines()
            for line in lines:
                cleaned = line.strip()
                if cleaned and ':' in cleaned:
                    proxies.add(cleaned)
    except Exception as e:
        print(f'Error fetching: {e}')

with open('active_proxies.txt', 'w') as f:
    for p in list(proxies):
        f.write(f'{p}\n')

print(f'Total saved: {len(proxies)}')
