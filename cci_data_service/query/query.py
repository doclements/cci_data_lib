# pylint: disable=W0311

class Query(object):
    def __init__(self, service, coverage):
        super(Query, self).__init__()
        self.service = service
        self.coverage = coverage
        self.data = None
       