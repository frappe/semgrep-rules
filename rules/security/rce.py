def function_name(input):
	# ruleid: frappe-codeinjection-eval
	eval(input)


def render(doc, path):
	# ruleid: frappe-ssti
	frappe.render_template(doc.template, doc.as_dict())
	# ruleid: frappe-ssti
	frappe.render_template(path, {})
	# ruleid: frappe-ssti
	frappe.render_template(doc.template, doc.as_dict(), restrict_globals=False)
	# ok: frappe-ssti
	frappe.render_template("templates/includes/address.html", doc.as_dict())
	# ok: frappe-ssti
	frappe.render_template(doc.template, doc.as_dict(), restrict_globals=True)
