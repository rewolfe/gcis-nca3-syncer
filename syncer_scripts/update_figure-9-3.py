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

    # update figure contributor
    href = "/report/nca3/chapter/human-health/figure/contributors/wildfire-smoke-has-widespread-health-effects"
    update_url = "%s%s" % (url, href)
    data = {
        'role': 'convening_lead_author',
        'person_id': 844,
        'organization_identifier': 'columbia-university-mailman-school-public-health', 
    }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()

    # update image contributor
    img_id = "bf0d948c-6081-4101-bce1-b30542a08d00"
    href = "/image/contributors/%s" % img_id
    update_url = "%s%s" % (url, href)
    data = {
        'role': 'convening_lead_author',
        'person_id': 844,
        'organization_identifier': 'columbia-university-mailman-school-public-health', 
    }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()

    # create activity that generated image
    act_id = "bf0d948c-adapt-image-wildfire-smoke-widespread-health-effects-process"
    href = "/activity/"
    update_url = "%s%s" % (url, href)
    check_url = "%s%s" % (update_url, act_id)
    if requests.get(check_url, verify=False).status_code == 200:
        update_url = check_url
    data = {
        'identifier': act_id,
        'methodology': "Added star marker for Baltimore, wildfire labels and smoke labels to Postscript image provided by K. Knowlton",
        'output_artifacts': "health_Quebec_wildfires_12788_v5.png",
    }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()

    # add derivation prov relating to activity
    href = "/image/prov/%s" % img_id
    update_url = "%s%s" % (url, href)
    data = {
        'parent_uri': '/article/10.1021/es035311z',
        'parent_rel': 'prov:wasDerivedFrom',
        'activity': act_id,
        'note': "Image : bf0d948c-6081-4101-bce1-b30542a08d00 was adapted from Figure 3A of the cited article \"Impact of the 2002 Canadian Forest Fires on Particulate Matter Air Quality in Baltimore City\".",
    }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()






#account for activity 1
    act_id = "earth_obsv-image-wildfire-smoke-widespread-health-effects-process"
    href = "/activity/"
    update_url = "%s%s" % (url, href)
    check_url = "%s%s" % (update_url, act_id)
    if requests.get(check_url, verify=False).status_code == 200:
        update_url = check_url
    data = {
            'identifier': act_id,
            'methodology': "xxx copied the input image and placed a star to mark Baltimore, MD and highlighted fire locations in Quebec.",
            'output_artifacts': "http://earthobservatory.nasa.gov/NaturalHazards/view.php?id=9826",
    }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()

    # add derivation prov relating to activity
    #href = "/image/prov/%s" % img_id
    #update_url = "%s%s" % (url, href)
    #data = {
    #        'parent_uri': '',
    #        'parent_rel': 'prov:wasDerivedFrom',
    #        'activity': act_id,
    #        'note': "Image : bf0d948c-6081-4101-bce1-b30542a08d00 was created by activity %s"%act_id,
    #        }
    #r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    #r.raise_for_status()



    
    
    #account for activity_2 
    act_id = "earth_obsv_2-image-wildfire-smoke-widespread-health-effects-process"
    href = "/activity/"
    update_url = "%s%s" % (url, href)
    check_url = "%s%s" % (update_url, act_id)
    if requests.get(check_url, verify=False).status_code == 200:
        update_url = check_url
    data = {
            'identifier': act_id,
            'methodology':"The two input images were subsetted and merged to generate the output.",
#            'input_artifacts': "",
            'output_artifacts': "Image fires-in-quebec-canada",#"http://earthobservatory.nasa.gov/NaturalHazards/view.php?id=9826",
            'notes':"Two images from NASAâ€™s MODIS Rapid Response System http://lance-modis.eosdis.nasa.gov/cgi-bin/imagery/single.cgi?image=Canada.A2002188.1635.2km.jpg and http://lance-modis.eosdis.nasa.gov/cgi-bin/imagery/single.cgi?image=EastCoast.A2002188.1635.1km.jpg",
    }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()


    # add derivation prov relating to activity
