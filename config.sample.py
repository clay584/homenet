# Netbox Info
NB_HOST = "http://localhost:8080"
NB_TOKEN = "some_api_token"


USERNAME = "foo"
PASSWORD = r"bar"

inventory = {
    "sandbox-iosxe-latest-1.cisco.com": {
        "host": "sandbox-iosxe-latest-1.cisco.com",
        "auth_username": USERNAME,
        "auth_password": PASSWORD,
        "auth_strict_key": False,
    },
    "some.linux.server": {
        "host": "some.linux.server",
        "auth_username": "foo1",
        "auth_password": "bar1",
        "auth_strict_key": False,
        "comms_prompt_pattern": r"^.*\]\$",
    },
}
