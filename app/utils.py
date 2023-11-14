import requests


def search_location(location):
    url = "https://api.content.tripadvisor.com/api/v1/location/search"
    headers = {'accept': 'application/json'}
    params = {'key': '6A2A0969ED22430DB68AB70E1E89FE91', 'searchQuery': location}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        
        # Check if the response status code is 200 (OK) before returning the data.
        if response.status_code == 200:
            return response.json()  # Return the JSON response data
        else:
            return {'error': f'An error occurred: {response.status_code}'}
            
    except requests.RequestException as e:
        # Handle any exceptions that occur during the HTTP request
        return {'error': str(e)}
    


# Remember to replace 'YOUR_API_KEY' with your actual API key, and ensure
# that you do not expose your API key in your source code.


import requests

import requests

def show_images(location_id):
    url = f"https://api.content.tripadvisor.com/api/v1/location/{location_id}/photos"
    headers = {'accept': 'application/json'}
    params = {'key': 'YOUR_API_KEY'}  # Replace 'YOUR_API_KEY' with your actual API key
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # This will raise an exception for HTTP errors
        
        # Check if 'data' key is in the JSON response
        json_response = response.json()
        if 'data' in json_response:
            return json_response
        else:
            return {'error': 'No data key in response'}
    
    except requests.RequestException as e:
        # Handle any exceptions that occur during the HTTP request
        return {'error': str(e)}


def location_description(location_id):
    url = f"https://api.content.tripadvisor.com/api/v1/location/{location_id}/details"
    headers = {'accept': 'application/json'}
    params = {'key': 'YOUR_API_KEY'}
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            # Return the JSON response data
            return response.json()
        else:
            # Return an error message with the status code
            return {'error': f'An error occurred: {response.status_code}'}
    except requests.RequestException as e:
        # Handle any exceptions that occur during the HTTP request
        return {'error': str(e)}




# print(search_location('Omaha'))

# # show_images('91516')

# # location_description(91516)








# {
#   "data": [
#     {
#       "location_id": "588680",
#       "name": "West Omaha/ NE Lincoln KOA",
#       "address_obj": {
#         "street1": "14601 Highway 6",
#         "street2": "",
#         "city": "Gretna",
#         "state": "Nebraska",
#         "country": "United States",
#         "postalcode": "68028-6308",
#         "address_string": "14601 Highway 6, Gretna, NE 68028-6308"
#       }
#     },
#     {
#       "location_id": "91533",
#       "name": "Super 8 by Wyndham Omaha NE",
#       "address_obj": {
#         "street1": "7111 Spring St",
#         "street2": "I 80 and 72nd St Exit 449",
#         "city": "Omaha",
#         "state": "Nebraska",
#         "country": "United States",
#         "postalcode": "68106-3577",
#         "address_string": "7111 Spring St I 80 and 72nd St Exit 449, Omaha, NE 68106-3577"
#       }
#     },
#     {
#       "location_id": "97574",
#       "name": "Days Inn & Suites by Wyndham Omaha NE",
#       "address_obj": {
#         "street1": "11515 Miracle Hills Dr",
#         "street2": "",
#         "city": "Omaha",
#         "state": "Nebraska",
#         "country": "United States",
#         "postalcode": "68154-4450",
#         "address_string": "11515 Miracle Hills Dr, Omaha, NE 68154-4450"
#       }
#     },
#     {
#       "location_id": "234653",
#       "name": "Super 8 by Wyndham Council Bluffs IA Omaha NE Area",
#       "address_obj": {
#         "street1": "2712 S 24th St",
#         "street2": "",
#         "city": "Council Bluffs",
#         "state": "Iowa",
#         "country": "United States",
#         "postalcode": "51501-6949",
#         "address_string": "2712 S 24th St, Council Bluffs, IA 51501-6949"
#       }
#     },
#     {
#       "location_id": "2095176",
#       "name": "Baymont Inn & Suites Omaha NE",
#       "address_obj": {
#         "street1": "3301 S 72nd St",
#         "street2": "I-80 at Exit 449",
#         "city": "Omaha",
#         "state": "Nebraska",
#         "country": "United States",
#         "postalcode": "68124-3567",
#         "address_string": "3301 S 72nd St I-80 at Exit 449, Omaha, NE 68124-3567"
#       }
#     },
#     {
#       "location_id": "60885",
#       "name": "Omaha",
#       "address_obj": {
#         "state": "Nebraska",
#         "country": "United States",
#         "address_string": "Omaha, NE"
#       }
#     },
#     {
#       "location_id": "4506487",
#       "name": "The Village Bar omaha ne",
#       "address_obj": {
#         "street1": "5700 S 77th St",
#         "city": "Ralston",
#         "state": "Nebraska",
#         "country": "United States",
#         "postalcode": "68127-4202",
#         "address_string": "5700 S 77th St, Ralston, NE 68127-4202"
#       }
#     },
#     {
#       "location_id": "91499",
#       "name": "Embassy Suites by Hilton Omaha Downtown Old Market",
#       "address_obj": {
#         "street1": "555 South 10th Street",
#         "street2": "",
#         "city": "Omaha",
#         "state": "Nebraska",
#         "country": "United States",
#         "postalcode": "68102",
#         "address_string": "555 South 10th Street, Omaha, NE 68102"
#       }
#     },
#     {
#       "location_id": "23063263",
#       "name": "The Farnam, Autograph Collection",
#       "address_obj": {
#         "street1": "1299 Farnam Street",
#         "city": "Omaha",
#         "state": "Nebraska",
#         "country": "United States",
#         "postalcode": "68102",
#         "address_string": "1299 Farnam Street, Omaha, NE 68102"
#       }
#     },
#     {
#       "location_id": "278564",
#       "name": "Lauritzen Gardens Omaha's Botanical Center",
#       "address_obj": {
#         "street1": "100 Bancroft St",
#         "street2": "",
#         "city": "Omaha",
#         "state": "Nebraska",
#         "country": "United States",
#         "postalcode": "68108-1752",
#         "address_string": "100 Bancroft St, Omaha, NE 68108-1752"
#       }
#     }
#   ]
# }



