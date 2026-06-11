class Config:
    pass

class DatabaseConfig(Config):
    def __init__(self):
        self.host = "localhost"
        self.user = "root"

config = DatabaseConfig()

print("Host:", config.host)
print("User:", config.user)