import os
import logging

logger = logging.getLogger('source')


def create_folders(*folders):
    """
    Utility for creating directories
    :param folders: directory names
    :return:
    """

    for folder in folders:
        os.makedirs(folder, exist_ok=True)
