from scapy.all import sr1, IP, TCP, conf

conf.verb = 0 #quiet mode

SYN = 0x02
ACK = 0x10
SYNACK = SYN | ACK

def tcp_scan(host, port):
    syn_pkt = IP(dst=host)/TCP(dport=port, flags='S') # 'S' for SYN
    synack_pkt = sr1(syn_pkt, timeout=1)
    syn_pkt.show()
    if synack_pkt is None:
        print('Cannot reach host "%s" on port %d' % (host, port))
    elif synack_pkt['TCP'].flags == SYNACK:
        print("%5d OPEN" % port)
    else:
        print("%5d CLOSED" % port)