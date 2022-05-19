import pytest
from django.contrib.auth.models import User
from charity_app.models import Category, Institution, Donation

'''
Fixtures for PyTest - used in the tests.py file to create "dummy" data.
Most of the fixtures compose of a single object and list of multiple objects, for testing purposes
'''

@pytest.fixture
def user():
    return User.objects.create_user(id=1, username="Janek", first_name="Jan", last_name="Kowalski",
                                    email="jankowalski@gmail.com", is_superuser=1)

@pytest.fixture
def category():
    return Category.objects.create_user(name="testname")

@pytest.fixture
def institution():
    return Institution.objects.create_user(name="testname", description="testdescription", type=1)

@pytest.fixture
def donation():
    return Donation.objects.create_user(quantity=2, address="testaddress", phone_number=123412323, city="testcity",
                                        zip_code=1234, pick_up_date="2022", pick_up_time="12:22:00",
                                        pick_up_comment="asd", institution_id=2)
