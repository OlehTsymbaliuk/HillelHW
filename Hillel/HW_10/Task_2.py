import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')

    with open('new.csv', 'w', newline='') as csv_new:
        field_names = ['email']
        csv_writer = csv.DictWriter(csv_new, fieldnames=field_names, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['first_name']
            del line['last_name']
            csv_writer.writerow(line)
