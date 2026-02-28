# Subject-wise Average Marks Calculator

class Solution:

    def subject_average(self, students):
        subject_total = {}
        subject_count = {}
        ## Write your code here and don't forget to add return keyword
        for student in students:
            for subject,marks in student["marks"].items():
                if subject in subject_total:
                    subject_total[subject]+= marks
                    subject_count[subject]+= 1
                else:
                    subject_total[subject] = marks
                    subject_count[subject] =1
                
        subject_avg={}
        for subject in subject_total:
            subject_avg[subject]=subject_total[subject]/subject_count[subject]

        highest_subject=None
        highest_avgg=0

        for subject in subject_avg:
            if subject_avg[subject]>highest_avgg:
                highest_avgg=subject_avg[subject]
                highest_subject=subject
        
        return subject_avg,highest_subject
