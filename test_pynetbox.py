#!/usr/bin/env python3
import pynetbox
from config import NB_HOST, NB_TOKEN


nb = pynetbox.api(NB_HOST, token=NB_TOKEN)


devices = nb.dcim.devices.all()

for device in devices:
    print(device.name)
