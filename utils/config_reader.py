import configparser
import os


def read_config_data_key(section, key, filename='/data/config.cfg'):
    parent_dir = os.getcwd()
    filepath = os.path.abspath(parent_dir + filename)
    cp = configparser.RawConfigParser(interpolation=configparser.ExtendedInterpolation())
    cp.read(filepath)
    return cp.get(section, key)


def read_config_data_all(section, filename='/data/config.cfg'):
    parent_dir = os.getcwd()
    filepath = os.path.abspath(parent_dir +  filename)
    _interpolation = configparser.ExtendedInterpolation()
    cp = configparser.RawConfigParser(interpolation=_interpolation)
    cp.read(filepath)
    data = {}
    for k, v in cp.items(section):
        data.setdefault(k, v)
    return data


if __name__ == '__main__':

    filename = '/../data/config.cfg'
    parent_dir = os.getcwd()
    filepath = os.path.abspath(parent_dir + filename)
    print(filepath)
    cp = configparser.RawConfigParser(interpolation=configparser.ExtendedInterpolation())
    cp.read(filepath)
    print(cp.get("SUB_URLS", "base_url"))
