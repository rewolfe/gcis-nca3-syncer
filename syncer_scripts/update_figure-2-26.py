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


#insert 4 datasets:
    #dataset: Proxy Records
    dataset_id = "nca3-proxy-data-r1"
    href = "/dataset/"
    update_url = "%s%s"%(url,href)
    check_url = "%s%s"%(update_url, dataset_id)
    if requests.get(check_url, verify=False).status_code == 200:
        update_url = check_url
    data = {
        'identifier': dataset_id,
        'cite_metadata': "Kemp, A. C., B. P. Horton, J. P. Donnelly, M. E. Mann, M. Vermeer, and S. Rahmstorf, 2012: Climate related sea-level variations over the past two millennia. Proceedings of the National Academy of Sciences of the United States of America, 108, 11017-11022, doi:10.1073/pnas.1015619108. [Available online at http://www.pnas.org/content/108/27/11017.full.pdf+html]",
        'spatial_extent': "maximum_latitude: ; minimum_latitude: ; maximum_longitude: ; minimum_longitude: ;",
        'name': "Proxy Data",
        'temporal_extent': "2014-04-29T00:00:00 2014-04-29T00:00:00",
    }

    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()
    
    #dataset: Tide Gauge Data
    dataset_id = "nca3-tide-gauge-data-r1"
    href = "/dataset/"
    update_url = "%s%s"%(url,href)
    check_url = "%s%s"%(update_url, dataset_id)
    if requests.get(check_url, verify=False).status_code == 200:
        update_url = check_url
    data = {
            'identifier': dataset_id,
            cite_metadata: "Church, J. A., and N. J. White, 2011: Sea-level rise from the late 19th to the early 21st century. Surveys in Geophysics, 32, 585-602, doi:10.1007/s10712-011-9119-1",
            temporal_extent: "2014-04-29T00:00:00 2014-04-29T00:00:00",
            name: "Tide Gauge Data",
            spatial_extent: "maximum_latitude: ; minimum_latitude: ; maximum_longitude: ; minimum_longitude: ;"
            }

    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()

    #dataset: 2012_rel3: Global Mean Sea Level Time Series
    dataset_id = "global-mean-sea-level-time-series_2012_rel3"
    href = "/dataset/"
    update_url = "%s%s"%(url,href)
    check_url = "%s%s"%(update_url, dataset_id)
    if requests.get(check_url, verify=False).status_code == 200:
        update_url = check_url
    data = {
            'identifier': dataset_id,
            publication_year: 2012,
            name: "2012_rel3: Global Mean Sea Level Time Series (seasonal signals retained)",
            url: "http://sealevel.colorado.edu/content/2012rel3-global-mean-sea-level-time-series-seasonal-signals-retained",
            }

    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()

    href = "/dataset/contributors/%s"%dataset_id
    update_url = "%s%s"%(url,href)
    data =  {
                'person_id': 15294,
                'role_type_identifier': "convening_lead_author",
                'organization_identifier': "university-colorado",
            }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()
    """
    contributors: [
    {
        role_type_identifier: "convening_lead_author",
        person: { },
        person_id: null,
        organization_uri: "/organization/university-colorado",
        href: "https://gcis-search-stage.jpl.net:3000/contributor/15294.json",
        uri: "/contributor/15294",
        organization: {
            url: "http://www.cu.edu/",
            identifier: "university-colorado",
            name: "University of Colorado (System)",
            country_code: "US",
            organization_type_identifier: "academic"
        },
        person_uri: null,
        id: 15294
    }
    ],
    """
    
    
    
    #dataset: Grey Shaded Areas(report)
    dataset_id = "a549fd51-0537-4a9b-b85e-a2082efdd841"
    href = "/webpage/"
    update_url = "%s%s"%(url,href)
    check_url = "%s%s"%(update_url, dataset_id)
    if requests.get(check_url, verify=False).status_code == 200:
        update_url = check_url
    data = {
            'identifier': dataset_id,
            url: "http://scenarios.globalchange.gov/report/global-sea-level-rise-scenarios-united-states-national-climate-assessment",
            title: "Global Sea Level Rise Scenarios for the United States National Climate Assessment",
            }

    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()
   
    href = "/webpage/prov/%s"%dataset_id
    update_url = (url, href)
    data = {
            'parent_uri':"/report/usgcrp-ocpfy2014/chapter/federal-investments-global-change-research",
            'parent_rel': "cito:isCitedBy",
            'publication_type_identifier': "chapter"
            }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()

    #has parents
    """
    parents: [
    {
        publication_type_identifier: "chapter",
        note: "",
        url: "/report/usgcrp-ocpfy2014/chapter/federal-investments-global-change-research",
        label: "chapter usgcrp-ocpfy2014 chapter 3 : Federal Investments In Global Change Research",
        relationship: "cito:isCitedBy",
        activity_uri: null
    }
    ],
    """

    #Article Estimating Mean Sea Level Change from the TOPEX and Jason Altimeter Missions
    article_id = "10.1080/01490419.2010.491031"
    href = "/article/"
    update_url = "%s%s"%(url,href)
    check_url = "%s%s"%(update_url, dataset_id)
    if requests.get(check_ulr, verify=False).status_code == 200:
        update_url = check_url
    data = {
            'identifier': article_id,
            journal_identifier: "marine-geodesy",
            year: 2010,
            title: "Estimating Mean Sea Level Change from the TOPEX and Jason Altimeter Missions",
            journal_vol: "33",
            doi: "10.1080/01490419.2010.491031",
            journal_pages: "435-446",

            }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()

    href = "/article/contributors/%s"%article_id
    update_url = "%s%s"%(url, href)
    contributors = [
        {
            'role': "author",
            'person_id': 6673,
            'identifier': 8996,
        },
        {
            'role':"author",
            'person_id': 6674,
            'identifier':8997,
        },
        {
            'role':"author",
            'person_id':6675,
            'identifier': 8998,
        },
        {
            'role':"author",
            'person_id':6676,
            'identifier':8999
        },
    ]
    for data in contributors:
        r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
        r.raise_for_status()

    

    """
    contributors: [
    {
        role_type_identifier: "author",
        person: {
            last_name: "Nerem",
            id: 6673,
            orcid: null,
            middle_name: null,
            first_name: "R. S.",
            url: null
        },
        organization_uri: null,
        person_id: 6673,
        href: "https://gcis-search-stage.jpl.net:3000/contributor/8996.json",
        person_uri: "/person/6673",
        organization: null,
        id: 8996,
        uri: "/contributor/8996"
    },
    {
            href: "https://gcis-search-stage.jpl.net:3000/contributor/8997.json",
            organization: null,
            person_uri: "/person/6674",
            id: 8997,
            uri: "/contributor/8997",
            role_type_identifier: "author",
            person: {
                url: null,
                last_name: "Chambers",
                id: 6674,
                orcid: null,
                first_name: "D. P.",
                middle_name: null
            },
            organization_uri: null,
            person_id: 6674
    },
    {
        id: 8998,
        person_uri: "/person/6675",
        organization: null,
        uri: "/contributor/8998",
        href: "https://gcis-search-stage.jpl.net:3000/contributor/8998.json",
        person: {
            last_name: "Choe",
            id: 6675,
            orcid: null,
            middle_name: null,
            first_name: "C.",
            url: null
        },
        role_type_identifier: "author",
        organization_uri: null,
        person_id: 6675
    },
    {
        href: "https://gcis-search-stage.jpl.net:3000/contributor/8999.json",
        id: 8999,
        person_uri: "/person/6676",
        organization: null,
        uri: "/contributor/8999",
        role_type_identifier: "author",
        person: {
            url: null,
            last_name: "Mitchum",
            orcid: null,
            id: 6676,
            first_name: "G. T.",
            middle_name: null
            },
        organization_uri: null,
        person_id: 6676
    }
    ]
    """
    #add parents
    href = "/article/prov/%s"%(article_id)
    update_url = "%s%s"%(url, href)
    data = {
            'parent_uri': "/dataset/nasa-podaac-integrated-multi-mission-ocean-altimeter-data-for-climate-research",
            'parent_rel': "prov:wasDerivedFrom",

            }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()



    """

    parents: [
    {
        url: "/dataset/nasa-podaac-integrated-multi-mission-ocean-altimeter-data-for-climate-research",
        publication_type_identifier: "dataset",
        note: "",
        label: "dataset nasa-podaac-integrated-multi-mission-ocean-altimeter-data-for-climate-research",
        relationship: "prov:wasDerivedFrom",
        activity_uri: null
    }
    ],
    """

    #add cited by
    href = "/article/prov/%s"%(article_id)
    update_url = "%s%s"%(url, href)

    cited_by = [
            {
                'reference': "/reference/7b7ffcb0-766c-43b3-ac22-db29fbffef71",
                'publication_type': "chapter",
                'publication': "/report/nca3/chapter/our-changing-climate"
                },
            {
                'publication_type': "chapter",
                'reference': "/reference/7b7ffcb0-766c-43b3-ac22-db29fbffef71",
                'publication': "/report/nca3/chapter/appendix-climate-science-supplement"
                },
            {
                'publication_type': "chapter",
                'reference': "/reference/7b7ffcb0-766c-43b3-ac22-db29fbffef71",
                'publication': "/report/nca3/chapter/hawaii"
                },
            {
                'publication_type': "figure",
                'reference': "/reference/7b7ffcb0-766c-43b3-ac22-db29fbffef71",
                'publication': "/report/nca3/chapter/our-changing-climate/figure/past-and-projected-changes-in-global-sea-level-rise"
                },
            {
                'reference': "/reference/7b7ffcb0-766c-43b3-ac22-db29fbffef71",
                'publication_type': "finding",
                'publication': "/report/nca3/chapter/hawaii/finding/rising-sea-water-damages"
                },
            {
                'publication': "/report/nca3/chapter/appendix-scenarios-and-models",
                'reference': "/reference/7b7ffcb0-766c-43b3-ac22-db29fbffef71",
                'publication_type': "chapter"
                },
            {
                'reference': "/reference/7b7ffcb0-766c-43b3-ac22-db29fbffef71",
                'publication_type': "figure",
                'publication': "/report/nca3/chapter/appendix-climate-science-supplement/figure/sea-level-rise-19932012"
                },
            {
                'publication': "/report/nca3",
                'publication_type': "report",
                'reference': "/reference/7b7ffcb0-766c-43b3-ac22-db29fbffef71"
                }

            ]

    for data in cited_by:
        r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
        r.raise_for_status()


    """
    cited_by: [
    {
        reference: "/reference/7b7ffcb0-766c-43b3-ac22-db29fbffef71",
        publication_type: "chapter",
        publication: "/report/nca3/chapter/our-changing-climate"
    },
    {
            publication_type: "chapter",
            reference: "/reference/7b7ffcb0-766c-43b3-ac22-db29fbffef71",
            publication: "/report/nca3/chapter/appendix-climate-science-supplement"
            },
    {
            publication_type: "chapter",
            reference: "/reference/7b7ffcb0-766c-43b3-ac22-db29fbffef71",
            publication: "/report/nca3/chapter/hawaii"
            },
    {
            publication_type: "figure",
            reference: "/reference/7b7ffcb0-766c-43b3-ac22-db29fbffef71",
            publication: "/report/nca3/chapter/our-changing-climate/figure/past-and-projected-changes-in-global-sea-level-rise"
            },
    {
            reference: "/reference/7b7ffcb0-766c-43b3-ac22-db29fbffef71",
            publication_type: "finding",
            publication: "/report/nca3/chapter/hawaii/finding/rising-sea-water-damages"
    },
    {
        publication: "/report/nca3/chapter/appendix-scenarios-and-models",
        reference: "/reference/7b7ffcb0-766c-43b3-ac22-db29fbffef71",
        publication_type: "chapter"
    },
    {
        reference: "/reference/7b7ffcb0-766c-43b3-ac22-db29fbffef71",
        publication_type: "figure",
        publication: "/report/nca3/chapter/appendix-climate-science-supplement/figure/sea-level-rise-19932012"
    },
    {
            publication: "/report/nca3",
            publication_type: "report",
            reference: "/reference/7b7ffcb0-766c-43b3-ac22-db29fbffef71"
            }
    ],


    """



    #activity: nca3-past_projected_changes_clobal_sea_level_rise-process
    act_id = "nca3-past_projected_changes_global_sea_level_rise-process"
    href = "/activity/"
    update_url = "%s%s"%(url, href)
    check_url = "%s%s"%(update_url, act_id)
    if requests.get(check_ulr, verify=False).status_code == 200:
        update_url = check_url
    data = {
            'identifier': act_id,
            #'software': " % plot_scenarios.m - matlab script to plot future sea level scenarios % along with historical sea level rise % 8/28/2012 % revised 11/2/2012 to remove intermediate scenarios and replace with % 1 to 4 foot bound by 2100 % first generate scenarios t=[1992:2100];tt=t-1992; lowsc=0.0017*tt; ilowsc=0.0017*tt+2.71e-5*tt.^2; ihisc=0.0017*tt+8.71e-5*tt.^2; hisc=0.0017*tt+1.56e-4*tt.^2; lowsc=lowsc-interp1(t,lowsc,2000); ilowsc=ilowsc-interp1(t,ilowsc,2000); hisc=hisc-interp1(t,hisc,2000); ihisc=ihisc-interp1(t,ihisc,2000); % load proxy data load kemp_data kslr(:,2)=kslr(:,2)-.3; % fit 9-degree polynomial to data x=kslr(:,1); [p,s,mu]=polyfit(x,kslr(:,2),9); xhat=(x-mu(1))/mu(2); xx=[xhat*0,xhat,xhat.^2,xhat.^3,xhat.^4,xhat.^5,... xhat.^6,xhat.^7,xhat.^8,xhat.^9]; ksmooth=xx*p(end:-1:1)'-.183; ksmooth=ksmooth-ksmooth(end)+.12; iii=find(kslr(:,1)>1700&kslr(:,1)<1900); % estimate error bar err=sqrt(mean(kslr(:,4).^2)); % load Church reconstruction ch=load('CSIRO_Recons_gmsl_mo_2011.txt'); ii=find(ch(:,1)>1992&ch(:,1)<1993); ch(:,2)=ch(:,2)-interp1(ch(:,1),ch(:,2),2000); ch(:,2)=ch(:,2)/1000; % load nerem data ssh=load('sl_ns_global.txt'); ssh(:,2)=ssh(:,2)/1000; ii=find(ssh(:,1)>1993&ssh(:,1)<1994); ssh(:,2)=ssh(:,2)-mean(ssh(ii,2))+.004; ssh(:,2)=ssh(:,2)-interp1(ssh(:,1),ssh(:,2),2000)+.004; % convert meters to feet fac=39.3701/12; % make a plot clf,a1=subplot(1,1,1);hold on jjj=find(t>=2000); plot(kslr(iii,1),ksmooth(iii)*fac,'r','linewidth',2) plot(ch(:,1),ch(:,2)*fac,ssh(:,1),ssh(:,2)*fac,'linewidth',2) plot(t,lowsc*fac,'color',[1 1 1]*.8,'linewidth',2) plot(t,hisc*fac,'--','linewidth',4,'color',[1 1 1]*1) pp1x=[t(jjj) t(jjj(end)) t(jjj(end:-1:1))]; pp1y=[lowsc(jjj) ihisc(jjj(end)) ihisc(jjj(end:-1:1))]*fac; pp1=patch(pp1x,pp1y,[1 1 1]*.8,'edgecolor',[1 1 1]*.8); pp2x=pp1x; pp2y=[ihisc(jjj) hisc(jjj(end)) hisc(jjj(end:-1:1))]*fac; pp2c=[t(jjj)*0+.8 1 t(jjj(end:-1:1))*0+1]; pp2=patch(pp2x,pp2y,pp2c,'edgecolor','none','facecolor','interp'); colormap gray,caxis([0 1]) plot(kslr(iii,1),ksmooth(iii)*fac,'r','linewidth',2) p1x=[kslr(iii,1);kslr(iii(end:-1:1),1);kslr(iii(1),1)]; p1y=[ksmooth(iii)-err;ksmooth(iii(end:-1:1))+err;ksmooth(iii(1))]; p1=patch(p1x,p1y*fac,[1 .7 .7],'edgecolor','none'); plot(kslr(iii,1),ksmooth(iii)*fac,'r','linewidth',2) plot(t,lowsc*fac,'color',[1 1 1]*.8,... 'linewidth',2) plot(ch(:,1),ch(:,2)*fac,ssh(:,1),ssh(:,2)*fac,'linewidth',2) axis([1800 2100 -1 7]),set(gca,'fontsize',16) xlabel('Year (AD)'),ylabel('Global Sea Level Rise (feet)') set(a1,'position',[0.13 0.11 .75 .7]) t1=text(2116,0.17*fac,{'0.66 ft'}); %t2=text(2120,0.5*fac+.1,{'Int. Low';'1.6 ft'}); %t3=text(2120,1.2*fac+.1,{'Int. High';'3.9 ft'}); t4=text(2090,2.11*fac,{'Scenarios above';... '6 or 7 ft by 2100';'are not plausible'},... 'edgecolor','k','backgroundcolor','w'); set([t1,t4],'fontsize',12,'horizontalalignment','center',... 'verticalalignment','middle') pp3=patch([2097.5 2102.5 2102.5 2097.5 2097.5],[1 1 4 4 1],'r'); set(pp3,'edgecolor','none','facecolor',[1 .7 .2],'clipping','off') pp4=plot([2100 2100],[1 4],'color',[1 .5 0],'linewidth',2); pp5=plot([2095 2105],[1 1],'color',[1 .5 0],'linewidth',2); pp6=plot([2095 2105],[4 4],'color',[1 .5 0],'linewidth',2); set(gca,'ygrid','on') set([pp4;pp5;pp6],'clipping','off') tl1=text(1806,0,'Proxy Records','color','r','backgroundcolor','w'); tl2=text(1887,.5,'Tide Gauge Data','color','b','backgroundcolor','w'); tl3=text(1975,1.4,'Satellites','color',[0 .5 0],'backgroundcolor','w'); tl4=text(2050,3.2,{'Future';'Scenarios'},'color','k','backgroundcolor','w'); tl5=text(2116,2.5,{'Likely Range';'1 to 4 feet'},'color',[1 0 0],... 'rotation',270,'horizontalalignment','center',... 'verticalalignment','middle','fontsize',14); set([tl1,tl2,tl3,tl4],'fontsize',14,'fontweight','normal') set(tl4,'horizontalalignment','center','edgecolor','k') ann1=annotation('arrow',[.63 .63],[.30 .23]); set(ann1,'color',[0 .5 0]) title('Global Sea Level Rise') print -depsc -f1 slr_scenarios_v4.eps !/home/jwillis/.eps2gif slr_scenarios_v4",
        }
    r = gcis.s.post(update_url, data=json.dumps(data), verify = False)
    r.raise_for_status()


