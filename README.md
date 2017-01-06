# CCI Open Data Extraction Library

## Aim

The library aims to provide programatic access to the complete ESA OC-CCI data catalogue. The library makes use of the OGC WCS Processing extension WCPS. As such to work **the library does require an internet connection**.

The library will allow predefined queries to be run and the results will be parsed into appropriate data structure. Most will utilise [numpy](http://www.numpy.org/). 

## TBD

1. simple point extraction
2. simple point timeseries extraction 
3. area extraction - will have flags for kind of processing (mean/median/min/max/...)
4. area timeseries extraction - flags as above

## TBD - MAYBE

1. output plot option 
  * maybe use matplotlib/bokeh/something else? 
  * maybe make its a pluggable system 
2. output image option
  * similar to owslib we could offere a file type object