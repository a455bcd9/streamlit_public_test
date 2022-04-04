"""Display a histogram of the users' stuff
"""

import json
import requests
import csv
from datetime import date
import os
from pyairtable import Table
from datetime import datetime, timezone
from urllib.parse import urlparse
import re
import streamlit as st
import pandas as pd
import numpy as np

st.title('Crypto-demographics of Courtyard NFT holders')
data_load_state = st.text('Loading data...')

AIRTABLE_KEY = os.getenv('AIRTABLE_KEY')
AIRTABLE_BASE_ID = os.getenv('AIRTABLE_BASE_ID')
table = Table(AIRTABLE_KEY, AIRTABLE_BASE_ID, 'users')
              
data_load_state.text("Done!")
