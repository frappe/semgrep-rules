import frappe
from frappe import _

from frappe.model.document import Document
from frappe.utils import cint


# ruleid: frappe-breaks-multitenancy
variable = frappe.db.get_value("ABC", "x", "y")

# ruleid: frappe-breaks-multitenancy
precision = cint(frappe.db.get_single_value("System Settings", "float_precision"))


# ruleid: frappe-modifying-but-not-comitting
def on_submit(self):
	if self.value_of_goods == 0:
		frappe.throw(_('Value of goods cannot be 0'))
	self.status = 'Submitted'

	# ok: frappe-breaks-multitenancy
	variable = frappe.db.get_value("ABC", "x", "y")


class DocTyper(Document):
	# ruleid: frappe-breaks-multitenancy
	variable = frappe.db.get_value("ABC", "x", "y")

	def validate(self):
		# ok: frappe-breaks-multitenancy
		variable = frappe.db.get_value("ABC", "x", "y")

		# ok: frappe-breaks-multitenancy
		self.attr = frappe.db.get_value("ABC", "x", "y")



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
