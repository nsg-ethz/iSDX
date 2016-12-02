#!/usr/bin/env python
#  Author:
#  Rudiger Birkner (Networked Systems Group ETH Zurich)

import os
import sys
np = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if np not in sys.path:
    sys.path.append(np)
import pctrl.ss_lib as ss_lib


class FakeSS(object):
    def __init__(self, config):
        self.best_path_size =   int(config["Next Hop Bits"])
        self.VMAC_size =        int(config["VMAC Size"])
        self.port_size =        int(config["Port Bits"])
        self.iSDX_VMAC_size = 24
        self.iSDX_best_path_size = 8

        self.max_bits = self.VMAC_size - self.best_path_size - 1
        self.max_initial_bits = self.max_bits - 4


class VMACBuilder(object):
    def __init__(self, config):
        self.ss_instance = FakeSS(config)

    # constructs a match VMAC for checking next-hop
    def next_hop_match(self, participant_name, inbound_bit = False):
        return ss_lib.vmac_next_hop_match_iSDXmac(participant_name, self.ss_instance, inbound_bit)

    # returns a mask on just participant bits
    def next_hop_mask(self, inbound_bit = False):
        return ss_lib.vmac_next_hop_mask_iSDXmac(self.ss_instance, inbound_bit)

    # constructs stage-2 VMACs (for both matching and assignment)
    def part_port_match(self, participant_name, port_num, inbound_bit = False):
        return ss_lib.vmac_part_port_match(participant_name, port_num,
                                        self.ss_instance, inbound_bit)

    # returns a mask on participant and port bits
    def part_port_mask(self, inbound_bit = False):
        return ss_lib.vmac_part_port_mask(self.ss_instance, inbound_bit)

    # looks like 100000000000000
    def only_first_bit(self):
        return ss_lib.vmac_only_first_bit(self.ss_instance)
