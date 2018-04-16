#!/usr/bin/env python3

from scapy.all import *

conf.verb = 0

def openvpn_udp_scan(host, port):
    print('[+] Scanning port %d... ' % port, end='')
    msg = '\x38\x78\xdd\x5d\x8a\xa7\xd1\xc9\x38\x00\x00\x00\x00\x00'
    pkt = IP(dst=host)/UDP(sport=45290, dport=port)/Raw(load=msg)

    answer = sr1(pkt, timeout=2)
    if answer is None:
        print('KO')
    elif 'ICMP' in answer:
        print('IMPKO')
    else:
        print('OK')

if __name__ == '__main__':
    openvpn_udp_scan('open.fdn.fr', 1194)
    openvpn_udp_scan('open.fdn.fr', 1195)
    openvpn_udp_scan('open.fdn.fr', 443)
    openvpn_udp_scan('open.fdn.fr', 53)
    openvpn_udp_scan('open.fdn.fr', 123)