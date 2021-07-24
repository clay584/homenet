#!/usr/bin/env python3
from diagrams import Diagram
from diagrams.generic.network import Firewall, Router, Subnet, Switch, VPN
from diagrams.onprem.network import Internet
from diagrams import Cluster, Diagram, Edge


with Diagram("Logical Topology", show=False):

    # with Cluster("Internet"):
    #     ipv4 = Internet("IPv4")
    #     ipv6 = Internet("IPv6")
    ipv4 = Internet("IPv4")
    ipv6 = Internet("IPv6")
    fw = Firewall("palo-fw")
    rtr = Router("edgerouter-x")
    ont = Switch("FiOS ONT")

    # lines
    red_dashed_line = Edge(color="red", style="dashed", label="6in4 Tunnel")

    # Make the connections
    fw - rtr - ont - ipv4
    ont - red_dashed_line - ipv6
