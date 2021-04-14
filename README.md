# glm-data-stream
Data stream using of GOES Lightning mapper (GLM). 
Converts the raw NetCDF4 files from National Oceanic and Atmospheric Administration(NOAA)'s repository at Amazon Web Service (AWS) into mor readable JSON files.

This application is event-based on the creation of the files. As such, it will use AWS's services, such as Lambda, to handle the triggering.