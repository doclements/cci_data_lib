# pylint: disable=W0311

point_extraction = """
for c in ({coverage})
return
encode (
   c[Lat({lat}), Long({lon}), ansi("{date}")], "csv"
)
"""
area_extraction = """
for c in ({coverage})
return
encode (
   c[Lat({lat1}:{lat2}), Long({lon1}:{lon2), ansi("{date}")], "csv"
)
"""
point_extraction_timeseries = """
for c in ({coverage})
return
encode (
   c[Lat({lat}), Long({lon}), ansi("{date1}":"{date2}")], "csv"
)
"""
area_extraction_timeseries = """
for c in ({coverage})
return
encode (
   c[Lat({lat1}:{lat2}), Long({lon1}:{lon2), ansi("{date1}":"{date2}")], "csv"
)"""