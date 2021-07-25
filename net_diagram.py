#!/usr/bin/env python3
from diagrams import Diagram
from diagrams.generic.network import Firewall, Router, Subnet, Switch, VPN
from diagrams.onprem.network import Internet
from diagrams import Cluster, Diagram, Edge
from diagrams.openstack.sharedservices import Keystone
from diagrams.custom import Custom
from common import load_network_data


ICONPATH = "resources/enterprise/network"

nd = load_network_data()


with Diagram("Logical Topology", show=False):

    # Cloudy things
    ipv4 = Internet("IPv4 Internet")
    ipv6 = Internet("IPv6 Internet")
    dancing_kame = Keystone("Dancing Kame\nhttps://www.kame.net")
    plane_kame = Keystone("Boring Kame\nhttps://www.kame.net")

    # Nodes
    fw = Custom(
        nd.devices.palo_fw.hostname,
        f"{ICONPATH}/palofw.png",
    )
    rtr = Custom(
        nd.devices.edge.hostname,
        f"{ICONPATH}/ubiquiti.png",
    )
    core_rtr = Custom(nd.devices.core_rtr.hostname, f"{ICONPATH}/sq_router.png")

    # Zones and VRFs
    with Cluster("Core Router VRFs"):
        with Cluster(nd.zones.client_zone.name):
            vrf104 = Custom(nd.vrfs.vrf104.name, f"{ICONPATH}/c_vrf.png")
            vrf105 = Custom(nd.vrfs.vrf105.name, f"{ICONPATH}/c_vrf.png")
            vrf106 = Custom(nd.vrfs.vrf106.name, f"{ICONPATH}/c_vrf.png")

        with Cluster(nd.zones.dmz_zone.name):
            vrf101 = Custom(nd.vrfs.vrf101.name, f"{ICONPATH}/c_vrf.png")
            vrf102 = Custom(nd.vrfs.vrf102.name, f"{ICONPATH}/c_vrf.png")
            vrf103 = Custom(nd.vrfs.vrf103.name, f"{ICONPATH}/c_vrf.png")

        with Cluster(nd.zones.iot_zone.name):
            vrf107 = Custom(nd.vrfs.vrf107.name, f"{ICONPATH}/c_vrf.png")

        with Cluster(nd.zones.guest_zone.name):
            vrf108 = Custom(nd.vrfs.vrf108.name, f"{ICONPATH}/c_vrf.png")

    # Lines
    red_dashed_line = Edge(color="red", style="dashed", label="6in4 Tunnel")
    v6_traffic = Edge(color="red", label="IPv6 Native")
    dot1q = Edge(color="blue", label="802.1q Sub-Interfaces", style="bold")

    # Connections
    [vrf104, vrf105, vrf106] - core_rtr
    vrf107 - core_rtr
    vrf108 - core_rtr
    [vrf101, vrf102, vrf103] - core_rtr
    core_rtr - dot1q - fw - rtr - ipv4 - plane_kame
    rtr - red_dashed_line - ipv6 - v6_traffic - dancing_kame
