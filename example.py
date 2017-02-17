# pylint: disable=W0311

from cci_data_service import coverages, services
from cci_data_service.query.point import Point
from cci_data_service.query.point_timeseries import PointTimeSeries
from cci_data_service.query.area import Area
from cci_data_service.query.area_timeseries import AreaTimeseries
from cci_data_service.service import Service

from cci_data_service.query.query import Query

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# _service = services['pml']
# _ecmwf_service = services['ecmwf']

# # print "blah"
# service = Service("http://earthserver.pml.ac.uk/rasdaman/ows")

# point = Point(service,55, -40,  service.coverages['OCCCI_V3_monthly_chlor_a'], date="2006-06-01T00:00:00Z")

# print point.data

# point = Point(_service,55, -40, "2006-05-31T23:59:00Z", coverages['v_2.0']['chlor_a'])
# print point.data

# point = Point(_service,55, -40, "2006-06-30T23:59:00Z", coverages['v_2.0']['chlor_a'])
# print point.data

# pointTS = PointTimeSeries(service,55, -40, "2006-06-01T00:00:00Z","2006-10-01T00:00:00Z", service.coverages['OCCCI_V3_monthly_chlor_a'])
# print pointTS.data



# area = Area(_service, 50, 80, -50, 0, "2006-06-01T00:00:00Z",coverages['v_3.0']['chlor_a'], output="gtiff")
# print area.query
# with open('test_output.tiff', 'w') as outfile:
#    outfile.write(area.data)


# csv output will be auto parsed into a numpy array this example then snows potting that using matplot lib
# need a clean way to remove nulls
# area = Area(service, 40, 60, -50, -0, "2006-09-01T00:00:00Z",service.coverages['OCCCI_V3_monthly_chlor_a'], output="csv")
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
"""

"""

# csv output will be auto parsed into a numpy array this example then snows potting that using matplot lib
# need a clean way to remove nulls
# areaTS = AreaTimeseries(service, 50, 60, -15, 0, "2006-06-01T00:00:00Z","2006-11-01T00:00:00Z",service.coverages['OCCCI_V3_monthly_chlor_a'], output="csv")
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
# ecmwf_service = Service("http://earthserver.ecmwf.int/rasdaman/ows")

# ecwms_area = Area(ecmwf_service,-80, 80, -180, 179, "2012-01-01T06:00:00Z",  ecmwf_service.coverages['temp2m'])
# print ecwms_area.data.shape
# print ecwms_area.data
# print np.min(ecwms_area.data)
# print np.max(ecwms_area.data)
# plt.imshow(ecwms_area.data)
# plt.show()
# point = Point(ecmwf_service,50.347472, -4.217737, "2012-01-01T06:00:00Z", ecmwf_service.coverages['temp2m'])
# print point.data
# print point.data  - 273.15
# point = Point(ecmwf_service,50.347472, -4.217737, "2012-02-01T06:00:00Z", ecmwf_service.coverages['temp2m'])
# print point.data
# print point.data  - 273.15

# ECMWF time series test
# point = PointTimeSeries(ecmwf_service,50.347472, -4.217737,  "2010-03-01T12:00:00Z", "2012-03-01T12:00:00Z", ecmwf_service.coverages['temp2m'])
# plt.plot([x - 273.15 for x in point.data][0::4])
# plt.show()


# point = PointTimeSeries(ecmwf_service,51.584852, -4.196566,  "2010-03-01T12:00:00Z", "2012-03-01T12:00:00Z", ecmwf_service.coverages['temp2m'])
# plt.plot([x - 273.15 for x in point.data][0::4])
# plt.show()
"""sdl;dlfks;ldkf

"""

# MEEO test - they dont use ansi so this is a test of the config files
# example date 2016-07-14T11:10:52Z for coverage L8_B2_32630_30
# frt00008306_07_if163l_trr3
jub_service = Service("http://access.planetserver.eu:8080/rasdaman/ows")
# point = Point(jub_service, 562.6610837,298.2737483, jub_service.coverages['frt0000a0ac_07_if165l_trr3'])
# print point.data

area = Area(jub_service, 562.6610837, 600, 298.2737483, 320, jub_service.coverages['frt0000a0ac_07_if165l_trr3'], output="netcdf")
with open('test_output_jub_area.nc', 'w') as outfile:
   outfile.write(area.data)
#print point.data


# meeo_area = Area(meeo_service, 4902991, 4917275, 377983, 390000, "2015-05-31T10:34:57Z" , meeo_service.coverages['L8_B5_32631_30'])
# print meeo_area.data.shape
# print meeo_area.data
# print np.min(meeo_area.data)
# print np.max(meeo_area.data)
# plt.imshow(meeo_area.data)
# plt.show()


# from cci_data_service.query.templates import landsat_rgb_area
# from cci_data_service.utils import create_query, web_post, web_post_file

# class CustomQuery(Query):
#     def __init__(self, service, south, north, west, east, date, coverage_id, output="csv"):
#         coverage = service.coverages['L8_B5_'+coverage_id]
#         super(CustomQuery, self).__init__(service, coverage)
#         self.template_params = {
#             "swath_id": coverage_id,
#             "south": south,
#             "north": north,
#             "west": west,
#             "east": east,
#             "date": date,
#             "time_label":self.coverage_time,
#             "x_label":self.x_name,
#             "y_label":self.y_name
#         }
#         self.output = output
#         self.template = landsat_rgb_area
#         self._get_data()

#     def _get_data(self):
#         self.query = create_query(self)
#         print self.query
#         if self.output == "csv":
#             self.data = web_post(self.wcps_url, {"query":self.query})[1:-1]
#             self.data = self.data.split('},{')
#             self.data = [x.split(',') for x in self.data]
#             self.data = np.array(self.data)
#             self.data = self.data.astype(np.float)
#         if self.output == "netcdf":
#             self.data = web_post_file(self.wcps_url, {"query":self.query})
#         if self.output == "gtiff":
#             self.data = web_post_file(self.wcps_url, {"query":self.query})
#         if self.output == "png":
#             #



# meeo_area = CustomQuery(meeo_service, 4902991, 4917275, 377983, 390000, "2015-05-31T10:34:57Z" , "32631_30")
# print meeo_area.data.shape
# print meeo_area.data
# print np.min(meeo_area.data)
# print np.max(meeo_area.data)
# plt.imshow(meeo_area.data)
# plt.show()
