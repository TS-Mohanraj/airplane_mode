# Copyright (c) 2026, hemanth balaji and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AirplaneTicket(Document):

    def validate(self):
        self.validate_capacity()
        self.remove_duplicate_addons()
        self.calculate_total_amount()

         
    # def before_submit(self):
    #     # Prevent submission if the status is not 'Boarded'
    #     # Replace 'status' with your exact fieldname if it is different
    #     if self.status != "Boarded":
    #         frappe.throw(
    #             msg="Cannot submit Airplane Ticket! The status must be <b>Boarded</b> to submit this document.",
    #             title="Submission Blocked"
    #         )

    def remove_duplicate_addons(self):
        if not self.add_ons_item:
            return
        
        seen = set()
        unique_addons = []
        
        for item in self.add_ons_item:
            if item.item not in seen:
                seen.add(item.item)
                unique_addons.append(item)
        self.add_ons_item = unique_addons
           

    def calculate_total_amount(self):
    # Initialize addons total
        addons_total = 0

        # Change self.add_ons to self.add_ons_item
        if self.add_ons_item:
            for item in self.add_ons_item:
                addons_total += float(item.amount)  # Ensure amounts are floats
        # Calculate final total price
        flight_price = float(self.flight_price) if self.flight_price else 0
        self.total_amount = flight_price + addons_total


    # def calculate_total_amount(self):
    #     # Initialize total with the mandatory flight price
    #     total = float(self.flight_price or 0.0)
        
    #     # Add up all the amounts from the add_ons child table
    #     if self.add_ons:
    #         for item in self.add_ons:
    #             total += float(item.amount or 0.0)
                
    #     # Populate the final total amount field
    #     self.total_amount = total

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