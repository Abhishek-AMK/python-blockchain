**Activate the virtual environment**

```
source blockchain-env/Scripts/activate
```

**Install all packages**
```

pip install -r requirements.txt
```

**Run the tests**

Make sure to activate the virtual environment.

```
python -m pytest backend/tests
```

**Run the applications and API**

Make sure to activate the virtual environment

```

python -m backend.app
```

**Run a peer instance**

Make sure to activate the virtual environment.

```

export PEER=True && python -m backend.app
```

**Run the frontend**
```

npm run start
```