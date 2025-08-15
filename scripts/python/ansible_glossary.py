from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

# Set up the document
doc = SimpleDocTemplate("Ansible_AAP_Glossary_and_Comparison.pdf", pagesize=A4)
styles = getSampleStyleSheet()
story = []

# Title
story.append(Paragraph("Ansible Automation Platform (AAP) Glossary & Comparison", styles['Title']))
story.append(Spacer(1, 12))

# Glossary data
glossary_data = [
    ["Component", "Description"],
    ["Automation Controller", "Web UI and API for managing automation; formerly Tower/AWX."],
    ["Automation Hub", "Central repository for certified Ansible content."],
    ["Automation Execution Environments", "Containerized runtimes for automation consistency."],
    ["Private Automation Hub", "Internal hub for hosting custom or certified content."],
    ["Automation Mesh", "Distributed job execution framework."],
    ["awx-cli", "CLI tool to manage the Automation Controller via API."],
    ["Content Collections", "Bundled content (roles, modules) curated by Red Hat and partners."],
    ["Analytics / Insights", "SaaS-based metrics and reporting for automation."],
    ["Credential Management", "Secure storage for SSH keys, tokens, cloud credentials, etc."],
    ["RBAC", "Role-based access control for users and teams."],
    ["Inventory", "Static or dynamic definitions of managed hosts."],
    ["Projects", "Git-based repositories of playbooks and automation content."],
    ["Job Templates", "Reusable job definitions with all required parameters."],
    ["Workflows", "Chained jobs with conditional logic."],
    ["Schedules", "Time-based triggers for job automation."],
    ["Notifications", "Alerts via email, Slack, or webhooks for job events."],
    ["Smart Inventory", "Filtered host groups using metadata or tags."],
    ["Survey", "User prompts for job runtime inputs."],
    ["Execution Nodes", "Remote execution endpoints in the mesh."],
    ["EDA Controller", "Event-driven automation controller."],
    ["Rulebook", "YAML-based logic for handling incoming events."],
    ["Event Source Plugin", "Defines event triggers like Kafka or webhooks."],
    ["Ansible Navigator", "CLI tool for local testing with execution environments."],
    ["Automation Catalog", "Portal or ITSM integration for self-service automation."],
    ["Content Signing", "Mechanism to verify the integrity and authenticity of content."]
]

table = Table(glossary_data, colWidths=[170, 360])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('GRID', (0, 0), (-1, -1), 0.25, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
]))
story.append(table)
story.append(PageBreak())

# Comparison table
story.append(Paragraph("ansible-core vs Ansible Automation Platform (AAP)", styles['Heading2']))
comparison_data = [
    ["Feature / Component", "ansible-core", "Ansible Automation Platform (AAP)"],
    ["Purpose", "Task execution engine", "Enterprise automation solution"],
    ["Playbooks & Modules", "Yes", "Yes"],
    ["CLI Tools", "Yes", "Yes + awx-cli, ansible-navigator"],
    ["Collections Support", "Yes", "Yes + certified content"],
    ["Execution Environments", "Optional", "Containerized & required"],
    ["Web UI", "No", "Yes (Automation Controller)"],
    ["RBAC", "No", "Yes"],
    ["Job Scheduling", "No", "Yes"],
    ["Logging & Auditing", "Limited", "Comprehensive"],
    ["Workflows", "No", "Yes"],
    ["Credential Management", "Manual", "Secure store + integrations"],
    ["Automation Mesh", "No", "Yes"],
    ["Content Hub", "No", "Yes (Private & Public)"],
    ["EDA", "No", "Yes"],
    ["Analytics", "No", "Yes"]
]
comp_table = Table(comparison_data, colWidths=[170, 160, 200])
comp_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('GRID', (0, 0), (-1, -1), 0.25, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
]))
story.append(comp_table)

# Build PDF
doc.build(story)
