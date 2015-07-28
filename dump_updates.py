#!/usr/bin/env python
import os, sys, re, logging, json, requests, argparse
from bs4 import BeautifulSoup

from gcis_clients import GcisClient


log_format = "[%(asctime)s: %(levelname)s/%(funcName)s] %(message)s"
logging.basicConfig(format=log_format, level=logging.INFO)


DEL_RE = re.compile(r'^\d+\s+days\s+ago:\s+(?P<val>.*)\s+(?P<user>.*?)\s+deleted\s+(?P<type>.*)\s*$')


def crawl_all(url, output_dir):
    """Crawl watch log and detect changes to NCA3 info."""

    # scrape watch log
    gcis = GcisClient(url)
    r = gcis.s.get("%s/watch" % url, params={ 'limit': 1000000,
                                              'type': 'changes',
                                              't': 'any' }, verify=False)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, 'lxml')
    divs = soup.find_all('div', class_="logrow")
    divs.reverse() # sort logs by ascending time order
    for div in divs:
        logging.info("#" * 80)

        # extract summary
        summary = " ".join([" ".join(i.split()) for i in div.stripped_strings])
        logging.info(summary)

        # detect deletion
        match = DEL_RE.search(summary)
        if match:
            val, user, doc_type = match.groups()
            logging.info("user: %s" % user)
            logging.info("value: %s" % val)
            logging.info("type: %s" % doc_type)

        # extract link
        a = div.a
        if a is not None:
            href = a.get('href')
            a_url = "%s%s.json" % (url, href)
            doc_file = "%s%s.json" % (output_dir, href)
            doc_dir = os.path.dirname(doc_file)
            logging.info("%s %s %s %s" % (output_dir, a_url, doc_file, doc_dir))
            if not os.path.isdir(doc_dir): os.makedirs(doc_dir, 0755)
            r = gcis.s.get(a_url, verify=False)
            if r.status_code == 404: continue
            with open(doc_file, 'w') as f:
                json.dump(r.json(), f, indent=2, sort_keys=True)


if __name__ == "__main__":
    desc = "Crawl and dump changes made to GCIS relating to NCA3 info."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('url', help="GCIS url")
    parser.add_argument('output_dir', help="output directory")
    args = parser.parse_args()
    crawl_all(args.url, args.output_dir)
