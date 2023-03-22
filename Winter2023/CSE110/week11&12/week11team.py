max_salary = 0
min_salary = 999999999999
max_data = []
min_data = []

choice = input('Which job title should I analyze? ')
with open ('Winter2023/CSE110/hr_system.txt') as hr_file:
    for line in hr_file:
        line = line.strip()
        hr_data = line.split(" ")
        salary = int(hr_data[3])
        job_title = hr_data[2]
        if job_title == choice:
            if salary > max_salary:
                max_salary = salary
                max_data = hr_data
            if salary < min_salary:
                min_salary = salary
                min_data = hr_data

if max_salary != 0:
   print(f'The max salary for {choice} is ${max_salary} for employee {max_data[0]}.')
   print(f'The min salary for {choice} is ${min_salary} for employee {min_data[0]}.')
else:
    print(f'The job title {choice} does not exist in the dataset.')