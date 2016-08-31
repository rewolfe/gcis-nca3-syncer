#!/usr/bin/env python

import os, sys, re, logging, json, requests, argparse
# import os, sys, re, logging, json, argparse

from string import Template
from gcis_client import GcisClient
from gcis_clients.domain import Parent

user = "rewolfe@usgcrp.gov"
key = "xxx"

wrong_key = "test"
other_key = "yyy"

url = "https://data.gcis-dev-front.joss.ucar.edu"
# gcis = GcisClient(url, user, other_key)
gcis = GcisClient(url)

print(gcis.test_login())
print(gcis.s.auth)
print(gcis.s)

href = "/report/nca3/chapter/human-health/figure/contributors/wildfire-smoke-has-widespread-health-effects"
update_url = "%s%s" % (url, href)

print("here!")

data = {
    'role': 'convening_lead_author',
    'person_id': 844,
    'organization_identifier': 'columbia-university-mailman-school-public-health',
}
# r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
# r.raise_for_status()

