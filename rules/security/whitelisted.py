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


@frappe.whitelist()
def commit_without_methods():
	frappe.db.set_value("ToDo", "x", "status", "Closed")
	# ruleid: whitelisted-side-effect-on-get
	frappe.db.commit()


@frappe.whitelist()
def enqueue_without_methods():
	# ruleid: whitelisted-side-effect-on-get
	frappe.enqueue("app.module.job", queue="long")


@frappe.whitelist()
def sendmail_without_methods():
	if True:
		# ruleid: whitelisted-side-effect-on-get
		frappe.sendmail(recipients=["a@example.com"], subject="Hi")


@frappe.whitelist()
def ddl_without_methods():
	# ruleid: whitelisted-side-effect-on-get
	frappe.db.add_index("ToDo", ["status"])


@frappe.whitelist(methods=["POST"])
def commit_with_methods():
	# ok: whitelisted-side-effect-on-get
	frappe.db.commit()


@frappe.whitelist(methods="POST")
def enqueue_with_methods():
	# ok: whitelisted-side-effect-on-get
	frappe.enqueue("app.module.job")


@frappe.whitelist()
def enqueue_after_commit_without_methods():
	# ok: whitelisted-side-effect-on-get
	frappe.enqueue("app.module.job", enqueue_after_commit=True)


@frappe.whitelist()
def enqueue_now_without_methods():
	# ruleid: whitelisted-side-effect-on-get
	frappe.enqueue("app.module.job", now=True, enqueue_after_commit=True)


@frappe.whitelist(methods=["GET"])
def commit_with_get():
	# ruleid: whitelisted-side-effect-on-get
	frappe.db.commit()


@frappe.whitelist(methods="GET")
def sendmail_with_get_string():
	# ruleid: whitelisted-side-effect-on-get
	frappe.sendmail(recipients=["a@example.com"], subject="Hi")


@frappe.whitelist(methods=["GET", "POST"])
def commit_with_get_and_post():
	# ruleid: whitelisted-side-effect-on-get
	frappe.db.commit()


@frappe.whitelist(methods=("PUT", "DELETE"))
def commit_with_unsafe_methods():
	# ok: whitelisted-side-effect-on-get
	frappe.db.commit()


def not_whitelisted():
	# ok: whitelisted-side-effect-on-get
	frappe.db.commit()


@frappe.whitelist()
def read_only():
	# ok: whitelisted-side-effect-on-get
	return frappe.db.get_value("ToDo", "x", "status")
