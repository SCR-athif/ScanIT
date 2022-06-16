import nmap
def cve_scan():
    IP = str(input("Enter the Ip you want to scan for cves:  "))
    nm = nmap.PortScanner()
    result = nm.scan(hosts=IP, arguments='-p 1-1000 -sV -Pn --script vuln')
    for i in result['scan'][IP]['hostscript']:          #This for loop will help to select the vulerabilities list in the
        print(i)                                        #list in the result dictionary print one by one that was identified
                                                      #when the cve scanning was done
cve_scan()
