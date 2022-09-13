# Learning about APIs

From this website, [the right way to build an api with python](https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f)

### What APIs are and how they work
Application program interface
How we think about APIs
Acts as a gatekeeper between server and user

A script on a server
Most common API is a RESTful API
Representational state transfer


### 6 rules to ensure its restful

1. Single interface
    * Single entrypoint for us to communicate
2. Client server independace 
    * Acts as a middleman between server and client
    * If server updates, nothing should change in Api (should still work)
3. Statelessnes
    * second API requests shouldnt rely on previous request
    a. API doesnt change
4. Caching
    * Responses can be cached by the user
5. Layered systems
    * Modular =, one layer change does not change rest of API
6. Code on request
    * Should be able to execute the code on request
        * Rare


### Methods of interaction with Server
GET
	Retrieve info

POST
	Create resourse

PUT
	Update resource

DELETE
	Delete exisitng

PATCH
	Put for partial update but small
	
* Get is most common
* EG if we want GPS co-ords from maps API
	Get request is used
* Github API
	* Create/update/delete
	* Uses post/put/delete

#### API return codes
##### 2xx Sucess codes
200 ok
201 created
204 no content success but nothing retuned
##### 4xx Client error codes (our side)
400 bad request (request is wrong)
401 unauthorized (missed auth key)
403 forbidden (not allowed to access)
404 Not found (lost go home)



JSON format is used
Like a dict

Import requests

    response = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")
    response.json()['abilities'][0]['ability']['name']


## Example of get request using  mpas API
To get the location of the eifel tower

    res = requests.get(f"{API_URL}/json?address=Eifel+Tower&key={API_KEY}")

    res.json()['results'][0]['geometry']['location']


## Example of put request creating a repo in github
    PAYLOAD = {
    'name': 'api_test2',
    'public':'true'
    }
    from json import dumps
    res = requests.post(
        'https://api.github.com/user/repos',
        headers={'Authorization':f'token {GITHUB_KEY}'},
        data=json.dumps(PAYLOAD)
    )
    res.json()