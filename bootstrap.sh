# Download keys
mkdir -p uic-keys
wget https://railpublickey.uic.org/download.php --no-check-certificate -O uic-keys/keys.xml

# Generate model
kaitai-struct-compiler ticket.ksy -t python

# Setup python environment
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt