# DNS-Explorer

DNS Explorer is a simple Python-based subdomain enumeration tool that performs DNS lookups using a wordlist.

Features :

- Resolves subdomains using DNS A record queries

- Detects valid subdomains and prints their IP addresses


Usage
```bash
python DNS_explorer.py google.com subdomains.txt
```
Show non-existing subdomains
```bash
python DNS_explorer.py google.com subdomains.txt -o
```
Help menu
```bash
python DNS_explorer.py -h
```
clone it 
```bash
git clone https://github.com/badrchoukri/DNS-Discovery.git
```
