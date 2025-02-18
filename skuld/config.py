import msgspec

class Config(msgspec.Struct):
    migration_dir: str

def load_config(config_path: str = "skuld.yml") -> Config:
    with open(config_path, "r") as f:
        config_data = f.read()
    return msgspec.yaml.decode(config_data, type=Config)