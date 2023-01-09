import csv

employees = []

# Creates a list of employee dictionaries with their preferences added
with open("backend/app/data/Fall22.csv", "r") as file:
  csv_reader = csv.reader(file)
  for row in csv_reader:
    # Skip the header line
    if row[0] == "Time":
      break
    employee = {
      "name": row[1].strip() + ' ' + row[2].strip(),
      "semester": int(row[4]),
      "preferred_hours_amount": int(row[5]) if row[5].isdigit() else row[5],
      "preferred_hours_period": row[6].strip().split(";"),
      "preferred_hours_block": row[7].split(";"),
      
      "Monday 07:55-08:55": row[9],
      "Monday 08:55-09:55": row[10],
      "Monday 09:55-10:55": row[11],
      "Monday 10:55-11:55": row[12],
      "Monday 11:55-12:55": row[13],
      "Monday 12:55-13:55": row[14],
      "Monday 13:55-14:55": row[15],
      "Monday 14:55-16:00": row[16],
      "Monday 16:00-17:00": row[17],
      "Monday 17:00-18:00": row[18],
      "Monday 18:00-19:00": row[19],
      "Monday 19:00-20:00": row[20],

      "Tuesday 07:55-09:20": row[21],
      "Tuesday 09:20-10:45": row[22],
      "Tuesday 10:45-12:10": row[23],
      "Tuesday 12:10-13:05": row[24],
      "Tuesday 13:05-14:30": row[25],
      "Tuesday 14:30-17:20": row[26],
      "Tuesday 17:20-18:45": row[27],
      "Tuesday 18:45-18:00": row[28],
      
      "Wednesday 07:55-08:55": row[30],
      "Wednesday 08:55-09:55": row[31],
      "Wednesday 09:55-10:55": row[32],
      "Wednesday 10:55-11:55": row[33],
      "Wednesday 11:55-12:55": row[34],
      "Wednesday 12:55-13:55": row[35],
      "Wednesday 13:55-14:55": row[36],
      "Wednesday 14:55-16:00": row[37],
      "Wednesday 16:00-17:00": row[38],
      "Wednesday 17:00-18:00": row[39],
      "Wednesday 18:00-19:00": row[40],
      "Wednesday 19:00-20:00": row[41],

      "Thursday 07:55-09:20": row[42],
      "Thursday 09:20-10:45": row[43],
      "Thursday 10:45-12:10": row[44],
      "Thursday 12:10-13:05": row[45],
      "Thursday 13:05-14:30": row[46],
      "Thursday 14:30-17:20": row[47],
      "Thursday 17:20-18:45": row[48],
      "Thursday 18:45-18:00": row[49],

      "Friday 07:55-08:55": row[51],
      "Friday 08:55-09:55": row[52],
      "Friday 09:55-10:55": row[53],
      "Friday 10:55-11:55": row[54],
      "Friday 11:55-12:55": row[55],
      "Friday 12:55-13:55": row[56],
      "Friday 13:55-14:55": row[57],
      "Friday 14:55-16:00": row[58],
      "Friday 16:00-17:00": row[59],
      "Friday 17:00-18:00": row[60],
      "Friday 18:00-19:00": row[61],
      "Friday 19:00-20:00": row[62],

      "Saturday 11:55-12:55": row[63],
      "Saturday 12:55-13:55": row[64],
      "Saturday 13:55-14:55": row[65],
      "Saturday 14:55-15:55": row[66],
      "Saturday 15:55-16:55": row[67],
      "Saturday 16:55-17:55": row[68],
      "Saturday 17:55-18:55": row[69],
      "Saturday 18:55-20:00": row[70],

      "Sunday 11:55-12:55": row[71],
      "Sunday 12:55-13:55": row[72],
      "Sunday 13:55-14:55": row[73],
      "Sunday 14:55-15:55": row[74],
      "Sunday 15:55-16:55": row[75],
      "Sunday 16:55-17:55": row[76],
      "Sunday 17:55-18:55": row[77],
      "Sunday 18:55-20:00": row[78],
    }
    employees.append(employee)

