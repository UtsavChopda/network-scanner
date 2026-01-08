#!/usr/bin/env python3

# Network Scanner Project
# Author: Utsav Chopda
# Purpose: Discover live hosts in a network using ARP scanning

import scapy.all as scapy
import argparse


def get_arguments():
    """
    Handles command-line arguments
    """
    parser = argparse.ArgumentParser(description="Simple Network Scanner")
    parser.add_argument(
        "-t", "--target",
        dest="target",
        help="Target IP address or IP range (Example: 192.168.1.1/24)"
    )
    options = parser.parse_args()

    if not options.target:
        parser.error("[-] Please specify a target IP or IP range. Use --help for more info.")

    return options


def scan_network(ip):
    """
    Sends ARP requests to the target network
    """
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request

    answered_list = scapy.srp(
        arp_request_broadcast,
        timeout=1,
        verbose=False
    )[0]

    clients = []

    for element in answered_list:
        client_info = {
            "ip": element[1].psrc,
            "mac": element[1].hwsrc
        }
        clients.append(client_info)

    return clients


def display_result(results):
    """
    Displays scan result in a clean table format
    """
    print("\nIP Address\t\tMAC Address")
    print("-------------------------------------------")

    for client in results:
        print(client["ip"] + "\t\t" + client["mac"])


def main():
    options = get_arguments()
    result = scan_network(options.target)
    display_result(result)


if __name__ == "__main__":
    main()
