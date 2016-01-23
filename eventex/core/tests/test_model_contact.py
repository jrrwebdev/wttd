from eventex.core.models import Speaker, Contact

from django.test import TestCase
from django.core.exceptions import ValidationError


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Rafael Henrique da Silva Correia',
            slug='rafael-henrique',
            photo='https://avatars2.githubusercontent.com/u/1902333?v=3&s=460',
        )

    def test_email(self):
        Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL,
                               value='rafael@abraseucodigo.com.br')
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        Contact.objects.create(speaker=self.speaker, kind=Contact.PHONE,
                               value='11-900001000')
        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind=Contact.EMAIL,
                          value='rafael@abraseucodigo.com.br')
        self.assertEqual('rafael@abraseucodigo.com.br',
                         str(contact))
