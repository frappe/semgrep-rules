# ruleid:overusing-args
def function(args):
  args.updates = 1
  return args

# ok: overusing-args
def func(*args, **kwargs):
  acceptable = 1
  return acceptable

# ok: overusing-args
def func(*args):
  return 1



import unittest
from frappe.tests.utils import FrappeTestCase

# ruleid: use-frappetestcase
class MyTest(unittest.TestCase):
	def test_reality(self):
		self.assertEqual(1, 1)

# ok: use-frappetestcase
class MyTestGood(FrappeTestCase):
	def test_reality(self):
		self.assertNotEqual(1, 2)

# ruleid: frappetestcase-missing-super-call
class MyTestGood(FrappeTestCase):

	def test_reality(self):
		self.assertNotEqual(1, 2)

	@classmethod
	def setUpClass():
		pass


# ok: frappetestcase-missing-super-call
class MyTestGood(FrappeTestCase):

	def test_reality(self):
		self.assertNotEqual(1, 2)

	@classmethod
	def setUpClass():
		super().setUpClass()
		print("starting test")
