# pylint: disable=W0311

point_extraction = """
for c in ({coverage})
return
encode (
   c[N({lat}), E({lon}), {time_label}("{date}")], "csv"
)
"""
area_extraction = """
for c in ({coverage})
return
encode (
   c[Lat({lat1}:{lat2}), Long({lon1}:{lon2}), {time_label}("{date}")], "{output}"
)
"""
point_extraction_timeseries = """
for c in ({coverage})
return
encode (
   c[Lat({lat}), Long({lon}), {time_label}("{date1}":"{date2}")], "csv"
)
"""
area_timeseries_extraction = """
for c in ({coverage})
return
encode (
   c[Lat({lat1}:{lat2}), Long({lon1}:{lon2}), {time_label}("{date1}":"{date2}")], "{output}"
)"""