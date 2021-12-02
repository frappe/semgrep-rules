
// ok: frappe-missing-translate-function-js
frappe.msgprint('{{ _("Both login and password required") }}');

// ruleid: frappe-missing-translate-function-js
frappe.msgprint('What');

// ok: frappe-missing-translate-function-js
frappe.throw('  {{ _("Both login and password required") }}.  ');


// ruleid: frappe-missing-translation-button-text
frm.add_custom_button("Transfer Asset", function() {

})

// ok: frappe-missing-translation-button-text
frm.add_custom_button(__("Transfer Asset"), function() {

})

