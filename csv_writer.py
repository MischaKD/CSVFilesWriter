import csv

# with open('students.csv', 'w') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['First name', 'Last Name', 'Age'])
#     csv_writer.writerow(['Jack', 'White', 24])
#     csv_writer.writerow(['Jane', 'Black', 23])

# with open('cars.csv') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     make_model_list = []
#     for car in csv_reader:
#         make_model = [car[1], car[2]]
#         make_model_list.append(make_model)
#     print(make_model_list)
#
# with open('cars_make_model.csv', 'w') as file:
#     csv_writer = csv.writer(file)
#     for row in make_model_list:
#         csv_writer.writerow(row)


with open('cars.csv') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    # make_model_list = []
    with open('cars_make_model.csv', 'w') as file:
        csv_writer = csv.writer(file)
        for row in csv_reader:
            csv_writer.writerow([row[1], row[2]])


