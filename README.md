# glm-data-stream
Data stream using of GOES Lightning mapper (GLM). 
Converts the raw NetCDF4 files from National Oceanic and Atmospheric Administration(NOAA)'s repository at Amazon Web Service (AWS) into mor readable JSON files.

This application is event-based on the creation of the files. As such, it will use AWS's services, such as Lambda, to handle the triggering.



# Installation
`npm install serverless`
`npm install serverless-requirements-plugin serverless-dotenv-plugin`
`pip install -r requirements.txt`

# Testing
export all Enviroment Variables using:
`export $(xargs < .env)`

To run all the tests use:
`pytest`

To run a specific test, use:
`pytest tests/<filename> -v`
Add `-v` for verbose mode
