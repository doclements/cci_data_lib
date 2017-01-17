# pylint: disable=W0311
import numpy as np

from .templates import area_timeseries_extraction
from cci_data_service.utils import create_query, web_post, web_post_file
from cci_data_service.query.query import Query

class AreaTimeseries(Query):
    def __init__(self, service, lat1,lat2, lon1, lon2, start_date, end_date, coverage, output="csv"):
        super(AreaTimeseries, self).__init__(service, coverage)
        self.coords = {
            "lat1": lat1,
            "lat2": lat2,
            "lon1": lon1,
            "lon2": lon2,
            "date1": start_date,
            "date2": end_date,
            "output": output
        }
        self.output = output
        self.template = area_timeseries_extraction
        self._get_data()


    def _get_data(self):
        self.query = create_query(self)
        if self.output == "csv":
            self.data = web_post(self.service, {"query":self.query})
            self.data = self.data[2:-2]
            self.data = self.data.split('}},{{')

            self.data = [x.split('},{') for x in self.data]
            self.data = [[x.split(',') for x in y] for y in self.data]
            self.data = np.array(self.data)
            self.data = self.data.astype(np.float)
        if self.output == "netcdf":
            self.data = web_post_file(self.service, {"query":self.query})
