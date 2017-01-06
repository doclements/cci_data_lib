from cci_data_service import coverages, services
from cci_data_service.query.point import Point
from cci_data_service.query.point_timeseries import PointTimeSeries

_service = services['pml']

point = Point(_service,55, -40, "2006-06-01T00:00:00Z", coverages['v_3.0']['chlor_a'])
print point.data

point = Point(_service,55, -40, "2006-05-31T23:59:00Z", coverages['v_2.0']['chlor_a'])
print point.data

point = Point(_service,55, -40, "2006-06-30T23:59:00Z", coverages['v_2.0']['chlor_a'])
print point.data

pointTS = PointTimeSeries(_service,55, -40, "2006-06-01T00:00:00Z","2006-10-01T00:00:00Z", coverages['v_3.0']['chlor_a'])
print pointTS.data
