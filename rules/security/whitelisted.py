from typing import Any
import frappe



# ruleid: missing-argument-type-hint
@frappe.whitelist()
def function_name(inject, abc):
	pass

# ok: missing-argument-type-hint
@frappe.whitelist()
def function_name(inject: str, abc: str):
	pass

# ok: missing-argument-type-hint
@frappe.whitelist()
def function_name():
	pass

# ok: missing-argument-type-hint
@frappe.whitelist()
def function_name(abc: Any):
	pass


# ruleid: missing-argument-type-hint
@frappe.whitelist()
def function_name(inject, abc: str): # only one typed
	pass
