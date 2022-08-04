# Social eCards Backend

Production url: <https://sg-ecard-api.herokuapp.com>

The social e-cards application lets users sign up, create greeting cards, and follow each other. A user can see cards shown from newest to oldest: they can see a collection of their own cards, a collection of cards by users they follow, and a colletion of all cards.

This api serves two frontend applications. You can find the [documentation](https://github.com/Momentum-Team-13/social-e-cards-team-sugar-gliders-backend/blob/main/api.docs.md) for the endpoints in this repository.

Developers:

- Andres Alcocer
- Ryan Frenia

## Starting the app locally

Make sure you have python3 and pipenv installed

- Clone repository `git clone https://github.com/Momentum-Team-13/social-e-cards-team-sugar-gliders-backend.git`
- Activate virtual environment: `pipenv shell` (in project directory)
- `cd` into project directory and install package dependencies: `pipenv install`
- Create a `.env` file in `core/` directory. This app uses amazon sw3 buckets to store images. You will need to create one to input your credentials:

```text title="core/.env"
    USE_S3=True
    AWS_ACCESS_KEY_ID = your aws key
    AWS_SECRET_ACCESS_KEY = your aws secret
    AWS_STORAGE_BUCKET_NAME = aws storage bucket name
    AWS_S3_SIGNATURE_VERSION= your aws signature version
    AWS_S3_REGION_NAME= aws region ex (1-us-east)
    AWS_S3_FILE_OVERWRITE=False

```

- Run server locally: `python manage.py runserver`
