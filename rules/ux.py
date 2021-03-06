import frappe
from frappe import msgprint, throw, _


# ruleid: frappe-missing-translate-function-python
throw("Error Occured")

# ruleid: frappe-missing-translate-function-python
frappe.throw("Error Occured")

# ruleid: frappe-missing-translate-function-python
frappe.msgprint("Useful message")

# ruleid: frappe-missing-translate-function-python
msgprint("Useful message")


# ok: frappe-missing-translate-function-python
translatedmessage = _("Hello")

# ok: frappe-missing-translate-function-python
throw(translatedmessage)

# ok: frappe-missing-translate-function-python
msgprint(translatedmessage)

# ok: frappe-missing-translate-function-python
msgprint(_("Helpful message"))

# ok: frappe-missing-translate-function-python
frappe.throw(_("Error occured"))

not_translated = "abc"

# ruleid: frappe-missing-translate-function-python
frappe.throw("Some Text" + not_translated + "More text")

# ok: frappe-missing-translate-function-python
frappe.throw(_("Some Text") + not_translated)

# ok: frappe-missing-translate-function-python
frappe.throw(_("Some Text") + not_translated, title=_("None"))

# ruleid: frappe-missing-translate-function-python
frappe.throw(_("Some Text"), title="Warning")

# ok: frappe-missing-translate-function-python
frappe.throw(_("Some Text"), title=_("Warning"))
