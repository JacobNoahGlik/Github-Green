import os

__CONFIG_FILE__: str = "config"

def get_config(file: str = __CONFIG_FILE__) -> dict[str, str]:
    if not os.path.exists(file):
        revert_to_default(file=file)
    configuration = {}
    with open(file, 'r') as config:
        lines = config.read().split('\n')
    for line in lines:
        if len(line) < 5 or len(line.split('"')) != 3:
            continue
        key = line.split(' ')[0]
        configuration[key] = line.split('"')[1]
    return configuration


def update_config(file: str = __CONFIG_FILE__, configuration: dict[str, str] = {}) -> None:
    c = get_config(file=file)
    c.update(configuration)
    with open(file, 'w') as config:
        for key, value in c.items():
            config.write(f'{key}="{value}"\n')

