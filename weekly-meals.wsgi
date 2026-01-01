import sys
import site

# Activate the virtual environment
site.addsitedir('/var/www/weekly-meals/.venv/lib/python3.11/dist-packages')
sys.path.append('/var/www/weekly-meals')

from webui.app import app as application