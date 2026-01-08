#!/usr/bin/env python3

# Network Scanner Project
# Author: Utsav Chopda
# Purpose: Discover live hosts in a network using ARP scanning

#!/usr/bin/env python3

import scapy.all as scapy
import argparse
import sys


def get_target():
    parser = argparse.ArgumentParser(description="Simple Network Scanner")
    parser.add_argument(
        "-t", "--target",
        dest="target",
        help="Target IP or IP range (Example: 192.168.1.1/24)"
    )
    args = parser.parse_args()

    if args.target:
        return args.target
    else:
        return input("Enter target IP or IP range: ")


def scan_network(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request

    answered = scapy.srp(packet, timeout=2, verbose=False)[0]

    clients = []
    for sent, received in answered:
        clients.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return clients


def display_result(results):
    print("\nIP Address\t\tMAC Address")
    print("-------------------------------------------")

    if not results:
        print("No devices found.")
        return

    for client in results:
        print(client["ip"] + "\t\t" + client["mac"])


def main():
    try:
        target = get_target()
        results = scan_network(target)
        display_result(results)
    except Exception as e:
        print(f"Error: {e}")

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()

