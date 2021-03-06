# hetzner dns ansible collection

Manage DNS records using ansible. E.g. [set DNS records while creating servers in the same play](https://git.osuv.de/m/hetzner_dns/wiki/Home).

* https://galaxy.ansible.com/markuman/hetzner_dns
* `ansible-galaxy collection install markuman.hetzner_dns`

## Auth

The API token can be set via ansible parameter or ENV variable.

| **Ansible Parameter** | **ENV Variable** |
| --- | --- |
| `api_token` | `HETZNER_DNS_TOKEN` |


## record

When `state: absent` (_deleting_) a record, than `name` and `type` are sufficient (_`value` and `ttl` doesn't matter_).  
When `state: present`, the `ttl` default value  is set to `300`.  
Either `zone_id` or `zone_name`  must be given, but not both.  
`record` module supports `check_mode`.

| parameters | default | comment |
| --- | --- | --- |
| `name` | - | name of a record |
| `value` | - | required with `state: present` |
| `type` | - | type of record. valid records: "A" "AAAA" "NS" "MX" "CNAME" "RP" "TXT" "SOA" "HINFO" "SRV" "DANE" "TLSA" "DS" "CAA" |
| `ttl` | `300` | TTL of a record |
| `zone_id` | - | Required one of `zone_name` or `zone_id` |
| `zone_name` | - | Required one of `zone_name` or `zone_id` |
| `api_token` | - | Can be also set as env variable `HETZNER_DNS_TOKEN` |


```yml
- name: add record
  markuman.hetzner_dns.record:
    zone_name: osuv.de
    name: hetzner_dns_ansible_collection
    value: osuv.de.
    type: CNAME
    ttl: 300
  register: RECORD

- name: add record no change
  markuman.hetzner_dns.record:
    zone_name: osuv.de
    name: hetzner_dns_ansible_collection
    value: osuv.de.
    type: CNAME
    ttl: 300
  register: RECORD

- name: add record change
  markuman.hetzner_dns.record:
    zone_name: osuv.de
    name: hetzner_dns_ansible_collection
    value: osuv.de.
    type: CNAME
    ttl: 60
  register: RECORD

- name: del record
  markuman.hetzner_dns.record:
    zone_name: osuv.de
    name: hetzner_dns_ansible_collection
    type: CNAME
    state: absent
  register: RECORD
```

#### mx priority

When dialing with sevaral mx records, the priority must be part of the value.

```yml
- name: take care about mx record
  markuman.hetzner_dns.record:
    api_token: "{{ API }}"
    zone_name: osuv.de
    name: "@"
    value: 10 mail.osuv.de.
    type: MX
    ttl: 300
  register: RECORD
```

## record_info

When no filter is given, all records will be returned.  
Either `zone_id` or `zone_name`  must be given, but not both.  
Parameter `filter` must be a list, where each object supports the same keys as in `record`  module for search.

| parameter | default | comments |
| --- | --- | --- |
| `filter` | - | Apply a list of key/value pairs to search for |
| `zone_id` | - | Required one of `zone_name` or `zone_id` |
| `zone_name` | - | Required one of `zone_name` or `zone_id` |
| `api_token` | - | Can be also set as env variable `HETZNER_DNS_TOKEN` |


```yml
- name: fetch zone info
  markuman.hetzner_dns.record_info:
    filter:
      - name: fritzbox
        value: 192.168.178.1
        type: A
      - name: fritzbox
        type: AAAA
    zone_name: osuv.de
```

## zone_info

To determine the `zone_id`.

```yml
- name: fetch zone info
  markuman.hetzner_dns.zone_info:
    name: zone_name
```

### SCM

| **host** | **category** |
| --- | --- |
| [git.osuv.de/m/hetzner_dns](https://git.osuv.de/m/hetzner_dns) | origin |
| [gitlab.com/markuman/hetzner_dns](https://gitlab.com/markuman/hetzner_dns) | pull mirror |
| [gitub.com/markuman/hetzner_dns](https://github.com/markuman/hetzner_dns) | push mirror |