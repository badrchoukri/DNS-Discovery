import dns
import dns.resolver
import sys

GREEN = "\033[92m"
RED   = "\033[91m"
RESET = "\033[0m"

try : 
    def DNSRequest(domain , show=False):

        try:
            result = dns.resolver.resolve(domain,'A')
            if result:
                for answer in result:
                    print(f"{GREEN + domain + RESET} : {answer}")
                    

        except dns.resolver.NXDOMAIN:
            if show == True : 
               print(f"{RED + domain + RESET} : domain not exist.")

        except dns.exception.Timeout:
            if show == True:
                print(f"{RED + domain + RESET} : Time out.")
        
    def Subsomainsearch(domain , dictionnary, show ,nums):
        for word in dictionnary:
            subdomain = word+"."+domain
            DNSRequest(subdomain , show )
            if nums:
                for i in range(0,10):
                    s = word + str(i)+"."+domain
                    DNSRequest(s , show)
            

    domain = sys.argv[1]
    d = sys.argv[2]

    show = False
    if "-o" in sys.argv :
        show = True

    if "-h" in sys.argv:
        print("DNS_explorer.py [domain name] [word list] [-o] :")
        print()
        print("[domain name] : the domain name you want to scan .")
        print("[domain name] : the domain name you want to scan .")
        print("[word list] : the list of key words to generate a subdomains .") 
        print("[-o] : to show up the domins not exist .")
        sys.exit()

    dictionnary = []
    with open(d,"r") as f:
        dictionnary = f.read().splitlines()

    Subsomainsearch(domain,dictionnary, show,True)

except KeyboardInterrupt:
    print(RED+ "programme stoped by the user." +RESET)