for employee in employees:
  print(employee["Sunday 17:55-18:55"], employee["Sunday 18:55-20:00"])

# Assigns employees to available shifts considering employees' preferences and available restrictions
def create_schedule(employees, shifts):
  schedule = {}
  for shift in shifts:
    # sorts employees by "semester" in decreasing order
    sorted_employees = sorted(employees, key=lambda x: x["years"], reverse=True)
    # assigns a shift to an employee if all the restrictions and preferences have been satisfied
    for employee in sorted_employees:
      if employee_can_work_shift(employee, shift) and employee_wants_shift(employee, shift):
        assign_shift_to_employee(schedule, employee, shift)
        break
  return schedule


# Determines if an employee can work a shift by looking at the given restrictions
def employee_can_work_shift(employee, shift):
  # Check if employee's preferred hours amount and preferred hours period allow them to work the shift
  # Check if employee's total hours for the week do not go below 8 or above 20 after assigning the shift
  # Check if the shift's staff amount requirement is satisfied
  return True


# Determines if an employee can work a shift by looking at his/her preferences in the filled-out form
def employee_wants_shift(employee, shift):
  # Check if the employee's preferred hours block includes the shift's start and end times
  # Check if the shift is on a day that the employee wants to work
  return True

# Assigns a shift to an employee after all the restrictions and preferences have been met
def assign_shift_to_employee(schedule, employee, shift):
  # Add the shift to the employee's schedule
  # Update the employee's total hours for the week
  pass

