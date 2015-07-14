from datetime import datetime

from django.contrib.sites.models import Site
from django.core.cache import cache
from django.test import TestCase

from visitor.models import Visitor

class BaseTestCase(TestCase):

    def tearDown(self):
        super(BaseTestCase,self).tearDown()
        cache.clear()

class VisitorModelTest(BaseTestCase):

    def test_create_visitor(self):

        count = Visitor.objects.count()
        visitor = Visitor.objects.create(
            visitor_key = 'abcdefg',
            last_session_key = 'hijklmnop'
        )
        visitor.save()
        self.assertTrue(count < Visitor.objects.count())

    def test_unicode_on_unsaved_visitor(self):
        # Given: An instance of Visitor that has not been saved to the db
        session_key = 'hijklmnop'
        visitor = Visitor(
            visitor_key = 'abcdefg',
            last_session_key = session_key
        )
        self.assertEqual(visitor.id, None)

        # When: calling the __unicode__ method on visitor
        result = unicode(visitor)

        # Then:  the expected result is returned
        expected_result = u'#None/{session_key}'.format(session_key=session_key)
        self.assertEqual(result, expected_result)

        # Then: the expected result is a unicode type object
        self.assertTrue(isinstance(result, unicode))

    def test_unicode_on_saved_visitor(self):
        # Given: An instance of Visitor that has not been saved to the db
        session_key = 'hijklmnop'
        visitor = Visitor(
            visitor_key = 'abcdefg',
            last_session_key = session_key
        )
        visitor.save()
        self.assertNotEqual(visitor.id, None)

        # When: calling the __unicode__ method on visitor
        result = unicode(visitor)

        # Then: the expected result is a unicode type object
        self.assertTrue(isinstance(result, unicode))

        # Then:  the expected result is returned
        expected_result = u'#{id}/{session_key}'.format(id=visitor.id, session_key=session_key)
        self.assertEqual(result, expected_result)



    """ test on possibly deprecated method
    def test_manager_create_from_ip(self):
        ip = '127.0.0.1'
        visitor = Visitor.objects.create_from_ip(ip)
        self.assertEquals(Visitor.objects.count(), 1)

        visitor = Visitor.objects.create_from_ip(ip)
        self.assertEquals(Visitor.objects.count(), 1)
    """
