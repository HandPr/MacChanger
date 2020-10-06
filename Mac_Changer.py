#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its Mac Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="Your new Mac Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        # code to handle errors
        parser.error("[-] Please specify an interface, use --help for more information")
    elif not options.new_mac:
        # code to handle errors
        parser.error("[-] Please specify an MAC Address, use --help for more information")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing Mac Addres for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_mac_address(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read Mac Address")


options = get_arguments()
current_mac = get_mac_address(options.interface)
print("[+] Current MAC Address is " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_mac_address(options.interface)
if current_mac == options.new_mac:
    print("[+] Mac Address was successfully changed to " + current_mac)
else:
    print("[-] Mac Address did not change exiting....")

