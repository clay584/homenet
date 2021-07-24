#!/usr/bin/env python3
from config import inventory
from scrapli.driver.core import IOSXEDriver
from scrapli.driver.generic import GenericDriver
import json
import logging


# Scrapli logging
logging.basicConfig(filename="scrapli.log", level=logging.DEBUG)


# IOS-XE Router
rtr = inventory.get("sandbox-iosxe-latest-1.cisco.com")
rtr_conn = IOSXEDriver(**rtr)
rtr_conn.open()
response = rtr_conn.send_command("show version")
print(json.dumps(response.genie_parse_output(), sort_keys=True, indent=4))

# Linux Server
linux_server = inventory.get("viper.operational.io")
linux_conn = GenericDriver(**linux_server)
linux_conn.open()
print(linux_conn.send_command("uname -a").result)
