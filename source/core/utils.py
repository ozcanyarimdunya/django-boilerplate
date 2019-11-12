import os
import logging

logger = logging.getLogger('source')


class FolderUtils:
    @staticmethod
    def create_folder(path, exist_ok=True):
        """
        Utility for creating directory

        :param path: Folder path to create
        :param exist_ok: ensure if given folder exist so no need to re-create again, default: True
        :return:
        """
        os.makedirs(path, exist_ok=exist_ok)

    @classmethod
    def create_folders(cls, paths: (list, tuple), exist_ok=True):
        """
        Utility for creating directories

        :param paths: Folder paths to create
        :param exist_ok: ensure if given folder exist so no need to re-create again, default: True
        :return:
        """
        for path in paths:
            cls.create_folder(path, exist_ok)
