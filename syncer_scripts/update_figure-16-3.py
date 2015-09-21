#!/usr/bin/env python
# coding=utf-8
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
            #"href": "http://data.globalchange.gov/report/nca3/chapter/northeast/figure/flooding-and-hurricane-irene.json",
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

    #update image metadata
    img_id = "a40895b4-9e23-4fc6-a476-c4eb9dc1efd1"
    href = "/image/%s"%img_id
    update_url = "%s%s"%(url,href)
    data = {
            "identifier": img_id,
            "create_dt": "2014-03-04T10:34:00",
            "time_end": "2011-08-29T23:59:59",
            "time_start": "2011-08-29T00:00:00",
            "title": "Flooding and Hurricane Irene"
    }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()
    

    #add parents deriving webpage
    web_id = "c57946b1-f413-491f-b75c-1c08f7594f84"
    href = "/webpage/%s"%web_id
    update_url = "%s%s"%(url, href)
    data = {
        "identifier": web_id,
        #"relationship": "prov:wasDerivedFrom",
        "url": href,
        "title": "Hurricane Irene over the U.S. Northeast : Natural Hazards",
        #"publication_type_identifier": "webpage",
    }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()


    #add activity
    act_id = "3fa57f0d-64c4-4b08-8e00-1558bfdb94f8"
    href = "/activity/"
    update_url = "%s%s"%(url,href)
    check_url = "%s%s" % (update_url, act_id)
    if requests.get(check_url, verify=False).status_code == 200:
        update_url = check_url
    data = {
        'identifier': act_id,
        'methodology': "The input granules were mosaicked and subset to extract the desired area to display the region covered by Hurricane Irene. ", 
        'output_artifacts':"MYD021KM.A2011240.1750.006.2012076212937.hdf"
    }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()


#add derivation from activity to image
    href = "/image/prov/%s" %img_id
    update_url = "%s%s" %(url, href)

    fig_id = "flooding-and-hurricane-irene"
    fig_href = "/report/nca3/chapter/northeast/figure/%s"%fig_id
    
    data = {
        'parent_uri': fig_href,
        "parent_rel": 'prov:wasDerivedFrom',
        'activity': act_id,
    }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()


    #add activity2
    act_id = "789cf0c9-ab26-4c0f-a79c-c6bb516d0a8b"
    href = "/activity/"
    update_url = "%s%s"%(url,href)
    check_url = "%s%s" %(update_url, act_id)
    if requests.get(check_url, verify=False).status_code == 200:
        update_url = check_url
    data = {
        "identifier": act_id,
        "methodology": "The input granules were mosaicked and subset to extract the desired area to display the region covered by Hurricane Irene. ",
        "output_artifacts": "The input granules were mosaicked and subset to extract the desired area to display the region covered by Hurricane Irene. "
    }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()

    #add derivation from activity 2i to image
    href = "/image/prov/%s" %img_id
    update_url = "%s%s" %(url, href)

    fig_id = "flooding-and-hurricane-irene"
    fig_href = "/report/nca3/chapter/northeast/figure/%s"%fig_id
    
    
    data = {


        'parent_uri': fig_href,
        "parent_rel": 'prov:wasDerivedFrom',
        'activity': act_id,
    }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()



if __name__ == "__main__":
    desc = "Updated Figure 16.3: Flooding and Hurricane Irene"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('url', help="GCIS url")
    args = parser.parse_args()
    update(args.url)
