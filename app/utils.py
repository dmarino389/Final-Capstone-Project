import requests

def search_location(location):
  url = "https://api.content.tripadvisor.com/api/v1/location/search"
  headers = {'accept': 'application/json'}
  params = {'key': '6A2A0969ED22430DB68AB70E1E89FE91', 'searchQuery': location}
  response = requests.get(url, headers=headers, params = params)
  print(response.text)


def show_images(location_id):
 

  url = f"https://api.content.tripadvisor.com/api/v1/location/{location_id}/photos"
  headers = {'accept': 'application/json'}
  params = {'key': '6A2A0969ED22430DB68AB70E1E89FE91'}
  response = requests.get(url, headers=headers, params = params)
  print(response.text)


def location_description(location_id):
 

  url = f"https://api.content.tripadvisor.com/api/v1/location/{location_id}/details"
  headers = {'accept': 'application/json'}
  params = {'key': '6A2A0969ED22430DB68AB70E1E89FE91'}
  response = requests.get(url, headers=headers, params = params)
  print(response.text)



# search_location('Omaha')

# show_images('91516')

location_description(91516)