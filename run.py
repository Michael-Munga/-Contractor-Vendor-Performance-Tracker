#!/usr/bin/env python3

# from config.setup import Session
# from lib.models import Vendor, Project, Contract, PerformanceReview


# CRUD Operations 

# Vendors
def add_vendor():
    pass


def list_vendors():
    pass


def update_vendor():
    pass


def delete_vendor():
    pass


# Projects
def add_project():
    pass


def list_projects():
    pass


def update_project():
    pass


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
