import sys
import yaml
from pathlib import Path

def run():
    print(f'Import path: {sys.path}')
    config_file = Path(__file__).parent / 'config.yaml'
    with open(config_file, 'rt') as f:
        data = yaml.safe_load(f)

    print(f"Greetings from {data['name']}")
    print(f"Doing: {data['data']}")


if __name__ == '__main__':
    run()

