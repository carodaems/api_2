# Song API

## Thema

Ik heb voor deze API besloten een volledig nieuw project te starten, met als thema muziek. Het concept is een zeer gesimplificeerde versie van wat bijvoorbeeld zou kunnen uitgroeien tot een trading platform voor uiterst zeldzame Albums. Dit besloot ik te doen om het bouwen van de API niet te ingewikkeld te maken, dus een album kan maar tot één gebruiker behoren. Het is dus als het ware een collectieplatform.

Muziek is een deel van mijn dagelijks leven, ik zou niet weten wat ik zonder moet. Daarom heb ik het ook gekozen als onderwerp. Dit leent zich ook om een API voor aan te maken.

## Endpoint werking

### GET

- /albums/{album_id}: returned een album a.d.h.v. een ID
- /albums: returned lijst met alle albums
- /genres: returned lijst met alle genres

### PUT

- /albums/{album_id}: update een album (volledige resource)

### POST

- /users: voeg een nieuwe user toe met een request body
- /albums: voeg een nieuw album toe met een request body
- /genres: voeg een nieuwe genre toe met een request body

### DELETE

- /albums/{album_id}: verwijder een album a.d.h.v. een ID

## Authenticatie



## Screenshots

### POST /albums
![image](https://user-images.githubusercontent.com/91262442/210816990-440d8e9c-17c8-4c19-9663-504394c386bd.png)

### POST /genres
![image](https://user-images.githubusercontent.com/91262442/210817897-d87c9fd6-7580-4914-937c-61bc20350594.png)

### POST /users
![image](https://user-images.githubusercontent.com/91262442/210818755-8e4bb152-250f-4e2d-b84b-0e7ee2bb8027.png)

### GET /albums/{album_id}
![image](https://user-images.githubusercontent.com/91262442/210819395-ebe17a4f-7827-40cf-8627-ddb995b78dc5.png)

### GET /albums
![image](https://user-images.githubusercontent.com/91262442/210819810-80d45d43-b058-42b4-9278-e043a40f8225.png)

### GET /genres
![image](https://user-images.githubusercontent.com/91262442/210819913-ddddfd3e-44b1-44dd-b2bf-fcb32c894ed6.png)

### PUT /albums/{album_id}
![image](https://user-images.githubusercontent.com/91262442/210820874-18b82f89-0c62-47bc-8bf6-bc5d362dd2e9.png)

### DELETE /albums/{album_id}
![image](https://user-images.githubusercontent.com/91262442/210821297-92315b4a-e2a5-4353-a5ac-fab69407d87c.png)


### OpenAPI Docs



## Links

Hosted API: https://system-service-carodaems.cloud.okteto.net/
