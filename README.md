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


## redesign of service object

1. have a `service` Class that is initialised by service url
2. this class's responsibility is to either get service info from :-
  * static config file
  * web coverage service description docs -> stored in config files hereafter
  * taking config info from user during init params

## TBD for multi/hyperspectral

1. Band needs specifying as well as coverage
  * multiple could be used
  * or if none specified some object to hold an underterminate number or sub results
2. Need to get spatial info from WCS this is only way o make dynamic
  * or we can continue down the config file route?
  * could get huge but parsing xml every time would be slow as hell
  * axis info is definietly needed by all services - again slow vs big config file.


### how could a fully dynamic system be called?

Current signature is  :
`Point(_service,55, -40, "2006-06-01T00:00:00Z", coverages['v_3.0']['chlor_a'])`
This takes a URL from the services dictionary and a coverage from a similar dictionary.

If we want to make it truly dynamic how are users going to know what coverage name to give anyway? Does the actual use of the library implies a certain knowledge about the data?

I think it is probably OK to assume that, like with libs like `OWSLib`, the user will probably use the library in interactive mode to get the info then will use in static script or similar after that.

proposed signature :
`Service_Instance(service_url)`
`Point(Service_Instance,55, -40, "2006-06-01T00:00:00Z", Service_Instance.coverages['OCCCI_V3_monthly_chlor_a'] )`