from config.setup import Session
from lib.models import Vendor, Project, Contract, PerformanceReview
from datetime import date

session = Session()

# Clear Existing Data
session.query(PerformanceReview).delete()
session.query(Contract).delete()
session.query(Project).delete()
session.query(Vendor).delete()
session.commit()

#Add Vendors 
vendors = [
    Vendor(name="BuildSmart Ltd.", contact_info="info@buildsmart.com", specialty="Construction"),
    Vendor(name="GreenEnergy Co.", contact_info="contact@greenenergy.com", specialty="Renewable Energy"),
    Vendor(name="InfraCore Inc.", contact_info="hello@infracore.com", specialty="Infrastructure"),
    Vendor(name="SafeSecure", contact_info="support@safesecure.com", specialty="Security Systems"),
    Vendor(name="AquaTech", contact_info="sales@aquatech.com", specialty="Water Management"),
]
session.add_all(vendors)
session.commit()

# Add Projects 
projects = [
    Project(name="Downtown Revamp", start_date=date(2023, 1, 1), end_date=date(2023, 6, 30), budget=1000000.0),
    Project(name="Solar Farm Alpha", start_date=date(2023, 2, 15), end_date=date(2023, 9, 15), budget=750000.0),
    Project(name="City Surveillance", start_date=date(2023, 3, 10), end_date=date(2023, 10, 10), budget=500000.0),
    Project(name="Highway Extension", start_date=date(2023, 1, 20), end_date=date(2023, 12, 20), budget=2000000.0),
    Project(name="Smart Water Grid", start_date=date(2023, 4, 1), end_date=date(2023, 11, 1), budget=650000.0),
]
session.add_all(projects)
session.commit()

#Add Contracts 
contracts = [
    Contract(vendor=vendors[0], project=projects[0], contract_date=date(2023, 1, 5), amount=250000, status="Active"),
    Contract(vendor=vendors[1], project=projects[1], contract_date=date(2023, 2, 18), amount=300000, status="Pending"),
    Contract(vendor=vendors[2], project=projects[3], contract_date=date(2023, 1, 25), amount=750000, status="Active"),
    Contract(vendor=vendors[3], project=projects[2], contract_date=date(2023, 3, 15), amount=150000, status="Completed"),
    Contract(vendor=vendors[4], project=projects[4], contract_date=date(2023, 4, 5), amount=200000, status="Active"),
]
session.add_all(contracts)
session.commit()

# Add Performance Reviews 
reviews = [
    PerformanceReview(contract=contracts[0], review_date=date(2023, 6, 1), rating=4.5, remarks="Great execution."),
    PerformanceReview(contract=contracts[1], review_date=date(2023, 7, 1), rating=3.0, remarks="Delayed delivery."),
    PerformanceReview(contract=contracts[2], review_date=date(2023, 8, 10), rating=4.2, remarks="Met expectations."),
    PerformanceReview(contract=contracts[3], review_date=date(2023, 9, 20), rating=5.0, remarks="Exceeded expectations."),
    PerformanceReview(contract=contracts[4], review_date=date(2023, 10, 15), rating=3.8, remarks="Satisfactory."),
]
session.add_all(reviews)
session.commit()

print("Data Added successfully.")
