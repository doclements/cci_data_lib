# pylint: disable=W0311
import numpy as np

from .templates import area_extraction, area_extraction_no_time
from cci_data_service.utils import create_query, web_post, web_post_file
from cci_data_service.query.query import Query

class Area(Query):
    def __init__(self, service, lat1,lat2, lon1, lon2, coverage,date=None, output="csv"):
        super(Area, self).__init__(service, coverage)
        if date is None:
            self.template_params = {
                "lat1": lat1,
                "lat2": lat2,
                "lon1": lon1,
                "lon2": lon2,
                "x_label":self.x_name,
                "y_label":self.y_name,
                "output": output
            }
            self.template = area_extraction_no_time
        else:
            self.template_params = {
                "lat1": lat1,
                "lat2": lat2,
                "lon1": lon1,
                "lon2": lon2,
                "date": date,
                "time_label":self.coverage_time,
                "x_label":self.x_name,
                "y_label":self.y_name,
                "output": output
            }
            self.template = area_extraction
        self.output = output
        self._get_data()


    def _get_data(self):
        self.query = create_query(self)
        if self.output == "csv":
            self.data = web_post(self.wcps_url, {"query":self.query})[1:-1]
            self.data = self.data.split('},{')
            self.data = [x.split(',') for x in self.data]
            self.data = np.array(self.data)
            self.data = self.data.astype(np.float)
        if self.output == "netcdf":
            self.data = web_post_file(self.wcps_url, {"query":self.query})
        if self.output == "gtiff":
            self.data = web_post_file(self.wcps_url, {"query":self.query})
