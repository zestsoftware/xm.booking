import unittest

from zope.testing import doctest
from zope.testing import doctestunit
from zope.component import testing

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

OPTIONFLAGS = (doctest.ELLIPSIS |
               doctest.NORMALIZE_WHITESPACE)

@onsetup
def xm_setup():
    """Set up our Plone Site.
    """
    fiveconfigure.debug_mode = True
    import xm.booking
    zcml.load_config('configure.zcml', xm.booking)
    fiveconfigure.debug_mode = False

xm_setup()
ptc.setupPloneSite()

class TestCase(ptc.PloneTestCase):
    """Base test case.
    """
    pass
    

def test_suite():
    return unittest.TestSuite([

        doctestunit.DocTestSuite(
            module='xm.booking.browser.add',
            setUp=testing.setUp, tearDown=testing.tearDown),

        doctestunit.DocFileSuite(
            'tests.txt',
            optionflags=OPTIONFLAGS,
            package='xm.booking.timing')
        
        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
