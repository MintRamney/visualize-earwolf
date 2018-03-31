from collections import defaultdict

class Show:
    def __init__(self, hosts, episodes):
        self.hosts = hosts
        self.episodes = episodes

class Guest:

    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.hosted_shows = []
        self.guested_shows = defaultdict()

    def print_shows_hosted(self):
        for show in self.hosted_shows:
            print(show)

    def print_guested_shows(self):
        for app in self.guested_shows:
            print(" {}: {}".format(app,self.guested_shows[app]))
            
    def __str__(self):
        return "\n".join([self.name + ": " + convert(self.url)])

    def __repr__(self):
        return "\n".join([self.name + ": " + convert(self.url)])

def convert(s):
  try:
    return str(s,encoding='utf8')
  except:
    return s