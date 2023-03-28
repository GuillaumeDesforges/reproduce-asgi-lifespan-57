Reproduce issue https://github.com/florimondmanca/asgi-lifespan/issues/57 and its resolution

```console
$ python -m venv .venv && source .venv/bin/activate
$ pip install -r requirements.txt
$ pytest -s > LOGS.txt
```

see [LOGS.txt](./LOGS.txt)
