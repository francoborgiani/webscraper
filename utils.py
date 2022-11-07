import re

is_well_formed_link = re.compile(r"^https?://.+/.+$")
is_root_path = re.compile(r"^/.+$")

def build_link(host, url):
  if is_well_formed_link.match(url):
    return url
  elif is_root_path.match(url):
    return f"{host}{url}"
  else:
    return f"{host}/{url}"