# #location details json

# {
#   "location_id": "278564",
#   "name": "Lauritzen Gardens Omaha's Botanical Center",
#   "web_url": "https://www.tripadvisor.com/Attraction_Review-g60885-d278564-Reviews-Lauritzen_Gardens_Omaha_s_Botanical_Center-Omaha_Nebraska.html?m=66827",
#   "address_obj": {
#     "street1": "100 Bancroft St",
#     "street2": "",
#     "city": "Omaha",
#     "state": "Nebraska",
#     "country": "United States",
#     "postalcode": "68108-1752",
#     "address_string": "100 Bancroft St, Omaha, NE 68108-1752"
#   },
#   "ancestors": [
#     {
#       "level": "City",
#       "name": "Omaha",
#       "location_id": "60885"
#     },
#     {
#       "abbrv": "NE",
#       "level": "State",
#       "name": "Nebraska",
#       "location_id": "28948"
#     },
#     {
#       "level": "Country",
#       "name": "United States",
#       "location_id": "191"
#     }
#   ],
#   "latitude": "41.23456",
#   "longitude": "-95.91642",
#   "timezone": "America/Chicago",
#   "email": "m.harter@omahabotanicalgardens.org",
#   "phone": "+1 402-346-4002",
#   "website": "http://www.omahabotanicalgardens.org/",
#   "write_review": "https://www.tripadvisor.com/UserReview-g60885-d278564-Lauritzen_Gardens_Omaha_s_Botanical_Center-Omaha_Nebraska.html?m=66827",
#   "ranking_data": {
#     "geo_location_id": "60885",
#     "ranking_string": "#5 of 120 things to do in Omaha",
#     "geo_location_name": "Omaha",
#     "ranking_out_of": "120",
#     "ranking": "5"
#   },
#   "rating": "4.5",
#   "rating_image_url": "https://www.tripadvisor.com/img/cdsi/img2/ratings/traveler/4.5-66827-5.svg",
#   "num_reviews": "1144",
#   "review_rating_count": {
#     "1": "6",
#     "2": "9",
#     "3": "65",
#     "4": "243",
#     "5": "821"
#   },
#   "photo_count": "824",
#   "see_all_photos": "https://www.tripadvisor.com/Attraction_Review-g60885-d278564-m66827-Reviews-Lauritzen_Gardens_Omaha_s_Botanical_Center-Omaha_Nebraska.html#photos",
#   "hours": {
#     "periods": [
#       {
#         "open": {
#           "day": 1,
#           "time": "0900"
#         },
#         "close": {
#           "day": 1,
#           "time": "1700"
#         }
#       },
#       {
#         "open": {
#           "day": 2,
#           "time": "0900"
#         },
#         "close": {
#           "day": 2,
#           "time": "1700"
#         }
#       },
#       {
#         "open": {
#           "day": 3,
#           "time": "0900"
#         },
#         "close": {
#           "day": 3,
#           "time": "1700"
#         }
#       },
#       {
#         "open": {
#           "day": 4,
#           "time": "0900"
#         },
#         "close": {
#           "day": 4,
#           "time": "1700"
#         }
#       },
#       {
#         "open": {
#           "day": 5,
#           "time": "0900"
#         },
#         "close": {
#           "day": 5,
#           "time": "1700"
#         }
#       },
#       {
#         "open": {
#           "day": 6,
#           "time": "0900"
#         },
#         "close": {
#           "day": 6,
#           "time": "1700"
#         }
#       },
#       {
#         "open": {
#           "day": 7,
#           "time": "0900"
#         },
#         "close": {
#           "day": 7,
#           "time": "1700"
#         }
#       }
#     ],
#     "weekday_text": [
#       "Monday: 09:00 - 17:00",
#       "Tuesday: 09:00 - 17:00",
#       "Wednesday: 09:00 - 17:00",
#       "Thursday: 09:00 - 17:00",
#       "Friday: 09:00 - 17:00",
#       "Saturday: 09:00 - 17:00",
#       "Sunday: 09:00 - 17:00"
#     ]
#   },
#   "category": {
#     "name": "attraction",
#     "localized_name": "Attraction"
#   },
#   "subcategory": [
#     {
#       "name": "nature_parks",
#       "localized_name": "Nature & Parks"
#     },
#     {
#       "name": "attractions",
#       "localized_name": "Attractions"
#     }
#   ],
#   "groups": [
#     {
#       "name": "Nature & Parks",
#       "localized_name": "Nature & Parks",
#       "categories": [
#         {
#           "name": "Gardens",
#           "localized_name": "Gardens"
#         }
#       ]
#     }
#   ],
#   "neighborhood_info": [],
#   "trip_types": [
#     {
#       "name": "business",
#       "localized_name": "Business",
#       "value": "24"
#     },
#     {
#       "name": "couples",
#       "localized_name": "Couples",
#       "value": "341"
#     },
#     {
#       "name": "solo",
#       "localized_name": "Solo travel",
#       "value": "58"
#     },
#     {
#       "name": "family",
#       "localized_name": "Family",
#       "value": "314"
#     },
#     {
#       "name": "friends",
#       "localized_name": "Friends getaway",
#       "value": "192"
#     }
#   ],
#   "awards": [
#     {
#       "award_type": "Travelers Choice",
#       "year": "2023",
#       "images": {
#         "tiny": "https://static.tacdn.com/img2/travelers_choice/widgets/tchotel_2023_L.png",
#         "small": "https://static.tacdn.com/img2/travelers_choice/widgets/tchotel_2023_L.png",
#         "large": "https://static.tacdn.com/img2/travelers_choice/widgets/tchotel_2023_L.png"
#       },
#       "categories": [],
#       "display_name": "Travelers Choice"
#     },
#     {
#       "award_type": "Travelers Choice",
#       "year": "2022",
#       "images": {
#         "tiny": "https://static.tacdn.com/img2/travelers_choice/widgets/tchotel_2022_L.png",
#         "small": "https://static.tacdn.com/img2/travelers_choice/widgets/tchotel_2022_L.png",
#         "large": "https://static.tacdn.com/img2/travelers_choice/widgets/tchotel_2022_L.png"
#       },
#       "categories": [],
#       "display_name": "Travelers Choice"
#     }
#   ]
# }




