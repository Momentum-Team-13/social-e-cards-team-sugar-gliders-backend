# Greeting cards api endpoints

Base url for all endpoints:

- `<BASE_URL>`: `https://sg-ecard-api.herokuapp.com`

## Home

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
    <br />

## Following

- **Follow a user**

  - method: `POST`
  - url: `<BASE_URL>/followers/`
  - data: you need to set authorization header with the token as the value and send the user id in the request body (the id of the user to follow):
    - Example: `Authorization: Token b4eecdcb2731a4a1383ad2ae15a2eb2fd6a1ac3d`
    - JSON data in request body: `{ "following": 2 }`
  - response a user object:

    ```
      {
        "id": 15,
        "user_following": {
            "id": 1,
            "username": "test",
            "email": ""
        },
        "following": 1
      }
    ```

<br />

- **Get all followers for authenticated user**
  - method: `GET`
  - url: `<BASE_URL>/followers/`
  - data: you need to set authorization header with the token as the value
    - Example: `Authorization: Token b4eecdcb2731a4a1383ad2ae15a2eb2fd6a1ac3d`
  - response: an array of user objects:

```
          [
            {
              "id": 8,
              "user_following": {
                "id": 3,
                "username": "JohnSmith2",
                "email": ""
                },
              "following": 3
            },
            {
              "id": 13,
              "user_following": {
                "id": 4,
                "username": "Bob445",
                "email": ""
              },
              "following": 4
            },
            {
              "id": 15,
              "user_following": {
                  "id": 1,
                  "username": "Clare3x",
                  "email": ""
              },
                "following": 1
            }
          ]

```

  <br />

- **Remove a user from following list**

  - method: `DELETE`
  - url: `<BASE_URL>/followers/<ID>`
  - data: you need to set authorization header with the token as the value
    - Example: `Authorization: Token b4eecdcb2731a4a1383ad2ae15a2eb2fd6a1ac3d`
    - you must also specify the user id (to remove) in the url, example:
      - `<BASE_URL>/followers/3`
  - response: no response

  <br />

## Seeing and Creating Greeting Cards

- **View all greeting cards**
  - method: `GET`
  - url: `<BASE_URL>/ecards/`
  - data: you need to set authorization header with the token as the value
    - Example: `Authorization: Token b4eecdcb2731a4a1383ad2ae15a2eb2fd6a1ac3d`
  - response: an array of objects:

```
          [
            {
              "id": 1,
              "card_owner": {
                "id": 4,
                "username": "Bob",
                "email": ""
              },
              "created_at": "2022-07-28T19:47:27.045675Z",
              "updated_at": "2022-07-28T19:47:27.045712Z",
              "card_color_list": "#00FF00",
              "card_color": null,
              "card_inner_message": "test inner message",
              "card_outer_message": "test outer message",
              "card_image": "test card image",
              "card_owner": 1
            },
            {
              "id": 2,
              "card_owner": {
                "id": 2,
                "username": "Julian",
                "email": ""
              },
              "created_at": "2022-07-28T20:39:51.819332Z",
              "updated_at": "2022-07-28T20:39:51.819382Z",
              "card_color_list": "#00FF00",
              "card_color": null,
              "card_inner_message": "test inner message 2",
              "card_outer_message": "test outer message 2",
              "card_image": "test card image 2",
              "card_owner": 1
            }
          ]

```

  <br />

- **Create greeting card**
  - method: `POST`
  - url: `<BASE_URL>/ecards/`
  - data: you need to set authorization header with the token as the value
    - Example: `Authorization: Token b4eecdcb2731a4a1383ad2ae15a2eb2fd6a1ac3d`
    - JSON data in request body: `{ "card_inner_message": "test inner message", "card_outer_message": "test outer message", "card_image": "test card image"}`
  - response: 201 Created:

```
    {
      "id": 4,
      "card_owner": {
          "id": 4,
          "username": "Bob",
          "email": ""
      },
      "created_at": "2022-08-01T18:06:19.122274Z",
      "updated_at": "2022-08-01T18:06:19.122303Z",
      "card_color_list": "00FF00",
      "card_color": null,
      "card_inner_message": "inner message 5",
      "card_outer_message": "hello 5",
      "card_image": "image 5"
    }

```

  <br />

