import csv

shifts = [
  { "day": "Monday", "start": "07:55", "end": "08:55", "min_staff": 2 },
  { "day": "Monday", "start": "08:55", "end": "09:55", "min_staff": 2 },
  { "day": "Monday", "start": "09:55", "end": "10:55", "min_staff": 3 },
  { "day": "Monday", "start": "10:55", "end": "11:55", "min_staff": 3 },
  { "day": "Monday", "start": "11:55", "end": "12:55", "min_staff": 4 },
  { "day": "Monday", "start": "12:55", "end": "13:55", "min_staff": 4 },
  { "day": "Monday", "start": "13:55", "end": "14:55", "min_staff": 4 },
  { "day": "Monday", "start": "14:55", "end": "16:00", "min_staff": 3 },
  { "day": "Monday", "start": "16:00", "end": "17:00", "min_staff": 3 },
  { "day": "Monday", "start": "17:00", "end": "18:00", "min_staff": 2 },
  { "day": "Monday", "start": "18:00", "end": "19:00", "min_staff": 2 },
  { "day": "Monday", "start": "19:00", "end": "20:00", "min_staff": 2 },
  
  { "day": "Tuesday", "start": "07:55", "end": "09:20", "min_staff": 2 },
  { "day": "Tuesday", "start": "09:20", "end": "10:45", "min_staff": 3 },
  { "day": "Tuesday", "start": "10:45", "end": "12:10", "min_staff": 3 },
  { "day": "Tuesday", "start": "12:10", "end": "13:05", "min_staff": 4 },
  { "day": "Tuesday", "start": "13:05", "end": "14:30", "min_staff": 4 },
  { "day": "Tuesday", "start": "14:30", "end": "17:20", "min_staff": 4 },
  { "day": "Tuesday", "start": "17:20", "end": "18:45", "min_staff": 2 },
  { "day": "Tuesday", "start": "18:45", "end": "20:00", "min_staff": 2 },
  
  { "day": "Wednesday", "start": "07:55", "end": "08:55", "min_staff": 2 },
  { "day": "Wednesday", "start": "08:55", "end": "09:55", "min_staff": 2 },
  { "day": "Wednesday", "start": "09:55", "end": "10:55", "min_staff": 3 },
  { "day": "Wednesday", "start": "10:55", "end": "11:55", "min_staff": 3 },
  { "day": "Wednesday", "start": "11:55", "end": "12:55", "min_staff": 4 },
  { "day": "Wednesday", "start": "12:55", "end": "13:55", "min_staff": 4 },
  { "day": "Wednesday", "start": "13:55", "end": "14:55", "min_staff": 4 },
  { "day": "Wednesday", "start": "14:55", "end": "16:00", "min_staff": 3 },
  { "day": "Wednesday", "start": "16:00", "end": "17:00", "min_staff": 3 },
  { "day": "Wednesday", "start": "17:00", "end": "18:00", "min_staff": 2 },
  { "day": "Wednesday", "start": "18:00", "end": "19:00", "min_staff": 2 },
  { "day": "Wednesday", "start": "19:00", "end": "20:00", "min_staff": 2 },

  { "day": "Thursday", "start": "07:55", "end": "09:20", "min_staff": 2 },
  { "day": "Thursday", "start": "09:20", "end": "10:45", "min_staff": 3 },
  { "day": "Thursday", "start": "10:45", "end": "12:10", "min_staff": 3 },
  { "day": "Thursday", "start": "12:10", "end": "13:05", "min_staff": 4 },
  { "day": "Thursday", "start": "13:05", "end": "14:30", "min_staff": 4 },
  { "day": "Thursday", "start": "14:30", "end": "17:20", "min_staff": 4 },
  { "day": "Thursday", "start": "17:20", "end": "18:45", "min_staff": 2 },
  { "day": "Thursday", "start": "18:45", "end": "20:00", "min_staff": 2 },

  { "day": "Friday", "start": "07:55", "end": "08:55", "min_staff": 2 },
  { "day": "Friday", "start": "08:55", "end": "09:55", "min_staff": 2 },
  { "day": "Friday", "start": "09:55", "end": "10:55", "min_staff": 3 },
  { "day": "Friday", "start": "10:55", "end": "11:55", "min_staff": 3 },
  { "day": "Friday", "start": "11:55", "end": "12:55", "min_staff": 4 },
  { "day": "Friday", "start": "12:55", "end": "13:55", "min_staff": 4 },
  { "day": "Friday", "start": "13:55", "end": "14:55", "min_staff": 4 },
  { "day": "Friday", "start": "14:55", "end": "16:00", "min_staff": 3 },
  { "day": "Friday", "start": "16:00", "end": "17:00", "min_staff": 3 },
  { "day": "Friday", "start": "17:00", "end": "18:00", "min_staff": 2 },
  { "day": "Friday", "start": "18:00", "end": "19:00", "min_staff": 2 },
  { "day": "Friday", "start": "19:00", "end": "20:00", "min_staff": 2 },

  { "day": "Saturday", "start": "11:55", "end": "12:55", "min_staff": 2 },
  { "day": "Saturday", "start": "12:55", "end": "13:55", "min_staff": 2 },
  { "day": "Saturday", "start": "13:55", "end": "14:55", "min_staff": 2 },
  { "day": "Saturday", "start": "14:55", "end": "16:00", "min_staff": 2 },
  { "day": "Saturday", "start": "16:00", "end": "17:00", "min_staff": 2 },
  { "day": "Saturday", "start": "17:00", "end": "18:00", "min_staff": 2 },
  { "day": "Saturday", "start": "18:00", "end": "19:00", "min_staff": 2 },
  { "day": "Saturday", "start": "19:00", "end": "20:00", "min_staff": 2 },

  { "day": "Sunday", "start": "11:55", "end": "12:55", "min_staff": 2 },
  { "day": "Sunday", "start": "12:55", "end": "13:55", "min_staff": 2 },
  { "day": "Sunday", "start": "13:55", "end": "14:55", "min_staff": 2 },
  { "day": "Sunday", "start": "14:55", "end": "16:00", "min_staff": 2 },
  { "day": "Sunday", "start": "16:00", "end": "17:00", "min_staff": 2 },
  { "day": "Sunday", "start": "17:00", "end": "18:00", "min_staff": 2 },
  { "day": "Sunday", "start": "18:00", "end": "19:00", "min_staff": 2 },
  { "day": "Sunday", "start": "19:00", "end": "20:00", "min_staff": 2 },
]
employees = []

with open("backend/app/data/Fall22.csv", "r") as file:
  csv_reader = csv.reader(file)

  for row in csv_reader:
    if row[0] == "Time":
      break
    employee = {
      "name": row[1] + ' '.join(row[2]),
      "semesters": int(row[4]),
      "preferred_hours_amount": row[5],
      "preferred_hours_period": row[6],
      "preferred_hours_block": row[7],
    }
    employees.append(employee)
print(employees)