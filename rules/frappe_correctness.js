
// ruleid: frappe-incorrect-debounce
frappe.utils.debounce(() => {}, 1000)();

const d = new frappe.ui.Dialog({
	fields: [],
	primary_action: function () {
		// ruleid: frappe-dialog-primary-action-get-values
		const data = d.get_values();
	},
});

const d2 = new frappe.ui.Dialog({
	fields: [],
	primary_action: () => {
		// ruleid: frappe-dialog-primary-action-get-values
		const args = d2.get_values()["allocation"];
	},
});

const d3 = new frappe.ui.Dialog({
	fields: [],
	// ok: frappe-dialog-primary-action-get-values
	primary_action: function (data) {
		console.log(data);
	},
});

dialog.set_primary_action(__("Save"), () => {
	// ruleid: frappe-dialog-primary-action-get-values
	save_quick_entry(frm, dialog.get_values());
});

this.dialog.set_primary_action(__("Save"), function () {
	// ruleid: frappe-dialog-primary-action-get-values
	me.dialog_data = me.dialog.get_values();
});

// ok: frappe-dialog-primary-action-get-values
dialog.set_primary_action(__("Save"), (values) => save_quick_entry(frm, values));

// ok: frappe-dialog-primary-action-get-values
const values = dialog.get_values();

const d4 = new frappe.ui.Dialog({
	fields: [
		{
			fieldname: "item_code",
			onchange: () => {
				// ok: frappe-dialog-primary-action-get-values
				const values = d4.get_values();
			},
		},
	],
	primary_action: function (data) {},
});

// ok: frappe-dialog-primary-action-get-values
dialog.set_primary_action(__("Save"), save.bind(null, dialog.get_values()));
