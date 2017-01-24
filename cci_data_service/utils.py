# pylint: disable=W0311
import requests
from cci_data_service import x_y_lookup


def create_query(queryObj):
   queryObj.template_params['coverage'] = queryObj.coverage
   _q = queryObj.template.format(**queryObj.template_params)
   return _q


def web_post(url, payload):
   return requests.post(url, data=payload).text

def web_post_file(url, payload):
   return requests.post(url, data=payload).content


def get_lat_long(test_value):
   for p in x_y_lookup:
      if test_value in x_y_lookup[p]:
         return p
