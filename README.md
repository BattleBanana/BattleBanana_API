# BattleBanana API

## Introduction

This is the API for BattleBanana. This is mainly used for player transfer between BattleBanana and TheelUtil. It could eventually be used for other things as well such as voting and other things.

## Installation

### Requirements

- [Python 3.10+](https://www.python.org/downloads/)
- [MongoDB 6.0+](https://www.mongodb.com/download-center/community)*
- `pip install -r requirements.txt`

\* An older version of MongoDB could be supported, but there is no guarantee that it will work.

### Configuration

First thing you need to do, is rename the `sample.config.py` file to `config.py` and fill in the values.

- `DB_HOST`: The host of the MongoDB server.
- `DB_PORT`: The port of the MongoDB server (Default is 27017).
- `DB_USER`: The username of the MongoDB user.
- `DB_PWD`: The password of the MongoDB user.
- `DB_NAME`: The name of the MongoDB database.

Once that is done, you will need to create the MongoDB user. Make sure to replace `DB_USER` and `DB_PWD` with the values set above.

```bash
$ mongo
mongo> use admin
switched to db admin
mongo> db.createUser({user: "DB_USER", pwd: "DB_PWD", roles: [{role: "root", db: "admin"}]})
{ "ok" : 1 }
```

## Running the API

In development, you can run the API with the following command:

```bash
uvicorn main:app --reload
```

In production, you can use the following command:

```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```

You can change the host and port to whatever you want.
