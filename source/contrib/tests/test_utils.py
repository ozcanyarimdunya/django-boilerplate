import shutil
import tempfile
from pathlib import Path

from django.test import TestCase

from source.contrib.utils import create_folders


class TestFolderUtils(TestCase):

    def setUp(self) -> None:
        self.tmp_dir = Path(tempfile.TemporaryDirectory().name)

    def tearDown(self) -> None:
        try:
            shutil.rmtree(self.tmp_dir)
        except Exception as ex:
            print(ex)

    def test_create_folders(self):
        new_dir = self.tmp_dir.joinpath('new')
        create_folders(new_dir)
        self.assertTrue(
            self.tmp_dir.joinpath('new').is_dir()
        )

        new_dirs = [
            self.tmp_dir.joinpath('new1'),
            self.tmp_dir.joinpath('new2'),
            self.tmp_dir.joinpath('new3'),
        ]
        create_folders(*new_dirs)
        self.assertTrue(self.tmp_dir.joinpath('new1').is_dir())
        self.assertTrue(self.tmp_dir.joinpath('new2').is_dir())
        self.assertTrue(self.tmp_dir.joinpath('new2').is_dir())