#    href = "/image/prov/%s" % img_id
#    update_url = "%s%s" % (url, href)
#    data = {
            #seems like it should be  http://lance-modis.eosdis.nasa.gov/cgi-bin/imagery/single.cgi?image=EastCoast.A2002188.1635.1km.jpg that is linked as parent
#            'parent_uri': " http://lance-modis.eosdis.nasa.gov/cgi-bin/imagery/single.cgi?image=EastCoast.A2002188.1635.1km.jpg",#v"/image/%s"%img_id,
#            'parent_rel': 'prov:wasDerivedFrom',
#            'activity': act_id,
#            'note': "Image : bf0d948c-6081-4101-bce1-b30542a08d00 was created by activity %s"%act_id,
#            }
#    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
#    r.raise_for_status()



    #account for activity_3 
    act_id = "earth_obsv_3-image-wildfire-smoke-widespread-health-effects-process"
    href = "/activity/"
    update_url = "%s%s" % (url, href)
    check_url = "%s%s" % (update_url, act_id)
    if requests.get(check_url, verify=False).status_code == 200:
        update_url = check_url
    data = {
            'identifier': act_id,
            'methodology': "The two input images are processed to corrected reflectance images by a process described in the document https://earthdata.nasa.gov/files/MODIS_True_Color.pdf. Also, to generate the two images on the Rapid Response System, the two corresponding granules of the MODIS fire product are overlaid. When the images were generated in 2002, a system at University of Maryland was being used for the MODIS fire products. That system used an algorithm identical to the one used for the MODIS product MOD14 (Thermal Anomalies - Fires and Biomass Burning) which is currently available from Land Processes (LP) DAAC. The two granules can be obtained from LP DAAC using the links: http://e4ftl01.cr.usgs.gov//MODIS_Dailies_C/MOLT/MOD14.005/2002.07.07/MOD14.A2002188.1630.005.2011273181127.hdf and http://e4ftl01.cr.usgs.gov//MODIS_Dailies_C/MOLT/MOD14.005/2002.07.07/MOD14.A2002188.1635.005.2011273181055.hdf.It is to be noted that there may be very slight differences in the geolocation of the fires between these granules and the ones on the Rapid Response System due to the use of predictive ephemeris in the latter vs definitive ephemeris in the former. (Use of predictive ephemeris is standard practice for near real-time products because of the latency constraints.)Details about the MODIS fire products can be found in https://earthdata.nasa.gov/files/MODIS_Fire_Users_Guide_2.5.pdf. The Algorithm Theoretical Basis Document for MOD14 is at http://modis.gsfc.nasa.gov/data/atbd/atbd_mod14.pdf.",
            'output_artifacts': "Two images in NASA's MODIS Rapid Response System http://lance-modis.eosdis.nasa.gov/cgi-bin/imagery/single.cgi?image=Canada.A2002188.1635.2km.jpg and http://lance-modis.eosdis.nasa.gov/cgi-bin/imagery/single.cgi?image=EastCoast.A2002188.1635.1km.jpg",
    }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()

# add derivation prov relating to activity
#    href = "/image/prov/%s" % img_id
#    update_url = "%s%s" % (url, href)
#    data = {
#            'parent_uri': "http://lance-modis.eosdis.nasa.gov/cgi-bin/imagery/single.cgi?image=Canada.A2002188.1635.2km.jpg",#"/image/%s"%img_id,
#            'parent_rel': 'prov:wasDerivedFrom',
#            'activity': act_id,
#            'note': "Image : bf0d948c-6081-4101-bce1-b30542a08d00 was created by activity %s"%act_id,
#            }
#    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
#    r.raise_for_status()


# add derivation prov relating to activity
#    href = "/image/prov/%s" % img_id
#    update_url = "%s%s" % (url, href)
#    data = {
#            'parent_uri': "http://lance-modis.eosdis.nasa.gov/cgi-bin/imagery/single.cgi?image=EastCoast.A2002188.1635.1km.jpg",#"/image/%s"%img_id,
#            'parent_rel': 'prov:wasDerivedFrom',
#            'activity': act_id,
#            'note': "Image : bf0d948c-6081-4101-bce1-b30542a08d00 was created by activity %s"%act_id,
#            }
#    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
#    r.raise_for_status()

