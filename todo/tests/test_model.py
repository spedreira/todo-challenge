from django.test import TestCase, override_settings
from todo.models import Task


class TaskTestCase(TestCase):
    def setUp(self):
        with override_settings(USE_TZ=False):
            Task.objects.create(title='tarea',date_posted='2020-05-11', completion=False)
    
    def test_title(self):
        tarea = Task.objects.get(id=1)
        mock_title = tarea._meta.get_field('title').verbose_name
        self.assertEqual (mock_title, 'title')
    
    def test_title_length(self):
        tarea = Task.objects.get(id=1)
        mock_title_length = tarea._meta.get_field('title').max_length
        self.assertEqual (mock_title_length, 150)
    
    def test_date(self):
        tarea = Task.objects.get(id=1)
        mock_date = tarea._meta.get_field('date_posted').verbose_name
        self.assertEqual (mock_date, 'date posted')
    
    def test_completion(self):
        tarea = Task.objects.get(id=1)
        mock_completion = tarea._meta.get_field('completion').verbose_name
        self.assertEqual (mock_completion, 'completion')
    
    
    
    
    
    