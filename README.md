# python-repos-standards

## usage

1. Add this repo as a submodule in your python repo (microservice or lirery):

```git
git submodule add https://github.com/RickyCode/python-repos-standards.git .standards/
```

2. Run the python script that syncs the required files:

```cmd
python .standards/sync.py
```

2. When doin changes on your python repo don't forget to update the submodule:

```cmd
git submodule update --remote
```

3. Sync again:

```cmd
python .standards/sync.py
```
