from django.test.testcases import TestCase
from core.models import Log, Entity


class TaskTest(TestCase):

    def test_create_entry(self):
        entity = Entity.objects.create(name="User Create Test")
        exists = Log.objects.filter(entity_key=entity.number, kind=Log.CREATE).exists()
        self.assertTrue(exists)

    def test_update_entry(self):
        entity = Entity.objects.create(name="User Update Test")

        entity = Entity.objects.get(number=entity.number)
        entity.name = "User Update Test [NEW]"
        entity.save()
        exists = Log.objects.filter(entity_key=entity.number, kind=Log.UPDATE).exists()
        self.assertTrue(exists)

    def test_delete_entry(self):
        entity = Entity.objects.create(name="User Delete Test")
        number = entity.number
        entity.delete()
        exists = Log.objects.filter(entity_key=number, kind=Log.DELETE).exists()
        self.assertTrue(exists)