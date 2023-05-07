from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QPushButton
from PyQt5.QtGui import QFont

import numpy as np
from model import predictDisease


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window title and size
        self.setWindowTitle('Disease Predictor')
        self.setGeometry(100, 100, 400, 200)

        # Create the input labels and checkboxes
        self.symptoms = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of_urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_typhos', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic_patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze'
]
        self.input_checkboxes = []
        for i, label in enumerate(self.symptoms):
            checkbox = QCheckBox(label, self)
            checkbox.setFont(QFont('Arial', 12))
            checkbox.move(20, 20 + i * 30)
            self.input_checkboxes.append(checkbox)

        # Create the output label
        self.output_label = QLabel(self)
        self.output_label.setFont(QFont('Arial', 12))
        self.output_label.move(20, 120)

        # Create the "Run" button
        self.run_button = QPushButton(self)
        self.run_button.setText('Run')
        self.run_button.move(170, 160)
        self.run_button.clicked.connect(self.run_model)

    def run_model(self):
        input_data = []
        for checkbox in self.input_checkboxes:
            if checkbox.isChecked():
                input_data.append(1)
            else:
                input_data.append(0)
        input_data = np.array(input_data).reshape(1, -1)
        output_data = predictDisease(input_data)
        self.output_label.setText(f'Output: {output_data}')


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
