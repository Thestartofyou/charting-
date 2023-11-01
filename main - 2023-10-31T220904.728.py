class Patient:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.vital_signs = {}
        self.symptoms = []
        self.medications = []
        self.assessments = []

    def record_vital_signs(self, vital_type, value):
        self.vital_signs[vital_type] = value

    def add_symptom(self, symptom):
        self.symptoms.append(symptom)

    def prescribe_medication(self, medication):
        self.medications.append(medication)

    def perform_assessment(self, assessment):
        self.assessments.append(assessment)

    def display_chart(self):
        print(f"Patient Chart for {self.name}")
        print(f"Age: {self.age}, Gender: {self.gender}")
        print("\nVital Signs:")
        for vital_type, value in self.vital_signs.items():
            print(f"{vital_type}: {value}")
        print("\nSymptoms:")
        for symptom in self.symptoms:
            print(symptom)
        print("\nMedications:")
        for medication in self.medications:
            print(medication)
        print("\nAssessments:")
        for assessment in self.assessments:
            print(assessment)

# Create a patient and record information
patient1 = Patient("John Doe", 35, "Male")
patient1.record_vital_signs("Temperature", "98.6°F")
patient1.record_vital_signs("Heart Rate", "75 bpm")
patient1.add_symptom("Fever")
patient1.prescribe_medication("Acetaminophen 500mg")
patient1.perform_assessment("General physical examination")

# Display the patient's chart
patient1.display_chart()

