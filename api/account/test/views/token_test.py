from rest_framework import status
from account.models import User, Permission
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

class TestToken(APITestCase):
    GET_TOKEN_URL = '/api/v1/token/'
    GET_REGISTER_URL = '/api/v1/account/register/'
    REFRESH_TOKEN_URL = '/api/v1/token/refresh/'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.normal_permission = Permission(
            name="normal",
            description = "普通",
            is_can_open_admin = False,
            is_can_buy = True,
            is_can_sell = False,
            is_can_create_account_permission = False,
            is_can_delete_account_permission = False,
            is_can_delete_account = False,
        ).save()

        cls.admin_permission = Permission(
            name="admin",
            description="admin",
            is_can_open_admin=True,
            is_can_buy=True,
            is_can_sell=True,
            is_can_create_account_permission=True,
            is_can_delete_account_permission=True,
            is_can_delete_account=True,
        ).save()

        cls.user = User.objects.create_user(
            email='Tanaka@club.hekuta.net',
            username='admin',
            password='TESTAREA'
        )

    def test_normal_register(self):
        params_register = {
            'email': "TanakaSekai@club.hekuta.net",
            'username': "SubAdmin",
            'password': "TESTAREA",
            "checkPassword": "TESTAREA"
        }

        response = self.client.post(
            self.GET_REGISTER_URL,
            params_register,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_normal_login(self):
        params_login = {
            'email': "Tanaka@club.hekuta.net",
            'password': "TESTAREA"
        }

        response = self.client.post(
            self.GET_TOKEN_URL,
            params_login,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_force_login(self):
        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

    def test_refresh(self):
        token = str(RefreshToken.for_user(self.user).access_token)
        refresh_token = str(RefreshToken.for_user(self.user))
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

        params = {
            'refresh': refresh_token
        }

        response = self.client.post(
            self.REFRESH_TOKEN_URL,
            params,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
