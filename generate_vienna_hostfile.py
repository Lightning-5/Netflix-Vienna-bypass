import dns.resolver


file = open("Vienna_hostfile.txt", "w+")

#ipv4-c008-vie001-ix.1.oca.nflxvideo.net
zacetek="ipv4-c"
konec="-vie001-ix.1.oca.nflxvideo.net"

file.write("""#Vstavi me v "C:\Windows\System32\drivers\etc\hosts"\n""")
file.write("""#Linux: "/etc/hosts"\n""")
file.write("""#Mac OS X: "/private/etc/hosts"\n\n\n""")
file.write("#IPv4 records\n")
i=1

a_fra = "45.57.74.130"
aaaa_fra = "2a00:86c0:2074:2074::130"

while True:
    domena=zacetek + str(i).zfill(3) + konec
    #print(domena)

    try:
         a_record = dns.resolver.resolve(domena, 'A')
         
    except:
        break
    for ipval in a_record:
        #print(' IP:', ipval.to_text())
        #file.write(ipval.to_text() + "\t" + domena + "\n")
        file.write(a_fra + "\t" + domena + "\n")

    #prištej iterator
    i=i+1
#done

file.write("#Konec IPv4 records\n\n")
file.write("#IPv6 records\n")

zacetek="ipv6-c"
#konec="-vie001-ix.1.oca.nflxvideo.net"

i=1
while True:
    domena=zacetek + str(i).zfill(3) + konec
    #print(domena)

    try:
         aaaa_record = dns.resolver.resolve(domena, 'AAAA')
         
    except:
        break
    for ipval in aaaa_record:
        #print(' IP:', ipval.to_text())
        #file.write(ipval.to_text() + "\t" + domena + "\n")
        file.write(aaaa_fra + "\t" + domena + "\n")

    #prištej iterator
    i=i+1
#done

file.write("#Konec IPv6 records\n\n")

file.close()

