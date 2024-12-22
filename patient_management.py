def search(patients, search_disease):
    result = []
    for patient in patients:
        if search_disease in patient['Disease']:
            result.append(patient['Name'])
    if result:
        return f"Patients with {search_disease}: {', '.join(result)}"
    else:
        return None
search_disease = "Flu"
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
print(search(patients, search_disease))
