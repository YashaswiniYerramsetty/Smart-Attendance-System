import csv
from datetime import datetime
import random
import os

CSV_FILE = 'students.csv'

def get_students():
    students = []
    # Check if CSV exists
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['Name'].strip() != '':
                    students.append({'Name': row['Name'], 'ID': row['ID']})
        print(f"Loaded {len(students)} students from {CSV_FILE}")
    else:
        # Interactive input
        n = int(input("Enter number of students: "))
        print("Enter each student as: Name ID (e.g., Yashu 110)")
        for i in range(n):
            while True:
                entry = input(f"Student {i+1}: ").strip()
                if len(entry.split()) == 2:
                    name, student_id = entry.split()
                    students.append({'Name': name, 'ID': student_id})
                    break
                else:
                    print("Invalid format. Enter as: Name ID")
    return students

def mark_attendance(students):
    attendance_data = []
    for student in students:
        status = random.choice(['Present', 'Absent'])
        attendance_data.append({
            'Name': student['Name'],
            'ID': student['ID'],
            'Status': status,
            'Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    return attendance_data

def save_attendance(file_path, attendance_data):
    headers = ['Name', 'ID', 'Status', 'Date']
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(attendance_data)

def main():
    print("=== Smart Attendance System ===")
    students = get_students()
    attendance = mark_attendance(students)
    output_file = 'attendance.csv'
    save_attendance(output_file, attendance)
    print(f"\nAttendance recorded for {len(students)} students.")
    print(f"Saved in {output_file}")

if __name__ == "__main__":
    main()
    