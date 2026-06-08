# Copyright (c) 2026, hemanth balaji and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AirplaneTicket(Document):

    def validate(self):
        self.validate_capacity()

    def validate_capacity(self):

        flight = frappe.get_doc(
            "Airplane Flight",
            self.flight
        )

        airplane = frappe.get_doc(
            "Airplane",
            flight.airplane
        )

        capacity = airplane.capacity

        booked = frappe.db.count(
            "Airplane Ticket",
            {
                "flight": self.flight
            }
        )

        if booked >= capacity:
            frappe.throw(
                "No seats available"
            )