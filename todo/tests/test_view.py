from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from todo.models import Task


class TaskListTest(APITestCase):
    def setUp(self):
        self.valores = {'title': 'tarea', 'completion': False}
   
    def test_can_list_task(self):
        response = self.client.get(reverse('todo-api-list'), self.valores)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TaskNewTest(APITestCase):
    def test_new_task(self):
        valores = {'title': 'tarea'}
        response = self.client.post(reverse('todo-api-new'), valores, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TaskDeleteTest(APITestCase):
    def setUp(self):
        self.valores = Task.objects.create(title= 'tarea')

    def test_delete_task(self):
        response = self.client.delete(reverse('todo-api-delete', args=['1']))
        self.assertEqual(response.content.decode("utf-8"), '"Tarea eliminada"')

class TaskUpdateTest(APITestCase):
    def setUp(self):
        self.valores = Task.objects.create(title= 'tarea2', date_posted='2021-02-02', completion=False)
        self.newvalores = {'title': 'tarea1'}
    def test_update_task(self):
        response = self.client.post(reverse('todo-api-update', args=['1']), self.newvalores)
        self.assertEqual(response.content.decode("utf-8"), '{"id":1,"title":"tarea1","date_posted":"2021-02-02T00:00:00Z","completion":false}')

