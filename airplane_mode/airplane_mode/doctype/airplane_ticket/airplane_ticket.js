// Copyright (c) 2026, hemanth balaji and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
    refresh(frm) {

        frm.add_custom_button("Assign Seat", () => {

            let d = new frappe.ui.Dialog({
                title: "Assign Seat",
                fields: [
                    {
                        label: "Seat Number",
                        fieldname: "seat",
                        fieldtype: "Data",
                        reqd: 1
                    }
                ],

                primary_action(values) {

                    frm.set_value("seat", values.seat);

                    d.hide();
                },

                primary_action_label: "Assign"
            });

            d.show();

        });

    }
});