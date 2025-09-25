# usage
- preprequisites
```
pip install -r requirements.txt
```
- Example hostnames.txt contains:
```
google.com
openai.com
github.com
```
## Default system DNS, A records
```
python dns_lookup.py -f hostnames.txt
```

## Use Cloudflare DNS, MX records
```
python dns_lookup.py -f hostnames.txt -t MX -s 1.1.1.1
```

## Use Google DNS, CNAME records
```
python dns_lookup.py -f hostnames.txt -t CNAME -s 8.8.8.8
```