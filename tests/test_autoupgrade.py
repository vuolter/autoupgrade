from unittest import TestCase
#import autoupgrade
from autoupgrade import normalize_version
#import sys


#print sys.argv
#autoupgrade.AutoUpgrade("x").restart()

#autoupgrade.AutoUpgrade("pip").upgrade_if_needed()

#autoupgrade.AutoUpgrade("alsdhf").upgrade()
#autoupgrade.AutoUpgrade("pip").upgrade()

class TestFunctions(TestCase):
    
    def test_normalize(self):
        self.assertGreater(normalize_version('0.1.2'), normalize_version('0.1.1'))
        self.assertGreater(normalize_version('0.1.5A'), normalize_version('0.1.5'))
        self.assertGreater(normalize_version('0.10.0'), normalize_version('0.9.5'))
        self.assertGreater(normalize_version('1.2.3'), normalize_version('1.2'))
        self.assertGreater(normalize_version('1.2A.3'), normalize_version('1.2.3'))
        self.assertEqual(normalize_version('1.2.3'), normalize_version('1.2.3'))
