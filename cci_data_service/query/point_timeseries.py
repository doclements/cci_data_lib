# pylint: disable=W0311

import numpy as np

from .templates import point_extraction_timeseries
from cci_data_service.utils import create_query, web_post
from cci_data_service.query.query import Query


class PointTimeSeries(Query):
    def __init__(self, service, lat, lon, start_date, end_date, coverage):
        super(PointTimeSeries, self).__init__(service, coverage)
        self.coords = {
            "lat": lat,
            "lon": lon,
            "date1": start_date,
            "date2": end_date
        }
        self.template = point_extraction_timeseries
        self._get_data()

    def _get_data(self):
        self.query = create_query(self)
        self.data = np.array([float(x) for x in web_post(self.service, {"query":self.query})[1:-1].split(',')])