shifts = [
  { "day": "Monday", "start": "07:55", "end": "08:55", "staff_amount": 2 },
  { "day": "Monday", "start": "08:55", "end": "09:55", "staff_amount": 2 },
  { "day": "Monday", "start": "09:55", "end": "10:55", "staff_amount": 3 },
  { "day": "Monday", "start": "10:55", "end": "11:55", "staff_amount": 3 },
  { "day": "Monday", "start": "11:55", "end": "12:55", "staff_amount": 4 },
  { "day": "Monday", "start": "12:55", "end": "13:55", "staff_amount": 4 },
  { "day": "Monday", "start": "13:55", "end": "14:55", "staff_amount": 4 },
  { "day": "Monday", "start": "14:55", "end": "16:00", "staff_amount": 3 },
  { "day": "Monday", "start": "16:00", "end": "17:00", "staff_amount": 3 },
  { "day": "Monday", "start": "17:00", "end": "18:00", "staff_amount": 2 },
  { "day": "Monday", "start": "18:00", "end": "19:00", "staff_amount": 2 },
  { "day": "Monday", "start": "19:00", "end": "20:00", "staff_amount": 2 },
  
  { "day": "Tuesday", "start": "07:55", "end": "09:20", "staff_amount": 2 },
  { "day": "Tuesday", "start": "09:20", "end": "10:45", "staff_amount": 3 },
  { "day": "Tuesday", "start": "10:45", "end": "12:10", "staff_amount": 3 },
  { "day": "Tuesday", "start": "12:10", "end": "13:05", "staff_amount": 4 },
  { "day": "Tuesday", "start": "13:05", "end": "14:30", "staff_amount": 4 },
  { "day": "Tuesday", "start": "14:30", "end": "17:20", "staff_amount": 4 },
  { "day": "Tuesday", "start": "17:20", "end": "18:45", "staff_amount": 2 },
  { "day": "Tuesday", "start": "18:45", "end": "20:00", "staff_amount": 2 },
  
  { "day": "Wednesday", "start": "07:55", "end": "08:55", "staff_amount": 2 },
  { "day": "Wednesday", "start": "08:55", "end": "09:55", "staff_amount": 2 },
  { "day": "Wednesday", "start": "09:55", "end": "10:55", "staff_amount": 3 },
  { "day": "Wednesday", "start": "10:55", "end": "11:55", "staff_amount": 3 },
  { "day": "Wednesday", "start": "11:55", "end": "12:55", "staff_amount": 4 },
  { "day": "Wednesday", "start": "12:55", "end": "13:55", "staff_amount": 4 },
  { "day": "Wednesday", "start": "13:55", "end": "14:55", "staff_amount": 4 },
  { "day": "Wednesday", "start": "14:55", "end": "16:00", "staff_amount": 3 },
  { "day": "Wednesday", "start": "16:00", "end": "17:00", "staff_amount": 3 },
  { "day": "Wednesday", "start": "17:00", "end": "18:00", "staff_amount": 2 },
  { "day": "Wednesday", "start": "18:00", "end": "19:00", "staff_amount": 2 },
  { "day": "Wednesday", "start": "19:00", "end": "20:00", "staff_amount": 2 },

  { "day": "Thursday", "start": "07:55", "end": "09:20", "staff_amount": 2 },
  { "day": "Thursday", "start": "09:20", "end": "10:45", "staff_amount": 3 },
  { "day": "Thursday", "start": "10:45", "end": "12:10", "staff_amount": 3 },
  { "day": "Thursday", "start": "12:10", "end": "13:05", "staff_amount": 4 },
  { "day": "Thursday", "start": "13:05", "end": "14:30", "staff_amount": 4 },
  { "day": "Thursday", "start": "14:30", "end": "17:20", "staff_amount": 4 },
  { "day": "Thursday", "start": "17:20", "end": "18:45", "staff_amount": 2 },
  { "day": "Thursday", "start": "18:45", "end": "20:00", "staff_amount": 2 },

  { "day": "Friday", "start": "07:55", "end": "08:55", "staff_amount": 2 },
  { "day": "Friday", "start": "08:55", "end": "09:55", "staff_amount": 2 },
  { "day": "Friday", "start": "09:55", "end": "10:55", "staff_amount": 3 },
  { "day": "Friday", "start": "10:55", "end": "11:55", "staff_amount": 3 },
  { "day": "Friday", "start": "11:55", "end": "12:55", "staff_amount": 4 },
  { "day": "Friday", "start": "12:55", "end": "13:55", "staff_amount": 4 },
  { "day": "Friday", "start": "13:55", "end": "14:55", "staff_amount": 4 },
  { "day": "Friday", "start": "14:55", "end": "16:00", "staff_amount": 3 },
  { "day": "Friday", "start": "16:00", "end": "17:00", "staff_amount": 3 },
  { "day": "Friday", "start": "17:00", "end": "18:00", "staff_amount": 2 },
  { "day": "Friday", "start": "18:00", "end": "19:00", "staff_amount": 2 },
  { "day": "Friday", "start": "19:00", "end": "20:00", "staff_amount": 2 },

  { "day": "Saturday", "start": "11:55", "end": "12:55", "staff_amount": 2 },
  { "day": "Saturday", "start": "12:55", "end": "13:55", "staff_amount": 2 },
  { "day": "Saturday", "start": "13:55", "end": "14:55", "staff_amount": 2 },
  { "day": "Saturday", "start": "14:55", "end": "16:00", "staff_amount": 2 },
  { "day": "Saturday", "start": "16:00", "end": "17:00", "staff_amount": 2 },
  { "day": "Saturday", "start": "17:00", "end": "18:00", "staff_amount": 2 },
  { "day": "Saturday", "start": "18:00", "end": "19:00", "staff_amount": 2 },
  { "day": "Saturday", "start": "19:00", "end": "20:00", "staff_amount": 2 },

  { "day": "Sunday", "start": "11:55", "end": "12:55", "staff_amount": 2 },
  { "day": "Sunday", "start": "12:55", "end": "13:55", "staff_amount": 2 },
  { "day": "Sunday", "start": "13:55", "end": "14:55", "staff_amount": 2 },
  { "day": "Sunday", "start": "14:55", "end": "16:00", "staff_amount": 2 },
  { "day": "Sunday", "start": "16:00", "end": "17:00", "staff_amount": 2 },
  { "day": "Sunday", "start": "17:00", "end": "18:00", "staff_amount": 2 },
  { "day": "Sunday", "start": "18:00", "end": "19:00", "staff_amount": 2 },
  { "day": "Sunday", "start": "19:00", "end": "20:00", "staff_amount": 2 },
]