#new items: 2 datasets, 1 image
    #add dataset
    dataset_id = "nasa-modis-rapid-response-system"
    href = "/dataset/"
    update_url = "%s%s"%(url,href)
    check_url = "%s%s"%(update_url, dataset_id)
    if requests.get(check_url, verify=False).status_code == 200:
        update_url = check_url
    data = {
            'identifier': dataset_id,
            'description': "NASA MODIS Rapid Response System",

    }

    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()

    href = "/dataset/prov/%s"%dataset_id
    update_url = "%s%s"%(url,href)
    data = {
            #publication_type_identifier: "dataset",
            'note': "",
            'url': "/dataset/nasa-laads-mod021km-collection6",
            'relationship': "prov:wasDerivedFrom",
            'label': "dataset nasa-laads-mod021km-collection6",
            'activity_uri': "/activity/earth_obsv_3-image-wildfire-smoke-widespread-health-effects-process"
    }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()




        #add dataset
    dataset_id = "nasa-laads-mod021km-collection6"
    href = "/dataset/"
    update_url = "%s%s"%(url,href)
    check_url = "%s%s"%(update_url, dataset_id)
    if requests.get(check_url, verify=False).status_code ==200:
        update_url = check_url
    data = { 
            'identifier': dataset_id,
            'lat_max': "90",
            'start_time': "2002-07-04T00:00:00",
            'native_id': "MOD021KM",
            'lon_max': "180",
            'name': "MODIS/AQUA Calibrated Radiances L1B Swath 1km (Collection 006)",
            'lon_min': "-180",
            'lat_min': "-90",
            'description': "MODIS image data at 1km (Nadir) resolution, calibrated from raw counts into physically meaningful radiances and reflectances. Corrections for known instrument effects are applied, include cross-talk between different bands. Data for the 500m and 250m bands are aggregated up to 1km resolution. Also includes quality flags, error estimates, and a 5km X 5km sub-sample of all geolocation data from the MYD03 files. ",
            }   

    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()
    
    href = "/dataset/prov/%s"%dataset_id
    update_url = "%s%s"%(url, href)
    data = {
            'label': "dataset nasa-laads-mod021km-collection6",
            'relationship': "prov:wasDerivedFrom",
            'activity_uri': "/activity/earth_obsv_3-image-wildfire-smoke-widespread-health-effects-process",
            'url': "/dataset/nasa-laads-mod021km-collection6",
            'note': "",
            #'publication_type_identifier': "dataset"
            }

    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()



    #add image
    image_id = "b18ef51d-fires-in-quebec-canada"
    href = "/image/"
    update_url = "%s%s"%(url, href)
    check_url = "%s%s"%(update_url, image_id)
    if requests.get(check_url, verify=False).status_code == 200:
        update_url = check_url
    data = {
            'identifier': "b18ef51d-fires-in-quebec-canada",
            'title': "Fires in Quebec, Canada, Send Smoke to U.S.",
            'url': "http://earthobservatory.nasa.gov/NaturalHazards/view.php?id=9826",
            }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()

    href = "/image/prov/%s" % image_id
    update_url = "%s%s" % (url, href)
    data = {
            'parent_uri':"/dataset/nasa-modis-rapid-response-system",
            'note': "",
            #'publication_type_identifier': "dataset",
            'activity_uri': "/activity/earth_obsv_2-image-wildfire-smoke-widespread-health-effects-process",
            'label': "dataset nasa-modis-rapid-response-system",
            'relationship': "prov:wasDerivedFrom",
            }
if __name__ == "__main__":
    desc = "Updated Figure 9.3: Wildfire Smoke has Widespread Health Effects"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('url', help="GCIS url")
    args = parser.parse_args()
    update(args.url)