# # Show images json

# {
#   "data": [
#     {
#       "id": 197726676,
#       "is_blessed": false,
#       "caption": "Sculpture",
#       "published_date": "2016-06-29T23:55:21.403Z",
#       "images": {
#         "thumbnail": {
#           "height": 50,
#           "width": 50,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-t/0b/c9/11/d4/sculpture.jpg"
#         },
#         "small": {
#           "height": 150,
#           "width": 150,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-l/0b/c9/11/d4/sculpture.jpg"
#         },
#         "medium": {
#           "height": 188,
#           "width": 250,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-f/0b/c9/11/d4/sculpture.jpg"
#         },
#         "large": {
#           "height": 413,
#           "width": 550,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-s/0b/c9/11/d4/sculpture.jpg"
#         },
#         "original": {
#           "height": 1500,
#           "width": 2000,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-o/0b/c9/11/d4/sculpture.jpg"
#         }
#       },
#       "album": "Other",
#       "source": {
#         "name": "Traveler",
#         "localized_name": "Traveler"
#       },
#       "user": {
#         "username": "marycM7004JR"
#       }
#     },
#     {
#       "id": 1814361,
#       "is_blessed": false,
#       "caption": "Beautiful Blooms",
#       "published_date": "2007-02-23T05:00:00Z",
#       "images": {
#         "thumbnail": {
#           "height": 50,
#           "width": 50,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-t/00/1b/af/59/beautiful-blooms.jpg"
#         },
#         "small": {
#           "height": 150,
#           "width": 150,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-l/00/1b/af/59/beautiful-blooms.jpg"
#         },
#         "medium": {
#           "height": 171,
#           "width": 250,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-f/00/1b/af/59/beautiful-blooms.jpg"
#         },
#         "large": {
#           "height": 378,
#           "width": 550,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-s/00/1b/af/59/beautiful-blooms.jpg"
#         }
#       },
#       "album": "Other",
#       "source": {
#         "name": "Traveler",
#         "localized_name": "Traveler"
#       },
#       "user": {
#         "username": "birdlady07"
#       }
#     },
#     {
#       "id": 365030050,
#       "is_blessed": false,
#       "caption": "UP Trains at Lauritzen Gardens",
#       "published_date": "2018-12-17T16:35:51.253Z",
#       "images": {
#         "thumbnail": {
#           "height": 50,
#           "width": 50,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-t/15/c1/ea/a2/up-trains-at-lauritzen.jpg"
#         },
#         "small": {
#           "height": 150,
#           "width": 150,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-l/15/c1/ea/a2/up-trains-at-lauritzen.jpg"
#         },
#         "medium": {
#           "height": 166,
#           "width": 250,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-f/15/c1/ea/a2/up-trains-at-lauritzen.jpg"
#         },
#         "large": {
#           "height": 366,
#           "width": 550,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-s/15/c1/ea/a2/up-trains-at-lauritzen.jpg"
#         },
#         "original": {
#           "height": 851,
#           "width": 1280,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-m/1280/15/c1/ea/a2/up-trains-at-lauritzen.jpg"
#         }
#       },
#       "album": "Other",
#       "source": {
#         "name": "Traveler",
#         "localized_name": "Traveler"
#       },
#       "user": {
#         "username": "FreelyMi"
#       }
#     },
#     {
#       "id": 360413561,
#       "is_blessed": false,
#       "caption": "",
#       "published_date": "2018-11-23T14:08:44.614Z",
#       "images": {
#         "thumbnail": {
#           "height": 50,
#           "width": 50,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-t/15/7b/79/79/20181027-131622-largejpg.jpg"
#         },
#         "small": {
#           "height": 150,
#           "width": 150,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-l/15/7b/79/79/20181027-131622-largejpg.jpg"
#         },
#         "medium": {
#           "height": 141,
#           "width": 250,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-f/15/7b/79/79/20181027-131622-largejpg.jpg"
#         },
#         "large": {
#           "height": 309,
#           "width": 550,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-s/15/7b/79/79/20181027-131622-largejpg.jpg"
#         },
#         "original": {
#           "height": 720,
#           "width": 1280,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-m/1280/15/7b/79/79/20181027-131622-largejpg.jpg"
#         }
#       },
#       "album": "Other",
#       "source": {
#         "name": "Traveler",
#         "localized_name": "Traveler"
#       },
#       "user": {
#         "username": "ahlouetta"
#       }
#     },
#     {
#       "id": 359744169,
#       "is_blessed": false,
#       "caption": "Indoor Flowers",
#       "published_date": "2018-11-19T20:01:27.505Z",
#       "images": {
#         "thumbnail": {
#           "height": 50,
#           "width": 50,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-t/15/71/42/a9/indoor-flowers.jpg"
#         },
#         "small": {
#           "height": 150,
#           "width": 150,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-l/15/71/42/a9/indoor-flowers.jpg"
#         },
#         "medium": {
#           "height": 141,
#           "width": 250,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-f/15/71/42/a9/indoor-flowers.jpg"
#         },
#         "large": {
#           "height": 309,
#           "width": 550,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-s/15/71/42/a9/indoor-flowers.jpg"
#         },
#         "original": {
#           "height": 720,
#           "width": 1280,
#           "url": "https://media-cdn.tripadvisor.com/media/photo-m/1280/15/71/42/a9/indoor-flowers.jpg"
#         }
#       },
#       "album": "Other",
#       "source": {
#         "name": "Traveler",
#         "localized_name": "Traveler"
#       },
#       "user": {
#         "username": "bigdawgtraveler"
#       }
#     }
#   ]
# }