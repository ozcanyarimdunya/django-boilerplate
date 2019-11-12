from django.db import connection, migrations, models, transaction
from django.db.models.base import ModelBase
from django.test import TestCase

from .models import BaseModel


class TestBaseModel(TestCase):
    model = BaseModel

    @classmethod
    def setUpClass(cls):
        cls.model = ModelBase(
            '__TestModel__', (cls.model,),
            {'__module__': cls.model.__module__}
        )

        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(cls.model)

    @classmethod
    def tearDownClass(cls):
        with connection.schema_editor() as schema_editor:
            schema_editor.delete_model(cls.model)

    def test_base(self):
        self.model.objects.create()
        self.assertEqual(self.model.objects.count(), 1)
