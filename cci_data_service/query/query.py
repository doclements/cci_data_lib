# pylint: disable=W0311

class Query(object):
    def __init__(self, service, coverage):
        super(Query, self).__init__()
        self.service = service
        self.wcps_url = service.wcps_url
        self.coverage = coverage
        self.coverage_time = str(coverage['time_axis_name'][0])
        self.data = None
       