- **View only my greeting cards**
  - method: `GET`
  - url: `<BASE_URL>/ecards/me/`
  - data: you need to set authorization header with the token as the value
    - Example: `Authorization: Token b4eecdcb2731a4a1383ad2ae15a2eb2fd6a1ac3d`
  - response: an array of user objects:

```
        [
          {
            "id": 1,
            "created_at": "2022-07-28T19:47:27.045675Z",
            "updated_at": "2022-07-28T19:47:27.045712Z",
            "card_color_list": "#00FF00",
            "card_color": null,
            "card_inner_message": "test inner message",
            "card_outer_message": "test outer message",
            "card_image": "test card image",
            "card_owner": 1
          },
          {
            "id": 2,
            "created_at": "2022-07-28T20:39:51.819332Z",
            "updated_at": "2022-07-28T20:39:51.819382Z",
            "card_color_list": "#00FF00",
            "card_color": null,
            "card_inner_message": "test inner message 2",
            "card_outer_message": "test outer message 2",
            "card_image": "test card image 2",
            "card_owner": 1
          },
          {
            "id": 3,
            "created_at": "2022-07-28T21:42:30.175271Z",
            "updated_at": "2022-07-28T21:42:30.175310Z",
            "card_color_list": "00FF00",
            "card_color": null,
            "card_inner_message": "test inner message 2",
            "card_outer_message": "test outer message 2",
            "card_image": "test card image 2",
            "card_owner": 1
          }
        ]

```

  <br />

## Edit and Delete Greeting Cards

- **View only my selected greeting card**
  - method: `GET`
  - url: `<BASE_URL>/ecards/<int:pk`
  - data: you need to set authorization header with the token as the value
    - Example: `Authorization: Token b4eecdcb2731a4a1383ad2ae15a2eb2fd6a1ac3d`
  - response: an array of the objects for the particular card:

```
        [
          {
            "id": 3,
            "created_at": "2022-07-28T21:42:30.175271Z",
            "updated_at": "2022-07-28T21:42:30.175310Z",
            "card_color_list": "00FF00",
            "card_color": null,
            "card_inner_message": "test inner message 2",
            "card_outer_message": "test outer message 2",
            "card_image": "test card image 2",
            "card_owner": 1
          }
        ]

```

 <br />

- **Edit only my selected greeting card**
- method: `PATCH`
- url: `<BASE_URL>/ecards/<int:pk`
- data: you need to set authorization header with the token as the value
  - Example: `Authorization: Token b4eecdcb2731a4a1383ad2ae15a2eb2fd6a1ac3d`
- response: an updated array of the objects that were changed for the particular card:

```
  Example:

        Before PATCH (edit/udpate):
        [
          {
            "id": 3,
            "created_at": "2022-07-28T21:42:30.175271Z",
            "updated_at": "2022-07-28T21:42:30.175310Z",
            "card_color_list": "00FF00",
            "card_color": null,
            "card_inner_message": "test inner message 2",
            "card_outer_message": "test outer message 2",
            "card_image": "test card image 2",
            "card_owner": 1
          }
        ]

              Send PATCH Request

        After PATCH (edit/udpate):
        [
          {
            "id": 3,
            "created_at": "2022-07-28T21:42:30.175271Z",
            "updated_at": "2022-07-28T21:42:30.175310Z",
            "card_color_list": "00FF00",
            "card_color": null,
            "card_inner_message": "test inner message Patch",
            "card_outer_message": "test outer message Patch",
            "card_image": "test card image Patch",
            "card_owner": 1
          }
        ]

```

<br />

- **Delete only my selected greeting card**
- method: `DELETE`
- url: `<BASE_URL>/ecards/<int:pk`
- data: you need to set authorization header with the token as the value
  - Example: `Authorization: Token b4eecdcb2731a4a1383ad2ae15a2eb2fd6a1ac3d`
- response: No Response

  <br />

## View a List of Users

- method: `GET`
- url: `<BASE_URL>/users/`
- data: you need to set authorization header with the token as the value
  - Example: `Authorization: Token b4eecdcb2731a4a1383ad2ae15a2eb2fd6a1ac3d`
- response: an array of user objects:

```
        [
          {
            "id": 2,
            "username": "Testuser2",
            "email": ""
          },
          {
            "id": 1,
            "username": "user1",
            "email": "test@email.com"
          },
          {
            "id": 3,
            "username": "testuser3",
            "email": ""
          },
          {
            "id": 4,
            "username": "testuser4",
            "email": ""
          }
        ]

```
