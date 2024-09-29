Course Registration System (CRS) - Python Tkinter Application
This is a Course Registration System (CRS) built using Python, Tkinter for the GUI, and MySQL for database management. The system allows users to manage student registrations, courses, and generate reports in PDF format. It includes login authentication, CRUD operations, and various functionalities such as PDF report generation using PollyReports and ReportLab.

Features
Login Authentication: Simple login system with predefined credentials (admin as username and 1234 as password).
Course Registration Management: Allows users to create, read, update, and delete student records, courses, and registrations.
PDF Report Generation: Generates PDF reports using ReportLab and PollyReports libraries.
Interactive GUI: User-friendly interface built using Tkinter.
Web Browsing: Opens reports or specific links in the web browser when required.
Requirements
To run this project, you need to install the following dependencies:

Python 3.x
Tkinter (pip install tk)
PyMySQL (pip install pymysql)
PollyReports (pip install pollyreports)
ReportLab (pip install reportlab)
You can install the dependencies by running:

Copy code
pip install tk pymysql pollyreports reportlab
Setup Instructions
Clone the repository (if applicable) or download the code.py file.

Set up the database:

You will need a MySQL server running with a database configured for the system.
Modify the database connection settings in code.py as needed (hostname, username, password).
Run the application:

Simply run code.py using Python
Copy code
python code.py

Login:
Use the following credentials to log in:
Username: admin
Password: 1234

Perform Operations:
Once logged in, you can manage course registrations, view records, and generate PDF reports.
File Structure
code.py: Main script containing the entire logic for the application.
Known Issues and Improvements
The system currently uses predefined login credentials; you may want to implement role-based access control (RBAC) for better security.
Report generation could be further enhanced by adding filtering options and advanced formatting.
