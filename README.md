# property_management_space

# create property models
url: http://127.0.0.1:8000/api
method: post
request body: property_name, address, city, state

# fetch property models data
url: http://127.0.0.1:8000/api
method: get
request params: city_name

# update property model data 
url: http://127.0.0.1:8000/api/update-property-view/int:pk/
method: put
request body: property_name, address, city, state


# filter property model by its state
url: http://127.0.0.1:8000/api
method: get
request params: state_name
