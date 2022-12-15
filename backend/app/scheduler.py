import random

def schedule_shifts():
  # Define the shifts that need to be scheduled
  shifts = [
    { "start": "09:00", "end": "17:00", "min_staff": 1 },
    { "start": "13:00", "end": "21:00", "min_staff": 2 },
    { "start": "17:00", "end": "01:00", "min_staff": 3 }
  ]

  # Define the employees and their availability
  employees = [
    { "name": "Alice", "availability": ["09:00", "13:00", "17:00"] },
    { "name": "Bob", "availability": ["09:00", "13:00", "17:00", "21:00"] },
    { "name": "Charlie", "availability": ["13:00", "17:00", "21:00"] }
  ]

  # Create an empty schedule
  schedule = {}

  # Loop through the shifts and try to find employees to staff them
  for shift in shifts:
    available_employees = []
    for employee in employees:
      if shift["start"] in employee["availability"]:
        available_employees.append(employee["name"])
    
    # If there are not enough employees available for the shift,
    # fill the remaining spots with random employees
    while len(available_employees) < shift["min_staff"]:
      available_employees.append(random.choice(employees)["name"])
    
    # Add the shift to the schedule with the selected employees
    schedule[shift["start"]] = available_employees

  # Print the schedule
  for shift, employees in schedule.items():
    return f"Shift starting at {shift}: {', '.join(employees)}"
