# Cloaked Key

## Description

A standalone web service to securely storing secrets.

### API Interface

- set_secret(key, value) returns ->
  - success -> {key, value} stored successfully
  - fail -> if key already exists in store or any other issue occurs with storing
- get_secret(key) return ->
  - {key, value} -> key found, {key, value} retrieved successfully
  - fail -> key not found or some issue occurred during retrieval
- key_exists(key) return ->
  - yes -> key already exists
  - no -> key does not exist
  - fail -> some issue occurred

### Authentication and Authorization

- Other Services -> [Asymmetric JWT Auth](https://pypi.org/project/asymmetric-jwt-auth/)
- User -> [FastAPI JWT Auth](https://indominusbyte.github.io/fastapi-jwt-auth/)
