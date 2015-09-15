#!/usr/bin/env python
import os, sys, re, logging, json, requests, argparse
from string import Template

from gcis_clients import GcisClient


log_format = "[%(asctime)s: %(levelname)s/%(funcName)s] %(message)s"
logging.basicConfig(format=log_format, level=logging.INFO)

# disable unverified HTTPS warnings
requests.packages.urllib3.disable_warnings()


def update(url):
    """Updated GCIS for this figure."""

    # get authenticated GCIS client
    gcis = GcisClient(url)

    #update figure metadata
    fig_id = "flooding-and-hurricane-irene"
    href = "/report/nca3/chapter/northeast/figure/%s"%fig_id
    update_url = "%s%s"%(url,href)
    data = {
            "identifier":fig_id,
            "report_identifier":"nca3",
            "href": "http://data.globalchange.gov/report/nca3/chapter/northeast/figure/flooding-and-hurricane-irene.json",
            "caption": "Hurricane Irene over the Northeast on August 28, 2011. The storm, which brought catastrophic flooding rains to parts of the Northeast, took 41 lives in the United States, and the economic cost was estimated at $16 billion.<tbib>20978b46-3ff5-4da8-912d-403b28f846fb</tbib> (Figure source: MODIS instrument on NASAâ€™s Aqua satellite).",
            "ordinal":3,
            #"uri": "/report/nca3/chapter/northeast/figure/flooding-and-hurricane-irene",
            "title": "Flooding and Hurricane Irene",
            "usage_limits": "Free to use with credit to the original figure source.",
            "url": "http://nca2014.globalchange.gov/report/regions/northeast/graphics/flooding-and-hurricane-irene",
            "source_citation": "MODIS instrument on NASAâ€™s Aqua satellite",
            "create_dt": "2014-03-04T10:34:00",
            "chapter_identifier": "northeast",
        }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()


    #add Files

    #add parents

    #add images

    #add chapter

    #add references

if __name__ == "__main__":
    desc = "Updated Figure 16.3: Flooding and Hurricane Irene"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('url', help="GCIS url")
    args = parser.parse_args()
    update(args.url)
