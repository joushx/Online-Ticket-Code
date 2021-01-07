#!/bin/bash

# Download keys
mkdir -p uic-keys
wget https://railpublickey.uic.org/download.php --no-check-certificate -O uic-keys/keys.xml

# Generate model
kaitai-struct-compiler definitions/ticket.ksy -t python --outdir onlineticket/generated
kaitai-struct-compiler definitions/head.ksy -t python --outdir onlineticket/generated
kaitai-struct-compiler definitions/db_bl.ksy -t python --outdir onlineticket/generated

# Setup python environment
python3 -m venv env
source "env/bin/activate"
pip install -r requirements.txt