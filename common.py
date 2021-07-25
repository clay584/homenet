from ruamel.yaml import YAML
from box import Box


def load_network_data():
    data = {}
    with open("net_data/vlans.yml", "r") as f:
        vlans = YAML().load(f)
        data["vlans"] = vlans.get("vlans")
    with open("net_data/networks.yml", "r") as f:
        networks = YAML().load(f)
        data["networks"] = networks.get("networks")
    with open("net_data/SSIDs.yml", "r") as f:
        ssids = YAML().load(f)
        data["ssids"] = ssids.get("ssids")
    with open("net_data/devices.yml", "r") as f:
        devices = YAML().load(f)
        data["devices"] = devices.get("devices")
    with open("net_data/vrfs.yml", "r") as f:
        vrfs = YAML().load(f)
        data["vrfs"] = vrfs.get("vrfs")
    return Box(data)
