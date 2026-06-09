# Copyright (c) 2026, hemanth balaji and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
    def validate(self):
        # Auto-set Full Name before saving
        first_name = self.first_name or ""
        last_name = self.last_name or ""
        
        # Combine first and last name cleanly
        self.full_name = f"{first_name} {last_name}".strip()