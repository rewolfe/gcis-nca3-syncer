#!/bin/bash
if [ ! -d "env" ]; then
  virtualenv env
  source env/bin/activate
  pip install requests
  pip install git+git://github.com/USGCRP/gcis-py-client.git
fi
