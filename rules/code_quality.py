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


import frappe

doctypes = ["DocType A", "DocType B"]


# ruleid: unchecked-frappe-permission-call
frappe.has_permission("DocType", "read")

# ok: unchecked-frappe-permission-call
frappe.has_permission("DocType", "read", throw=True)

# ok: unchecked-frappe-permission-call
allowed = frappe.has_permission("DocType", "read")

# ok: unchecked-frappe-permission-call
if frappe.has_permission("DocType", "read"):
  pass

# ok: unchecked-frappe-permission-call
verdict = "yes" if frappe.has_permission("DocType", "read") else "no"

# ok: unchecked-frappe-permission-call
assert frappe.has_permission("DocType", "read")


def returns_permission():
  # ok: unchecked-frappe-permission-call
  return frappe.has_permission("DocType", "read")


# value used as a comprehension predicate — not a discarded call

# ok: unchecked-frappe-permission-call
permitted_list = [d for d in doctypes if frappe.has_permission(d, "read")]

# ok: unchecked-frappe-permission-call
permitted_negated = [d for d in doctypes if not frappe.has_permission(d, "read")]

# ok: unchecked-frappe-permission-call
permitted_set = {d for d in doctypes if frappe.has_permission(d, "read")}

# ok: unchecked-frappe-permission-call
permitted_map = {d: 1 for d in doctypes if frappe.has_permission(d, "read")}

# ok: unchecked-frappe-permission-call
has_any = any(d for d in doctypes if frappe.has_permission(d, "read"))
