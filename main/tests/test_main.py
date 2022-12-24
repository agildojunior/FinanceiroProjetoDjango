from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from main.models import Categoria


class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="teste@gmail.com", username="teste"
        )
        self.user.set_password("12345")
        self.user.save()
        self.client = Client()
        self.client.login(username="teste", password="12345")
        self.user2 = User.objects.create_user(
            email="user123@gmail.com", username="user123"
        )
        self.user2.set_password("12345")
        self.user2.save()

    
    def test_cadastro_logged(self):
        response = self.client.get(reverse("cadastro"))
        self.assertEqual(response.status_code, 200)
    
    def test_login_logged(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_inicio_logged(self):
        response = self.client.get(reverse("inicio"))
        self.assertEqual(response.status_code, 200)

    def test_grafico_logged(self):
        response = self.client.get(reverse("grafico"))
        self.assertEqual(response.status_code, 200)
    
    def test_perfil_logged(self):
        response = self.client.get(reverse("perfil"))
        self.assertEqual(response.status_code, 200)

    def test_deslogar_logged(self):
        response = self.client.post(reverse("deslogar"),follow=True,)
        self.assertEqual(response.status_code, 200)

    def test_categoriaAdd_logged(self):
        request = {"categoria": "teste"}
        response = self.client.post(
            reverse("categoriaAdd"),
            request,
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_receitaAdd_logged(self):
        request = {"valor": 1,"descricao": "teste","categoria": 1}
        response = self.client.post(
            reverse("receitaAdd"),
            request,
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_despesaAdd_logged(self):
        request = {"valor": 1,"descricao": "teste","categoria": 1}
        response = self.client.post(
            reverse("despesaAdd"),
            request,
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_login2_logged(self):
        request = {"username": "teste","senha": "12345"}
        response = self.client.post(
            reverse("login"),
            request,
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
    
    def test_login3_logged(self):
        request = {"username": "naoexiste","senha": "12345"}
        response = self.client.post(
            reverse("login"),
            request,
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_cadastro2_logged(self):
        request = {"email":"teste123@gmail.com","username": "teste","senha": "12345"}
        response = self.client.post(
            reverse("cadastro"),
            request,
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_cadastro3_logged(self):
        request = {"email":"teste1234@gmail.com","username": "teste1234","senha": "123456789"}
        response = self.client.post(
            reverse("cadastro"),
            request,
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_senhaEdit_logged(self):
        request = {"senha": "12345"}
        response = self.client.post(
            reverse("senhaEdit"),
            request,
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_userEdit_logged(self):
        request = {"username": "teste","email": "teste@gmail.com"}
        response = self.client.post(
            reverse("userEdit"),
            request,
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_userEditParte2_logged(self):
        request = {"username": "user123","email": "user123@gmail.com"}
        response = self.client.post(
            reverse("userEdit"),
            request,
            follow=True,
        )
        self.assertEqual(response.status_code, 200)


        