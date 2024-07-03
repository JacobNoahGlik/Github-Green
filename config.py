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

def revert_to_default(file: str = __CONFIG_FILE__) -> None:
    with open(file, 'w') as config:
        config.write(
            'key_file = "key.key"\n'
            'token_vault = "token.vault"\n'
            'name = "***** ****"\n'
            'email = "*******@gmail.com"\n'
            'local_repo_path = "./github_local"\n'
            'remote_url = "*******************************"\n'
            'logfile = "logfile"\n'
            'err = "errInfo.csv"\n'
        )

def default_key_filename(key_file: str | None = None, filename: str | None = None):
    configuration = get_config()
    if key_file is None:
        key_file = configuration['key_file']
    if filename is None:
        filename = configuration['token_vault']
    return key_file, filename

