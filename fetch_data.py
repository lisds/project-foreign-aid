""" Fetch and validate data
"""

from pathlib import Path
import pandas as pd
import requests
import hashlib
from zipfile import ZipFile


# file_info = {
#     # Dictionary with key values pairs, where keys are output filenames
#     # and values are dictionaries with keys URL and SHA1 hash.
#     'mosquito_beer.csv': {
#         'url': 'https://raw.githubusercontent.com/lisds/textbook/4065a20/data/mosquito_beer.csv',
#         'sha1': 'a49f198303d20f5f709b7b2ffad23726b0f537af'},
#     'family_of_veterans.xlsx': {
#         'url': 'https://www.ons.gov.uk/file?uri=/peoplepopulationandcommunity/armedforcescommunity/datasets/spousesandchildrenorstepchildrenofukarmedforcesveteranshealthandunpaidcareenglandandwales/current/veteransspouseandchildrenhealthandunpaidcareenglandandwales.xlsx',
#         'sha1': '9d1d93a6acac6ed207bcf3fce4e0694b511ed349'}
# }

# data_path = Path('data')

# for fname, info in file_info.items():
#     out_path = data_path / fname
#     r = requests.get(info['url'])
#     out_path.write_bytes(r.content)
#     assert hashlib.sha1(out_path.read_bytes()).hexdigest() == info['sha1']

# print('Fetch and validation passed')


file_info = {
    # Dictionary with key values pairs, where keys are output filenames
    # and values are dictionaries with keys URL and SHA1 hash.
    'PPD2_Jan_21_2022.zip': {
        'url': 'https://docs.aiddata.org/ad4/datasets/PPD2_archive_Jan21_2022.zip',
        'sha1': '87658660758f9736a8f9fb1b745037c25dd88567'},
}
data_path = Path('data')

for fname, info in file_info.items():
    out_path = data_path / fname
    r = requests.get(info['url'])
    out_path.write_bytes(r.content)
    assert hashlib.sha1(out_path.read_bytes()).hexdigest() == info['sha1']

print('Fetch and validation passed')


data_dir = Path('data')
data_dir.mkdir(exist_ok = True)
file_path = data_dir / Path('PPD2_Jan_21_2022.zip')
dest_path = file_path


with ZipFile(dest_path, 'r') as my_zip:
    
    csv_filename = 'PPD2_Jan_21_2022.csv'

    # Check if the CSV file exists in the zip archive
    if csv_filename in my_zip.namelist():
        # Extract the CSV file to a temporary directory
        my_zip.extract(csv_filename, path='temp')

        # Read the CSV file using pandas
        csv_path = Path('temp') / csv_filename
        df = pd.read_csv(csv_path)