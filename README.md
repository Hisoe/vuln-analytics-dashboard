# 📊 Enterprise Vulnerability Analytics & Executive Dashboard

## 📖 Overview

Security engineering is not just about finding vulnerabilities; it is about translating raw data into actionable business intelligence. This project demonstrates the ability to ingest a massive, 5,000-row enterprise vulnerability scan, separate the critical "signal" from the low-level "noise", and present it to executive leadership.

It features a custom-built Power BI Executive Dashboard and a strategic communication script designed to negotiate downtime with IT Operations without violating Service Level Agreements (SLAs).

## ✨ Key Features

Data Synthesis: A Python engine capable of generating realistic, enterprise-scale vulnerability datasets complete with randomized CVSS scores, compliance mappings, and SLA timelines.

Advanced Data Visualization (Power BI): Interactive dashboards utilizing custom DAX measures to isolate high-risk assets from thousands of background alerts.

Actionable Intelligence: A focused "Hit List" mapping the top 5 most vulnerable hosts to drive immediate IT remediation efforts.

Cross-Functional Communication: A structured negotiation script demonstrating empathy, business translation, and compensating controls (WAF) to secure patching windows with IT SysAdmins.

## 🗂️ Repository Structure
```text
├── generate_vuln_data.py       # Python script to generate the 5,000-row mock dataset
├── dashboard_screenshot.png    # Power BI Executive Dashboard visualization
├── Remediation_Call_Agenda.md  # SysAdmin negotiation and SLA protection script
└── README.md                   # Project documentation
```

## 🚀 Project Execution

1. Generating the Enterprise Dataset

To populate the dashboard, run the Python generator script to create a realistic `enterprise_vulnerability_scan.csv` file containing 5,000 unique records.

```text
python generate_vuln_data.py
```

2. The Executive Dashboard (Power BI)

The generated CSV was imported into Power BI. Key custom DAX measures were created to dynamically filter and calculate active threats, such as:

```text
Open_Critical_Vulns = CALCULATE(COUNT('enterprise_vulnerability_scan'[Scan_ID]), 'enterprise_vulnerability_scan'[Severity] = "Critical", 'enterprise_vulnerability_scan'[Status] = "Open")
```

Result: The dashboard successfully distills 5,000 alerts down to the specific Critical actions required, visualized by Severity, Compliance Framework (NIST/ISO/CIS), and Asset Name.

## 📊 Dashboard Preview

<img width="896" height="475" alt="dashboard_preview" src="https://github.com/user-attachments/assets/e2cb7de9-baed-41d2-ad65-372a8d034d26" />

## 🤝 The "Shift-Left" Communication Strategy

Vulnerability Management fails when Security and IT treat each other as adversaries. This repository includes `Remediation_Call_Agenda.md`, which outlines the exact script and negotiation strategy used to convince a System Administrator to patch a production server.

Core Strategy:

Empathy: Validate their 99.99% uptime metrics.

Translation: Explain the threat (e.g., active ransomware exploitation) in terms of business downtime, not just CVSS scores.

Collaboration: Offer flexible maintenance windows or temporary compensating controls (WAF rules) to protect SLAs during remediation.
