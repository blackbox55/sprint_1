import numpy as np

class Student():
    def __init__(self, iq, eq, career_path):
        self.iq = iq
        self.eq = eq
        self.career_path = career_path

    
    def doctor(self, iq):
        if iq >= 120:
            return 'Qualified to be a doctor without struggle!'
        else:
            return 'IQ must be 120 or above to pursue this path!'
        
    def teacher(self, iq):
        if iq <= 105:
            return 'Qualified to be a teacher'
        else:
            return 'IQ must be 105 or above to pursue this path!'

class BloomTechStudent(Student):
    def __init__(self, iq, eq, career_path, language):
      super().__init__(iq, eq, career_path)
      self.language = language


    def student_generator(self):
        iq = np.random.choice(range(60, 130, 2))
        eq =  np.random.choice(range(60, 130, 2))
        language = np.random.choice(['java', 'python', 'linux'])
        return f'A student with {iq}IQ, {eq}EQ, and is proficient in {language}\n'
student = BloomTechStudent(100, 90, 'Data Scientist', 'python')

student.student_generator()

students = []
for i in range(50):
  students.append(student.student_generator())