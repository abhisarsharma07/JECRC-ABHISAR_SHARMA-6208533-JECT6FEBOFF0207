# Department-wise Patient Count System

class Solution:

    def department_patient_count(self, visits):
        dep_count = {}
        ## Write your code here & Don't forget to add return keyword
        for visit in visits:
            department = visit["department"]

            if department in dep_count:
                dep_count[department]+=1
            else:
                dep_count[department] =1

        max_department = None
        max_count= 0

        for department in dep_count:
            if dep_count[department]> max_count:
                max_count=dep_count[department]
                max_department = department

        return dep_count, max_department