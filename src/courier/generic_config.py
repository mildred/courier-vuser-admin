from os import path, listdir

def get_file_contents(filename):
  with open(filename) as f:
    return f.read()

def get_config_contents(config):
  if path.isdir(config):
    content = []
    for f in listdir(config):
      content.append(get_file_contents(path.join(config, f)))
    return "\n".join(content)
  else:
    return get_file_contents(config)
      
