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

    #this figure - don't change it
    fig_id = "flooding-and-hurricane-irene"

    #update image metadata
    img_id = "a40895b4-9e23-4fc6-a476-c4eb9dc1efd1"
    update_url = "%s/image/%s" %(url,img_id)
    data = {
            "identifier": img_id,
            "create_dt": "2014-03-04T10:34:00",
            "time_end": "2011-08-29T23:59:59",
            "time_start": "2011-08-29T00:00:00",
            "title": "Flooding and Hurricane Irene",
    }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()
    

    #add parent/deriving webpage
    web_id = "c57946b1-f413-491f-b75c-1c08f7594f84"
    web_href = "/webpage/%s" %web_id
    update_url = "%s%s" %(url,web_href)
    data = {
        "identifier": web_id,
        "url": "http://eoimages.gsfc.nasa.gov/images/imagerecords/51000/51957/irene_amo_2011240_lrg.jpg", 
        "title": "Hurricane Irene over the U.S. Northeast : Natural Hazards",
    }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()


    #add derivation from webpage to image
    update_url = "%s/image/prov/%s" %(url,img_id)
    data = {
        "parent_uri": web_href,
        "parent_rel": 'prov:wasDerivedFrom',
    }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()
    
    #add dataset
    dataset_id = "nasa-laads-myd021km_v6"
    update_url = "%s/dataset/" %url
    check_url = "%s%s" %(update_url, dataset_id)
    if requests.get(check_url, verify=False).status_code ==200:
        update_url = check_url
    data = {
        'identifier': dataset_id,
        'lat_max': "90",
        'start_time': "2002-07-04T00:00:00",
        'native_id': "MYD021KM",
        'lon_max': "180",
        'name': "MODIS/AQUA Calibrated Radiances L1B Swath 1km (Collection 006)",
        'lon_min': "-180",
        'lat_min': "-90",
        'description': "MODIS Aqua image data at 1km (Nadir) resolution, calibrated from raw counts into physically meaningful radiances and reflectances. Corrections for known instrument effects are applied, include cross-talk between different bands. Data for the 500m and 250m bands are aggregated up to 1km resolution. Also includes quality flags, error estimates, and a 5km X 5km sub-sample of all geolocation data from the MYD03 files.",
    }

    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()

    #link to insturment/platform

    update_url = "%s/dataset/rel/%s" %(url,dataset_id);
    data = {
        'add_instrument_measurement': {
            'platform_identifier': "aqua",
            'instrument_identifier': "moderate-resolution-imaging-spectroradiometer"
        }
    }

    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()

    #add dataset contributors
    update_url = "%s/dataset/contributors/%s" %(url,dataset_id)
    ds_conts = [
        {
            'role':"data_archive",
            'organization_identifier':'/organization/level1-atmosphere-archive-distribution-system',
        }
    ]
    for data in ds_conts:
        r = gcis.s.post(update_url, data=json.dumps(data),verify=False)
        r.raise_for_status()

    #add activity
    act_id = "a40895b4-create-image-flooding_hurricane_irene-process"
    update_url = "%s/activity/" %url
    check_url = "%s%s" %(update_url, act_id)
    if requests.get(check_url, verify=False).status_code ==200:
        update_url = check_url
    data = {
        'identifier': act_id,
        'notes': "There is no image on earthobservatory or MODIS Rapid Response System that matched the image in the figure. The image might have existed in the MODIS Rapid Response System in 2011, but is part of the data that was lost due to a disk crash in 2013. It has not been restored, and may be restored when MODIS Collection 6 processing is completed.",
        'methodology': "Two MODIS Aqua dataset MYD021KM input granules were mosaicked and subset to extract the desired area to display the region covered by Hurricane Irene. The following two inputs were used.\n\n1. MODIS Aqua dataset MYD021KM granule MYD021KM.A2011240.1750.006.2012076212937.hdf (August 28, 2011, 17:50 UTC)\nftp://ladsftp.nascom.nasa.gov/allData/6/MYD021KM/2011/240/MYD021KM.A2011240.1750.006.2012076212937.hdf\n\n2. MODIS Aqua dataset MYD021KM granule MYD021KM.A2011240.1755.006.2012076211459.hdf  (August 28, 2011, 17:55 UTC)\nftp://ladsftp.nascom.nasa.gov/allData/6/MYD021KM/2011/240/MYD021KM.A2011240.1755.006.2012076211459.hdf\n\nThe landing page for MODIS Aqua dataset MYD021KM: http://gcmd.gsfc.nasa.gov/KeywordSearch/Metadata.do?Portal=lance&EntryId=MYD021KM&MetadataView=Full",
        'output_artifacts':"/report/nca3/chapter/northeast/figure/flooding-and-hurricane-irene"
    }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()

    #add derivation from activity to image
    dataset_href = "/dataset/%s" %dataset_id
    act_href = "/activity/%s" %act_id
    update_url = "%s/image/prov/%s" %(url,img_id)
    data = {
        'parent_uri': dataset_href,
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
