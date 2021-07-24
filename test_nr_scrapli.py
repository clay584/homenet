#!/usr/bin/env python3
from config import inventory
from scrapli.driver.core import IOSXEDriver
import json


dev = inventory.get("sandbox-iosxe-latest-1.cisco.com")

conn = IOSXEDriver(**dev)
conn.open()
response = conn.send_command("show version")
# print(response.result)
print(json.dumps(response.genie_parse_output(), sort_keys=True, indent=4))
