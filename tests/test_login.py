import unittest

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test.client import Client

from fieldbook.models import FieldBookUser

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        #self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

        self.user = User();
        self.user.set_password('johnpassword');
        self.user.username = 'john';
        self.user.email = 'lennon@thebeatles.com';
        self.user.is_active = True;
        self.user.save();

        fbuserprofile = FieldBookUser();
        fbuserprofile.user = self.user;
        # saving the fieldbook key and password
        fbuserprofile.fieldbook_api_key = '';
        fbuserprofile.fieldbook_api_secret = '';
        fbuserprofile.fieldbook_book= '5927f40a47df4704000cd90d';
        fbuserprofile.save();

    def testLogin(self):
        print ">> testLogin"
        response = self.client.login(username='john', password='johnpassword')
        self.assertEqual(response, True)