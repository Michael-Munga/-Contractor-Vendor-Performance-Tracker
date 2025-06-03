#!/usr/bin/env python3

from config.setup import Session
from lib.models import Vendor,Project
from datetime import date

session = Session()

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a valid number.")

def input_date(prompt):
    while True:
        try:
            return date.fromisoformat(input(prompt))
        except ValueError:
            print("Enter date as YYYY-MM-DD.")
# CRUD Operations 

# Vendors
def add_vendor():
    name = input("Vendor name: ")
    contact = input("Contact info: ")
    specialty = input("Specialty: ")
    try:
        vendor = Vendor(name=name, contact_info=contact,specialty=specialty)
        session.add(vendor)
        session.commit()
        print("vendor added succesfully.")
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
        

def list_vendors():
    try:
        vendors =session.query(Vendor).all()
        for v in vendors:
            print(f"ID: {v.id} | Name: {v.name} | Specialty: {v.specialty}")
    except Exception as e:
        print(f"Error: {e}")
        
def update_vendor():
    vendor_id =input_int("Vendor ID to update")
    try:
        vendor =session.get(Vendor,vendor_id)
        if not vendor:
            print("Vendor not found")
            return
        vendor.name = input(f"New name (current: {vendor.name}): ") or vendor.name
        vendor.contact_info = input(f"New contact info (current: {vendor.contact_info}): ") or vendor.contact_info
        vendor.specialty = input(f"New specialty (current: {vendor.specialty}): ") or vendor.specialty
        session.commit()
        print("Vendor updated.")
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
        

def delete_vendor():
    vendor_id = input_int("Vendor ID to delete: ")
    try:
        vendor = session.get(Vendor, vendor_id)
        if vendor:
            session.delete(vendor)
            session.commit()
            print("Vendor deleted.")
        else:
            print("Vendor not found.")
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()


# Projects
def add_project():
    name = input("Project name: ")
    start = input_date("Start date (YYYY-MM-DD): ")
    end = input_date("End date (YYYY-MM-DD): ")
    budget = float(input("Budget: "))
    try:
        project = Project(name=name, start_date=start, end_date=end, budget=budget)
        session.add(project)
        session.commit()
        print("Project added successfully.")
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
    


def list_projects():
    try:
        projects = session.query(Project).all()
        for p in projects:
            print(f"ID: {p.id} | {p.name} | Budget: {p.budget}")
    except Exception as e:
        print(f"Error: {e}")


def update_project():
    project_id = input_int("Project ID to update: ")
    try:
        project = session.get(Project, project_id)
        if not project:
            print("Project not found.")
            return
        project.name = input(f"New name (current: {project.name}): ") or project.name
        project.budget = float(input(f"New budget (current: {project.budget}): ") or project.budget)
        session.commit()
        print("Project updated.")
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()


# Contracts
def add_contract():
    pass


def list_contracts():
    pass


def update_contract_status():
    pass


def delete_contract():
    pass


# Reviews
def add_review():
    pass


def list_reviews():
    pass


def delete_review():
    pass


# CLI Menu 

def main():
    menu = {
        "1": add_vendor,
        "2": list_vendors,
        "3": update_vendor,
        "4": delete_vendor,
        "5": add_project,
        "6": list_projects,
        "7": update_project,
        "8": add_contract,
        "9": list_contracts,
        "10": update_contract_status,
        "11": delete_contract,
        "12": add_review,
        "13": list_reviews,
        "14": delete_review,
    }

    while True:
        print("\n--- Menu ---")
        print("1. Add Vendor")
        print("2. List Vendors")
        print("3. Update Vendor")
        print("4. Delete Vendor")
        print("5. Add Project")
        print("6. List Projects")
        print("7. Update Project")
        print("8. Add Contract")
        print("9. List Contracts")
        print("10. Update Contract Status")
        print("11. Delete Contract")
        print("12. Add Review")
        print("13. List Reviews")
        print("14. Delete Review")
        print("0. Exit")

        choice = input("Select option: ")
        if choice == "0":
            print("Goodbye!")
            break

        action = menu.get(choice)
        if action:
            action()
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
