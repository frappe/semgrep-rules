app_name = "test_app"

# ruleid: override-doctype-class
override_doctype_class = {"ToDo": "test_app.overrides.CustomToDo"}

# ruleid: override-doctype-class
override_doctype_class = {
	"User": ["test_app.overrides.CustomUser"],
}

# ok: override-doctype-class
override_whitelisted_methods = {"frappe.desk.doctype.event.event.get_events": "test_app.event.get_events"}

# ok: override-doctype-class
doc_events = {
	"ToDo": {
		"on_update": "test_app.todo.on_update",
	}
}


def build_hooks():
	# ok: override-doctype-class
	override_doctype_class = {"ToDo": "test_app.overrides.CustomToDo"}
	return override_doctype_class
