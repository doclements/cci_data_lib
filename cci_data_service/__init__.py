coverages = {
    "v_3.0": {
        "chlor_a": "OCCCI_V3_monthly_chlor_a"
    },
    "v_2.0": {
        "chlor_a": "CCI_V2_monthly_chlor_a"
    },
    "ecmwf_test": {
        "2m_air_temp" : "temp2m"
    }
}

services = {
    "pml" : "http://earthserver.pml.ac.uk/rasdaman/ows/wcps",
    "ecmwf" : "http://earthserver.ecmwf.int/rasdaman/ows/wcps"
}


x_y_lookup = {
    "E" : "X", 
    "N" : "Y",
    "Lat" : "Y",
    "Long" : "X"
}