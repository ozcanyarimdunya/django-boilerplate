import shutil
import tempfile
from pathlib import Path

from django.test import TestCase

from source.core.utils import FolderUtils


class TestFolderUtils(TestCase):

    def setUp(self) -> None:
        self.tmp_dir = Path(tempfile.TemporaryDirectory().name)

    def tearDown(self) -> None:
        try:
            shutil.rmtree(self.tmp_dir)
        except Exception as ex:
            print(ex)

    def test_create_folder(self):
        new_dir = self.tmp_dir.joinpath('new')
        FolderUtils.create_folder(new_dir)
        self.assertTrue(
            self.tmp_dir.joinpath('new').is_dir()
        )

    def test_create_folder_exception(self):
        new_dir = self.tmp_dir.joinpath('c/d/e/f')
        FolderUtils.create_folder(new_dir)
        with self.assertRaises(FileExistsError):
            FolderUtils.create_folder(new_dir, exist_ok=False)

    def test_create_folders(self):
        new_dirs = [
            self.tmp_dir.joinpath('new1'),
            self.tmp_dir.joinpath('new2'),
            self.tmp_dir.joinpath('new3'),
        ]
        FolderUtils.create_folders(new_dirs)
        self.assertTrue(self.tmp_dir.joinpath('new1').is_dir())
        self.assertTrue(self.tmp_dir.joinpath('new2').is_dir())
        self.assertTrue(self.tmp_dir.joinpath('new2').is_dir())
