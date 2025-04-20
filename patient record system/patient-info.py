import json
import os

patients = []

# Load previous data if file exists
if os.path.exists("patients.json"):
    with open("patients.json", "r") as f:
        patients = json.load(f)

def show_menu():
    print("\n--- Patient Record Manager ---")
    print("1. Add New Patient")
    print("2. Search Patient by Name")
    print("3. View All Patients")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter patient name: ")
        age = input("Enter patient age: ")
        gender = input("Enter patient gender: ")
        symptoms = input("Enter symptoms: ")
        diagnosis = input("Enter diagnosis: ")

        patient = {
            "name": name,
            "age": age,
            "gender": gender,
            "symptoms": symptoms,
            "diagnosis": diagnosis
        }

        patients.append(patient)
        print("✅ Patient added successfully!")

    elif choice == "2":
        search_name = input("Enter patient name to search: ").lower()
        found = False

        for patient in patients:
            if patient["name"].lower() == search_name:
                print("\n✅ Patient Found:")
                print(f"Name     : {patient['name']}")
                print(f"Age      : {patient['age']}")
                print(f"Gender   : {patient['gender']}")
                print(f"Symptoms : {patient['symptoms']}")
                print(f"Diagnosis: {patient['diagnosis']}")
                found = True
                break

        if not found:
            print("❌ No patient found with that name.")

    elif choice == "3":
        if not patients:
            print("No patient records found.")
        else:
            print("\n--- All Patient Records ---")
            for idx, patient in enumerate(patients, start=1):
                print(f"\nPatient {idx}")
                print(f"Name     : {patient['name']}")
                print(f"Age      : {patient['age']}")
                print(f"Gender   : {patient['gender']}")
                print(f"Symptoms : {patient['symptoms']}")
                print(f"Diagnosis: {patient['diagnosis']}")

    elif choice == "4":
        with open("patients.json", "w") as f:
            json.dump(patients, f, indent=2)

        print("✅ Records saved to file. Exiting the program.")
        break
    else:
        print("Invalid choice. Try again.")


