import datetime

from django.contrib.auth import authenticate, get_user_model
from django.test import TestCase, Client
from charity_app.models import Category, Institution, Donation, User


class SigninTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username="Janek", first_name="Jan", last_name="Kowalski",
                                    email="jankowalski@gmail.com")
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)


class CategoryModelTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(CategoryModelTestCase, cls).setUpClass()
        cls.category = Category(name="fundacja")
        cls.category.save()


class UserModelTestCase(CategoryModelTestCase):

    def test_created_properly(self):
        self.assertEqual(self.category.name, 'fundacja')

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.category.name, str)


class BaseInstitutionModelTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(BaseInstitutionModelTestCase, cls).setUpClass()
        cls.institution = Institution(name="testname", description="testdescription", type=1)
        cls.institution.save()


class InstitutionModelTestCase(BaseInstitutionModelTestCase):

    def test_created_properly(self):
        self.assertEqual(self.institution.name, 'testname')

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.institution.description, str)
        self.assertIsInstance(self.institution.type, int)


class BaseDonationModelTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(BaseDonationModelTestCase, cls).setUpClass()
        cls.donation = Donation(quantity=2, address="testaddress", phone_number=123412323, city="testcity",
                                        zip_code=1234, pick_up_date=datetime.date.today(), pick_up_time="12:22:00",
                                        pick_up_comment="asd", institution_id=1, user_id=1)
        cls.donation.save()
        cls.institution = Institution(name="testname", description="testdescription", type=1)
        cls.institution.save()
        cls.user = User(first_name="jan", last_name="kowalski", password="asd", email="asd@asd.com")
        cls.user.save()


class DonationModelTestCase(BaseDonationModelTestCase):

    def test_created_properly(self):
        self.assertEqual(self.donation.city, 'testcity')

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.donation.address, str)
        self.assertIsInstance(self.donation.phone_number, int)

    def test_it_has_date_fields(self):
        self.assertIsInstance(self.donation.pick_up_date, datetime.date)