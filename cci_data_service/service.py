# pylint: disable=W0311

class Service(object):
    def __init__(self, url, config_path=None):
        super(Service, self).__init__()
        self.url = url
        self.config_path = config_path
        self._setup()



    def _setup(self):
       pass
       