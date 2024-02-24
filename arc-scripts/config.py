import yaml


def load_config():
    ARC_PROPS = {}
    with open('resources/config.yml') as reader:
        try:
            ARC_PROPS = yaml.safe_load(reader)
        except Exception as e:
            print('Error while loading config.yml file')
    return ARC_PROPS


ARC_PROPS = load_config()
