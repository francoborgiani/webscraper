import yaml

__config = None

def config():

  global __config

  if not __config:
    # Read yaml file
    with open('config.yaml', mode="r") as f:
      # Transform yaml to a pyhton dictonary
      __config = yaml.load(f, Loader=yaml.Loader)

  return __config