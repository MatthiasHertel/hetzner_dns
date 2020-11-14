import os
import requests
import json
from ansible.errors import AnsibleError

class HetznerAPIHandler:
    def __init__(self, kwargs):
        self.TOKEN = kwargs.get('api_token') or os.environ.get('HETZNER_DNS_TOKEN')
        if self.TOKEN is None:
            raise AnsibleError('Unable to continue. No Hetzner DNS API Token is given.')

    def get_zone_info(self):
        try:
            r = requests.get(
                url="https://dns.hetzner.com/api/v1/zones",
                headers={
                    "Auth-API-Token": self.TOKEN,
                },
            )

            if r.status_code == 200:
                return r
            else:
                raise AnsibleError('Unknown Error')
        except requests.exceptions.RequestException:
            raise AnsibleError('HTTP Request failed')


