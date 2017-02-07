# pylint: disable=W0311

import hashlib
import os

from owslib.wcs import WebCoverageService
import json

from cci_data_service.utils import get_lat_long



class Service(object):
    def __init__(self, url, config_path=None):
        super(Service, self).__init__()
        self.url = url
        self.wcps_url = self.url+ '/wcps'
        self.url_hash = hashlib.md5(self.url).hexdigest()
        self.config_path = config_path
        # these two lists are to fix issues at the moemnt NEED TO BE REMOVED
        self.axis_removes = ['Lat','Lon','latitude','longitude','lat','lon','Long','long','Latitude', 'Longitude', 'Easting', 'Northing','E','N']
        self.banned = ['NCITest4', 'NCITest5', 'L8_B8_32631_15', 'LS8_test_tile']
        self.coverages = {}
        self._setup()




    def _setup(self):
        if not self.config_path:
           if not self.config_exists():
              print "config does not exists - CREATING new config"
              _fpath = os.path.join(os.path.dirname(__file__), 'configs', self.url_hash+'.json')
              with open(_fpath, 'w') as config_file:
                  self.init_config(config_file)
           else:
               #print "config found using cached copy - can edit / add to it"
               self._populate_from_cache()


    def get_config_filepath(self):
       return os.path.join(os.path.dirname(__file__), 'configs', self.url_hash+'.json')


    def config_exists(self):
        return os.path.isfile(os.path.join(os.path.dirname(__file__), 'configs', self.url_hash+'.json'))

    def init_config(self, config_file):
        _wcs = WebCoverageService(self.url, version="2.0.0")
        config = {}
        _covs = _wcs.contents.keys()
        config['coverages'] = {}
        config_file.write('{ "coverages": {')
        pos = 0
        for _cov in _covs:
            #print "writting coverage info for "+_cov
            #if _cov not in self.banned:
            try:
               t_cov = {}
               try:
                   t_cov['time_axis_name'] = [item for item in _wcs.contents[_cov].grid.axislabels if item not in self.axis_removes][0]
               except Exception, e:
                   t_cov['time_axis_name'] = ''
               spatial_axis = [item for item in _wcs.contents[_cov].grid.axislabels if item in self.axis_removes]
               for p in spatial_axis:
                   t_cov[get_lat_long(p)+'_axis_name'] = p
               # gather X and Y coords definition
               del _wcs.contents[_cov]
               t_cov['name'] = _cov
               #print json.dumps({ _cov :t_cov})
               #{"OCCCI_V3_monthly_rrs_555_bias": {"Y_axis_name": "Lat", "X_axis_name": "Long", "name": "OCCCI_V3_monthly_rrs_555_bias", "time_axis_name": "ansi"}}
               t_json_string = json.dumps({ _cov :t_cov})[1:-1]
               if pos < len(_covs) -1:
                   t_json_string = t_json_string + ','
               config_file.write(t_json_string)
               #config['coverages'][_cov] = t_cov
               self.coverages[_cov] = t_cov
               pos = pos + 1
            except Exception, e:
               print e
               print "coverage {} failed you should check it".format(_cov)
        #config_file.write(json.dumps(config))
        config_file.write('} }')
        return


    def _populate_from_cache(self):
       config_file = self.get_config_filepath()
       with open(config_file) as _config:
          config_obj = json.load(_config)
          self.config = config_obj
          self.coverages = config_obj['coverages']
