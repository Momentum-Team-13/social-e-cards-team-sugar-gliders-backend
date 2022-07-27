# Greeting cards api endpoints

Base url for all endpoints:

- `<BASE_URL>`: `https://sg-ecard-api.herokuapp.com`

## Home page

Get's you a free meme to lift your spirit whenever you're feeling down 😌

- method: `GET`
- url: `<BASE_URL>`
- response: an abject that contains a random Meme:

```
{
  "team": "Team Sugar Gliders",
  "description": "We got this team 😎, if you\"re feeling
      down there\"s a link here where you can see a funny Meme.
      Use it to lift your spirit.",
  "dank_meme_image": "https://i.redd.it/hsx65uf65yd91.jpg"
}
```

<br />

## User Authentication

- **Create user**

  - method: `POST`
  - url: `<BASE_URL>/auth/users/`
  - data: json object `{ "username": "yourusername", "password": "yourpassword" }`
  - response: will be a user object
    `{ "email": "", "username": "test", "id": 1 }`
    <br />

- **Login**

  - method: `POST`
  - url: `<BASE_URL>/auth/token/login/`
  - data: json object `{ "username": "yourusername", "password": "yourpassword" }`
  - response: will be a token: `{ "auth_token": "b4eecdcb2731a4a1383ad2ae15a2eb2fd6a1ac3d" }`
    <br />

- **Logout**

  - method: `POST`
  - url: `<BASE_URL>/auth/token/logout/`
  - data: you need to set authorization header with the token as the value, make sure you have a space after "Token":
    - Example: `Authorization: Token b4eecdcb2731a4a1383ad2ae15a2eb2fd6a1ac3d`
    - `<YOUR TOKEN>` is a long string you get back from the login endpoint
    - `Authorization: Token <YOUR TOKEN>`
  - response: will be empty (no data)
    <br />

- **Get user details**

  - method: `GET`
  - url: `<BASE_URL>/auth/users/me/`
  - data: you need to set authorization header with the token as the value, make sure you have a space after "Token":
    - Example: `Authorization: Token b4eecdcb2731a4a1383ad2ae15a2eb2fd6a1ac3d`
    - `<YOUR TOKEN>` is a long string you get back from the login endpoint
    - `Authorization: Token <YOUR TOKEN>`
  - response: will be a user object: `{ "email": "test@email.com", "id": 1, "username": "test" }`
