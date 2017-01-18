from cci_data_service import coverages, services
from cci_data_service.query.point import Point
from cci_data_service.query.point_timeseries import PointTimeSeries
from cci_data_service.query.area import Area
from cci_data_service.query.area_timeseries import AreaTimeseries

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

_service = services['pml']
_ecmwf_service = services['ecmwf']

# point = Point(_service,55, -40, "2006-06-01T00:00:00Z", coverages['v_3.0']['chlor_a'])
# print point.data

# point = Point(_service,55, -40, "2006-05-31T23:59:00Z", coverages['v_2.0']['chlor_a'])
# print point.data

# point = Point(_service,55, -40, "2006-06-30T23:59:00Z", coverages['v_2.0']['chlor_a'])
# print point.data

# pointTS = PointTimeSeries(_service,55, -40, "2006-06-01T00:00:00Z","2006-10-01T00:00:00Z", coverages['v_3.0']['chlor_a'])
# print pointTS.data

area = Area(_service, 50, 80, -50, 0, "2006-06-01T00:00:00Z",coverages['v_3.0']['chlor_a'], output="gtiff")
print area.query
with open('test_output.tiff', 'w') as outfile:
   outfile.write(area.data)


# csv output will be auto parsed into a numpy array this example then snows potting that using matplot lib
# need a clean way to remove nulls
# area = Area(_service, 50, 70, -50, -10, "2006-09-01T00:00:00Z",coverages['v_3.0']['chlor_a'], output="csv")
# print area.data.shape
# print area.data
# print np.min(area.data)
# print np.max(area.data)
# area.data[area.data == 9.96921e+36] = None
# plt.imshow(area.data, norm=matplotlib.colors.LogNorm())
# plt.show()


# areaTS = AreaTimeseries(_service, 50, 80, -50, 0, "2006-06-01T00:00:00Z","2006-09-01T00:00:00Z",coverages['v_3.0']['chlor_a'], output="netcdf")
# with open('test_output_TS.nc', 'w') as outfile:
#    outfile.write(areaTS.data)


# csv output will be auto parsed into a numpy array this example then snows potting that using matplot lib
# need a clean way to remove nulls
# areaTS = AreaTimeseries(_service, 50, 60, -15, 0, "2006-06-01T00:00:00Z","2006-11-01T00:00:00Z",coverages['v_3.0']['chlor_a'], output="csv")
# areaTS.data[areaTS.data == 9.96921e+36] = None
# _min =  np.nanmin(areaTS.data)
# _max =  np.nanmax(areaTS.data)
# st_val = 231
# plt.figure(1)
# for x in range(areaTS.data.shape[0]):
#    temp = st_val + x
#    f = plt.subplot(temp)
#    f.imshow(areaTS.data[x],norm=matplotlib.colors.LogNorm(vmin=_min, vmax=_max) )
# plt.show()


#ECMWF data test
# point = Point(_ecmwf_service,50.347472, -4.217737, "2012-01-01T06:00:00Z", coverages['ecmwf_test']['2m_air_temp'])
# print point.data
# print point.data  - 273.15
# point = Point(_ecmwf_service,50.347472, -4.217737, "2012-02-01T06:00:00Z", coverages['ecmwf_test']['2m_air_temp'])
# print point.data
# print point.data  - 273.15

# ECMWF time series test
# point = PointTimeSeries(_ecmwf_service,50.347472, -4.217737,  "2010-03-01T12:00:00Z", "2012-03-01T12:00:00Z", coverages['ecmwf_test']['2m_air_temp'])
# plt.plot([x - 273.15 for x in point.data][0::4])
# plt.show()


# point = PointTimeSeries(_ecmwf_service,51.584852, -4.196566,  "2010-03-01T12:00:00Z", "2012-03-01T12:00:00Z", coverages['ecmwf_test']['2m_air_temp'])
# plt.plot([x - 273.15 for x in point.data][0::4])
# plt.show()