# Rename file to config.py
USERNAME = "foo"
PASSWORD = r"bar"

inventory = {
    "sandbox-iosxe-latest-1.cisco.com": {
        "host": "sandbox-iosxe-latest-1.cisco.com",
        "auth_username": USERNAME,
        "auth_password": PASSWORD,
        "auth_strict_key": False,
    }
}
