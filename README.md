# Treatment Summary Report: SSRS to PDF using Python
## Project Objective:
#### Treatment Summary Report is a document that physicians at this facility have to fill out after every round of treatment. Eversince the reconstruction of the facility's database, this report has 50,000+ records from patients undergoing mental health and addiction treatment. The system that the company uses ran into problems extracting PDF records of individual records. 
#### That's why this task of re-building the SSRS report and automate the export process is important.
## Attempts to use different tools:
#### As the report is built in SSRS, the most direct way to export the PDF files is through SSIS. But this approach is not feasible with a large amount of record, and it constantly ran into database access problems.
#### I decided to change the approach and use simple Python script to access the SSMS database to extract information to build and export record. The task is to export the 37,000+ report from 2013, excluding the test cases. I write some SQL script to achieve this goal and narrow down the number of files needed to be exported.
## Unexpected hold back:
#### Test case of exported documents has blank pages due to SSRS page structure. I write another script in Python to detect blank pages and remove them from the files.
