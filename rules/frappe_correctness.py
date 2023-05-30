import frappe
from frappe import _

from frappe.model.document import Document
from frappe.utils import cint


# ruleid: frappe-breaks-multitenancy
variable = frappe.db.get_value("ABC", "x", "y")

# ruleid: frappe-breaks-multitenancy
precision = cint(frappe.db.get_single_value("System Settings", "float_precision"))


# ruleid: frappe-breaks-multitenancy
items = list(frappe.get_all("Item"))

# ruleid: frappe-breaks-multitenancy
config = bool(frappe.local.conf.config)

# ruleid: frappe-breaks-multitenancy
lang = str(frappe.lang)

# ruleid: frappe-breaks-multitenancy
testing = bool(frappe.flags.in_test)


# ruleid: frappe-modifying-but-not-comitting
def on_submit(self):
	if self.value_of_goods == 0:
		frappe.throw(_('Value of goods cannot be 0'))
	self.status = 'Submitted'

	# ok: frappe-breaks-multitenancy
	variable = frappe.db.get_value("ABC", "x", "y")

	# ok: frappe-breaks-multitenancy
	items = list(frappe.get_all("Item"))

	# ok: frappe-breaks-multitenancy
	config = bool(frappe.local.conf.config)


class DocTyper(Document):
	# ruleid: frappe-breaks-multitenancy
	variable = frappe.db.get_value("ABC", "x", "y")

	def validate(self):
		# ok: frappe-breaks-multitenancy
		variable = frappe.db.get_value("ABC", "x", "y")

		# ok: frappe-breaks-multitenancy
		self.attr = frappe.db.get_value("ABC", "x", "y")

		# ok: frappe-breaks-multitenancy
		land = str(frappe.lang)

		# ok: frappe-breaks-multitenancy
		testing = bool(frappe.flags.in_test)



# ok: frappe-modifying-but-not-comitting
def on_submit(self):
	if self.value_of_goods == 0:
		frappe.throw(_('Value of goods cannot be 0'))
	self.status = 'Submitted'
	self.db_set('status', 'Submitted')

# ok: frappe-modifying-but-not-comitting
def on_submit(self):
	if self.value_of_goods == 0:
		frappe.throw(_('Value of goods cannot be 0'))
	x = "y"
	self.status = x
	self.db_set('status', x)


# ok: frappe-modifying-but-not-comitting
def on_submit(self):
	x = "y"
	self.status = x
	self.save()

# ruleid: frappe-modifying-but-not-comitting-other-method
class DoctypeClass(Document):
	def on_submit(self):
		self.good_method()
		self.tainted_method()

	def tainted_method(self):
		self.status = "uptate"


# ok: frappe-modifying-but-not-comitting-other-method
class DoctypeClass(Document):
	def on_submit(self):
		self.good_method()
		self.tainted_method()

	def tainted_method(self):
		self.status = "update"
		self.db_set("status", "update")

# ok: frappe-modifying-but-not-comitting-other-method
class DoctypeClass(Document):
	def on_submit(self):
		self.good_method()
		self.tainted_method()
		self.save()

	def tainted_method(self):
		self.status = "uptate"


# ruleid: frappe-query-debug-statement
frappe.db.get_value("DocType", "name", debug=True)

# ruleid: frappe-query-debug-statement
frappe.db.get_value("DocType", "name", debug=1)

# ruleid: frappe-overriding-local-proxies
frappe.db = Database()

# ok: frappe-overriding-local-proxies
frappe.local.flags = {}

def replace_request():
	# ruleid: frappe-overriding-local-proxies
	frappe.request = {}


def testing_something(self):
	# ruleid: frappe-single-value-type-safety
    duration = frappe.db.get_value("System Settings", None, "duration") or 24


def testing_something(self):
	# ok: frappe-single-value-type-safety
    duration = frappe.db.get_single_value("System Settings", "duration") or 24


# ruleid: frappe-after-save-controller-hook
class DoctypeNew(Document):
	def before_save(self):
		self.good_method()

	def after_save(self):
		self.bad_method()

# ok: frappe-after-save-controller-hook
class DoctypeNew(Document):
	def before_save(self):
		self.good_method()


def bad_queries():
	# ruleid: frappe-qb-incorrect-order-usage
	frappe.qb.from_("some table").select("*").orderby("somefield", frappe.qb.desc).run()

def good_query():
	# ok: frappe-qb-incorrect-order-usage
	frappe.qb.from_("some table").select("*").orderby("somefield", order=frappe.qb.desc).run()


def bad_cache():
	# ruleid: frappe-cache-breaks-multitenancy
	c = frappe.cache()
	c.set("blah", "bleh")
	# ruleid: frappe-cache-breaks-multitenancy
	frappe.cache().get("blah")

def good_cache():
	# ok: frappe-cache-breaks-multitenancy
	c = frappe.cache()
	c.set_value("blah", "bleh")
	# ok: frappe-cache-breaks-multitenancy
	frappe.cache().get_value("blah")



def ins():
	# ruleid: frappe-get-doc-for-creation
	a = frappe.get_doc(doctype="blah", name="why")
	a.x = "y"
	a.insert()

	# ruleid: frappe-get-doc-for-creation
	frappe.get_doc(doctype="blah", name="why").insert()


	# ok: frappe-get-doc-for-creation
	a = frappe.get_doc(doctype="blah", name="why")
	a.x = "y"
	a.save()  # save is fine
