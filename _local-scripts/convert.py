import csv

# Define the input and output file names
input_file = 'register.csv'
output_file = 'register-insert.html'

# Read the CSV file and sort the entries by Surname
entries = []
with open(input_file, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    entries = list(reader)

# Sort entries by Surname
entries.sort(key=lambda x: x['Surname'])

# Write HTML to the output file
with open(output_file, mode='w', encoding='utf-8') as htmlfile:
#    htmlfile.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Register</title>\n</head>\n<body>\n')

    for entry in entries:
        full_name = f"{entry['First name']} {entry['Surname']}"
        affiliation = entry['Affiliation']
        email = entry['E-mail']
        personal_profile = entry['Web page (personal profile)']
        projects = [entry['Project website 1'], entry['Project website 2'], entry['Project website 3']]
        summary = entry['Short summary of research interests relevant to DELM']

        # Write HTML for each entry
        htmlfile.write(f'  <h2 class="mt-5">{full_name}</h2>\n')
        htmlfile.write(f'  <p>\n')
        htmlfile.write(f'    Affiliation: {affiliation}<br/>\n')
        htmlfile.write(f'    E-mail: <a href="mailto:{email}">{email}</a><br/>\n')
        if personal_profile:
            htmlfile.write(f'    Website: <a href="{personal_profile}">{personal_profile}</a>\n')
        htmlfile.write(f'  </p>\n')
        
        # Projects
        if any(projects):
            htmlfile.write(f'  <p>\n    Project(s): ')
            htmlfile.write(' | '.join(f'<a href="{project}" target="_blank">{project}</a>' for project in projects if project))
            htmlfile.write(f'  </p>\n')

        # Summary
        if summary:
            htmlfile.write(f'  <p>Interests: {summary}</p>\n')

#    htmlfile.write('</body>\n</html>\n')

print(f'HTML file "{output_file}" has been created.')
