#!/usr/bin/env python3
from nornir import InitNornir
from nornir_scrapli.tasks import get_prompt, send_command, send_configs
from config import USERNAME, PASSWORD


nr = InitNornir(config_file="nornir_data/config.yml")

# Assign username and password to nornir inventory hosts
for host in nr.inventory.hosts.values():
    host.username = USERNAME
    host.password = PASSWORD

prompt_results = nr.run(task=get_prompt)
command_results = nr.run(task=send_command, command="show version")
config_results = nr.run(
    task=send_configs,
    configs=["interface loopback123", "description nornir_scrapli was here"],
)

print("get_prompt result:")
print(prompt_results["iosxe-1"].result)
print("send_command result:")
print(command_results["iosxe-1"].result)
print("send_configs result:")
print(config_results["iosxe-1"].result)
