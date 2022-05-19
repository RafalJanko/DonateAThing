from django.test import Client
from django.urls import reverse
import pytest

# Create your tests here.

@pytest.mark.django_db
def test_menu_not_logged_in():
    client = Client()
    url = reverse('LandingPage')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_login_not_logged_in():
    client = Client()
    url = reverse('Login')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_register_not_logged_in():
    client = Client()
    url = reverse('Register')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_donation_logged_in(user):
    client = Client()
    client.force_login(user)
    response = client.get('/addDonnation')
    assert response.status_code == 301


@pytest.mark.django_db
def test_add_donation_not_logged_in():
    client = Client()
    url = 'addDonnation'
    response = client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db
def test_logout_while_logged_in(user):
    client = Client()
    client.force_login(user)
    response = client.get('/logout')
    assert response.status_code == 301


@pytest.mark.django_db
def test_logout_without_login():
    client = Client()
    url = 'Logout'
    response = client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db
def test_confirm_logged_in(user):
    client = Client()
    client.force_login(user)
    response = client.get('/confirmation')
    assert response.status_code == 301


@pytest.mark.django_db
def test_confirm_without_login():
    client = Client()
    url = 'Confirm'
    response = client.get(url)
    assert response.status_code == 404