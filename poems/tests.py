# Create your tests here.
from django.utils import unittest
from .models import Writer


class WriterTest(unittest.TestCase):
    def setUp(self):
        self.writer = Writer.objects.create(name='Fred', bio='my name is')

    def testWriter(self):
        self.assertEqual(self.writer.name, 'Fred')
        self.assertEqual(self.writer.bio, 'my name is')