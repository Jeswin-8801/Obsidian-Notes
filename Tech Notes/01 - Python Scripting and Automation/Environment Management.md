
Using `virtualenv`.

## Create Virtual Environment

```bash ln:False
$ python3 -m venv venv/
```

## Activate

```bash ln:False
$ source venv/bin/activate
(venv) $
```

## Install Packages

```bash ln:False
(venv) $ python -m pip install <package-name>
```

# Deactivate

```bash ln:False
(venv) $ deactivate
$
```

# Save to `requirements.txt`

```bash ln:False
$ python3 -m pip freeze > requirements.txt
```
