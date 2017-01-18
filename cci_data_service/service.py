# pylint: disable=W0311

import hashlib
import os

from owslib.wcs import WebCoverageService

class Service(object):
    def __init__(self, url, config_path=None):
        super(Service, self).__init__()
        self.url = url
        self.url_hash = hashlib.md5(self.url).hexdigest()
        self.config_path = config_path
        self._setup()



    def _setup(self):
        if not self.config_path:
           if not self.config_exists():
              print "config does not exists - CREATING new config"
              _fpath = os.path.join(os.path.dirname(__file__), 'configs', self.url_hash+'.txt')
              with open(_fpath, 'w') as config_file:
                  self.init_config(config_file)

    def config_exists(self):
        return os.path.isfile(os.path.join(os.path.dirname(__file__), 'configs', self.url_hash+'.txt'))

    def init_config(self, config_file):
        _wcs = WebCoverageService(self.url, version="2.0.0")
        _covs = _wcs.contents.keys()
        for _cov in _covs:
            print "writting coverage info"
            config_file.write(_cov)
        return
