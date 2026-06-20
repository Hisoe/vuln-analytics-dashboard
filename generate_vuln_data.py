import csv
import random
from datetime import datetime, timedelta

# Mock Data Configurations
hostnames = [f"SRV-PRD-{i:03}" for i in range(1, 51)] + [f"WS-USER-{i:03}" for i in range(1, 101)]
severities = ["Critical", "High", "Medium", "Low"]
frameworks = ["NIST CSF", "ISO 27001", "CIS Controls", "None"]
statuses = ["Open", "Closed", "Risk Accepted"]

# Generate 5,000 rows of mock scanner data
with open('enterprise_vulnerability_scan.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Scan_ID", "Hostname", "Vulnerability_Name", "Severity", "CVSS_Score", "Discovered_Date", "SLA_Deadline", "Status", "Compliance_Mapping", "Days_Open"])
    
    for i in range(1, 5001):
        host = random.choice(hostnames)
        sev = random.choices(severities, weights=[5, 15, 30, 50])[0] # Mostly Low/Med, few Critical
        
        # Calculate Dates and SLAs
        disc_date = datetime.now() - timedelta(days=random.randint(1, 90))
        sla_days = {"Critical": 15, "High": 30, "Medium": 90, "Low": 180}[sev]
        sla_deadline = disc_date + timedelta(days=sla_days)
        
        status = random.choices(statuses, weights=[60, 35, 5])[0]
        days_open = (datetime.now() - disc_date).days if status == "Open" else 0
        
        cvss = round(random.uniform(9.0, 10.0), 1) if sev == "Critical" else \
               round(random.uniform(7.0, 8.9), 1) if sev == "High" else \
               round(random.uniform(4.0, 6.9), 1) if sev == "Medium" else \
               round(random.uniform(0.1, 3.9), 1)
               
        framework = random.choice(frameworks)
        
        writer.writerow([f"VULN-{i:05}", host, f"Sample CVE-{random.randint(2018,2023)}-{random.randint(1000,9999)}", sev, cvss, disc_date.strftime("%Y-%m-%d"), sla_deadline.strftime("%Y-%m-%d"), status, framework, days_open])

print("✅ Successfully generated enterprise_vulnerability_scan.csv with 5,000 records!")