# pylint: disable=W0311

from .templates import point_extraction, point_extraction_no_time
from cci_data_service.utils import create_query, web_post
from cci_data_service.query.query import Query

class Point(Query):
    def __init__(self, service, lat, lon, coverage, date=None):
        super(Point, self).__init__(service, coverage)
        if date is None:
            self.template_params = {
                "lat": lat,
                "lon": lon,
                "x_label":self.x_name,
                "y_label":self.y_name
            }
            self.template = point_extraction_no_time
        else:
            self.template_params = {
                "lat": lat,
                "lon": lon,
                "date": date,
                "time_label":self.coverage_time,
                "x_label":self.x_name,
                "y_label":self.y_name
            }
            self.template = point_extraction
        self._get_data()

    def _get_data(self):
        self.query = create_query(self)
        print self.query
        try:
            self.data = float(web_post(self.wcps_url, {"query":self.query})[1:-1])
        except Exception, e:
            self.data = [float(x) for x in web_post(self.wcps_url, {"query":self.query})[2:-2].split(' ')]