#insert parents
    href = "/article/prov/%s"%(article_id)
    update_url = "%s%s"%(url, href)

       
    


    """
    publication_maps: [
            {
                parent: 19880,
                parent_uri: "/publication/19880",
                note: "",
                activity_identifier: "nca3-past_projected_changes_global_sea_level_rise-process",
                child_uri: "/publication/16896",
                child: 16896,
                relationship: "prov:wasDerivedFrom"
                },
            {
                activity_identifier: "nca3-past_projected_changes_global_sea_level_rise-process",
                child_uri: "/publication/16896",
                child: 16896,
                relationship: "prov:wasDerivedFrom",
                parent: 19881,
                parent_uri: "/publication/19881",
                note: ""
                },
            {
                relationship: "prov:wasDerivedFrom",
                child: 16896,
                child_uri: "/publication/16896",
                activity_identifier: "nca3-past_projected_changes_global_sea_level_rise-process",
                note: "",
                parent: 19819,
                parent_uri: "/publication/19819"
                },
            {
                relationship: "prov:wasDerivedFrom",
                child: 16896,
                child_uri: "/publication/16896",
                activity_identifier: "nca3-past_projected_changes_global_sea_level_rise-process",
                note: "",
                parent: 19882,
                parent_uri: "/publication/19882"
                }
            ],
    """


if __name__ == "__main__":
    desc = "Updated Figure 2.26: Past and Projected Changes in Global Sea Level Rise"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('url', help="GCIS url")
    args = parser.parse_args()
    update(args.url)
