# We importen onze libraries om requests naar de api te sturen 
from urllib.parse import urlencode
import requests

# Om met de API te kunnen communiceren hebben we eerst een token, client_id en client_secret nodig
# Dit is allemaal heel eenvoudig te vinden op Spotify developer
main_api = "https://accounts.spotify.com/api/token"
auth_response = requests.post(main_api, {
    'grant_type': 'client_credentials',
    'client_id': 'YOUR CLIENT ID',
    'client_secret': "YOUR CLIENT SECRET",
})

# Om met de API te kunnen communiseren moeten we een GET request sturen
access_token = auth_response.json()['access_token']
headers = dict(Authorization=f"Bearer {access_token}")

# We vragen aan de persoon die het script uitvoert welke arties ze willen opzoeken.
# Deze bewaren we in de variabele Artiest
Artiest = input("Artist to search for: ")

#base url van alle Spotify API endpoints
API_URL = "https://api.spotify.com/v1/"

# we maken een query die ons vertelt wat we willen terugkrijgen. Hierbij is q onze input
query = {
    "q": Artiest,
    "type": "artist",
    "limit": "7",
}

# Hier creeeren we onze request dus we plakken de base url + de search? en vervolgens onze querry
end_point = "search?"
api_response = requests.get(f"{API_URL}{end_point}{urlencode(query)}", headers=headers).json()

# Enkele waardes voor de layout te verbeteren 
popularity = "Popularity"
print('-' * 40 + " " + ("-" * 100) + " " + ("-" * len(popularity)))
print("Name" + (" " * 37) + "Genre" + (" " * 96) + popularity)

# Natuurlijk willen we alle Artiesten en niet enkel de eerste
# dus we gaan met een simpele for loop steeds de naam, het genre en de populariteit printen
for artists in api_response["artists"]["items"]:
    lengthgenres = (len(str(artists['genres'])))
    lenghtartist = len(artists['name'])


    officielelenght = 40 - lenghtartist + 1
    print(f"{artists['name']}" + (" " * officielelenght) + f"{artists['genres']}" + (" " * (101 - lengthgenres)) + f"{artists['popularity']}")
    
print('-' * 40 + " " + ("-" * 100) + " " + ("-" * len(popularity)))
