
# DonateAThing

A project that was part of the Portfolio Lab provided by CodersLab. The aim of the project is to create an app that would allow a person to donate different objects to charity institutions from the list. The project's aim is to work on one's Django and Javascript skills.


## Technology used
Python 3, Django, Bootstrap, Javascript, HTML, SQLite
## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
python manage.py runserver
```


## Tests

App has a set of tests to verify that all functionalities are running. The tests are divided into 2 separate files:

tests.py - tests all functionalities/views

tests_models_signin.py - tests the authorization/authentication as well as all models and it's option to create/update/delete

Example model test:

```bash
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
```
Example authentication tests:

```bash
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
```


## Contributing

Contributions are always welcome!

For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

