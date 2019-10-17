import os
import logging

logger = logging.getLogger('liaoey')


def create_folder(path, exist_ok=True):
    """
    Utility for creating directory

    :param path: Folder path to create
    :param exist_ok: ensure if given folder exist so no need to re-create again, default: True
    :return:
    """
    try:
        os.makedirs(path, exist_ok=exist_ok)
    except Exception as ex:
        logger.exception(ex)


def create_folders(paths: (list, tuple), exist_ok=True):
    """
    Utility for creating directories

    :param paths: Folder paths to create
    :param exist_ok: ensure if given folder exist so no need to re-create again, default: True
    :return:
    """
    for path in paths:
        create_folder(path, exist_ok)
