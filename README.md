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

![image](https://user-images.githubusercontent.com/91262442/210824695-7dbf412a-5a47-49c6-8d2d-ec46315ea199.png)

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


## OpenAPI Docs

![system-service-carodaems cloud okteto net_docs](https://user-images.githubusercontent.com/91262442/210825621-7aa85e05-07ae-4c71-b2a8-b08620c7281c.png)
![image](https://user-images.githubusercontent.com/91262442/210826013-1eb387ff-389c-44c9-9a80-b249012f8059.png)
![image](https://user-images.githubusercontent.com/91262442/210826063-533a414b-0d09-4641-a75d-29bda3728eea.png)
![image](https://user-images.githubusercontent.com/91262442/210826116-1124b5d8-2a58-472a-b7ba-53e05bf0c903.png)
![image](https://user-images.githubusercontent.com/91262442/210826145-76b1ceb8-b47c-42b9-b54e-4c4b011c21f0.png)
![image](https://user-images.githubusercontent.com/91262442/210826165-1669aaac-8f16-4466-af68-68a30066b614.png)


## Links

Hosted API: https://system-service-carodaems.cloud.okteto.net/
