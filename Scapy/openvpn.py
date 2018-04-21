
from scapy.all import Packet, BitEnumField, BitField, ConditionalField, ShortField, TCP,

import struct

class OpenVPN(Packet):
    name = 'OpenVPN'
    fields_desc = [
        BitEnumField('opcode', 1, 5, {
            1: 'P_CONTROL_HARD_RESET_CLIENT_V1',
            2: 'P_CONTROL_HARD_RESET_SERVER_V1',
            3: 'P_CONTROL_SOFT_RESET_V1',
            4: 'P_CONTROL_V1',
            5: 'P_ACK_V1',
            6: 'P_DATA_V1',
            7: 'P_CONTROL_HARD_RESET_CLIENT_V2',
            8: 'P_CONTROL_HARD_RESET_SERVER_V2',
            9: 'P_DATA_V2',
        }),
        BitField('keyid', 0, 3),
        ConditionalField(ShortField("Length", None),
                         lambda pkt: isinstance(pkt.underlayer, TCP))
    ]
    def post_build(self, pkt, pay):
        if isinstance(self.underlayer, TCP) and self.length is None:
            pkt = struct.pack("!H", len(pkt) - 2) + pkt[2:]
        return pkt + pay
