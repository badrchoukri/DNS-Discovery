# DNS-Discovery

DNS Explorer is a simple Python-based subdomain enumeration tool that performs DNS lookups using a wordlist.

Features :

- Resolves subdomains using DNS A record queries

- Detects valid subdomains and prints their IP addresses

- Optional display of failed lookups with the -o flag

- Colored output for better readability

- Handles common DNS errors (NXDOMAIN, Timeout)

- Graceful shutdown when interrupted by the user

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
