from Course import Course

class LearningManagementSystem:
    
    def __init__(self) -> None:
        self.courses = {} # key: course_offering_id, value: Course object
        self.allotment_done = False 
    
    def get_course(self, course_offering_id):
        return self.courses[course_offering_id]
    
    def get_all_courses(self):
        for _,course in self.courses.items():
            print(course.get_course_offering_id())
    
    def add_course_offering(self, course_name, instructor, date_in_ddmmyyyy, min_employees, max_employees) -> None:
        new_course = Course(course_name, instructor, date_in_ddmmyyyy, min_employees, max_employees)
        self.courses[new_course.course_offering_id] = new_course
        output = new_course.course_offering_id
        return output
        
    def register(self, email_id, course_offering_id) -> str:
        """Registers employee for course.
    
        The combination of email-id and course-offering-id in the input should be unique 
        
        The format of course-registration-id is REG-COURSE-<EMPLOYEE-NAME>-<COURSE-NAME> 
        
        If number of employees has not exceeded the maximum number of employees allowed for the course offering, course.status will be ACCEPTED 
        
        If number of employees has exceeded the maximum number of employees allowed for the course offering, course.status will be COURSE_FULL_ERROR 
        
        If the minimum number of employees for the course offering is not reached before the course date, the course.status of the course offering would be COURSE_CANCELED 
        
        Course-registration-id will only be returned if the course.status is ACCEPTED  
        
        Parameters
        ----------
        email-id: str 
        course-offering-id: str
        
        Returns
        -------
        output: str
        
        Format "course_registration_id> <status>"
        
        Raises
        ------
        COURSE_FULL_ERROR
            If no. of employees registered for the course has reached the maximum.
        """
        registration_status = None
        course = self.get_course(course_offering_id)
        employee_name = email_id.split("@")[0]
        
        if len(course.employees_registered) >= course.max_employees:
            registration_status = "COURSE_FULL_ERROR"
            raise Exception(registration_status)
        
        registration_status = "ACCEPTED"
        course_registration_id = "REG-COURSE" + "-" + employee_name + "-" + course.course_name  
        course.employees_registered.append((course_registration_id,email_id))
        output = course_registration_id  + " " + registration_status
        return output
           
    
    def cancel_registration(self, course_registration_id) -> list:
        """Cancels employee registration.
        Cancellation can be done until the course allotment is completed. There are 2 statuses : CANCEL_ACCEPTED, CANCEL_REJECTED 
        
        CANCEL_ACCEPTED when the cancellation is successful. 
        CANCEL_REJECTED when the course is already allotted. 
        
        Parameters
        ----------
        course-registration-id: str
        
        Returns
        -------
        output: str
    
        Format "<course-registration-id> <course.status>"
        """
        cancellation_status = None
        
        if self.allotment_done == True:
            cancellation_status = "CANCEL_REJECTED"
            output = course_registration_id + cancellation_status
            return output
        
        for _,course in self.courses.items():
            for registration in course.employees_registered:
                course_reg_id = registration[0]
                if course_reg_id == course_registration_id:
                    course.employees_registered.remove(registration)
                    cancellation_status = "CANCEL_ACCEPTED"
                    output = course_registration_id + " " + cancellation_status
                    return output
        
         
    
    def course_allotment(self, course_offering_id) -> str:
        """Allots employees to course offering, before the course offering date_in_ddmmyyyy . 
        
        It prints a list of all the employees with their details along with their final course allotment status (Registration Number, Employee Name, Email, Course Offering ID, Course Name, Instructor, Date, Final Status). The list is sorted based on the Registration number.
         
        If sufficient registrations are not received then the course offering itself gets cancelled. 
        
        The employees who have registered will get confirmed unless the minimum number of registrations is not received. 
        
        Even if the course offering gets canceled due to the minimum number of employees not registered, the list should be printed. 
        
        Parameters
        ----------
        course-offering-id: str
        
        Returns
        -------
        output: str

        Format of output is "<course-registration-id> <email-id> <course-offering-id> <course-name> <instructor> <date-in-ddmmyyyy> <course.status>"
        """
        
        self.allotment_done = True
        course = self.get_course(course_offering_id)
        course.employees_registered = sorted(course.employees_registered, key = lambda registration : registration[1])
        
        if len(course.employees_registered) < course.min_employees:
            course.course_status = "COURSE_CANCELLED"
            
        output = []
        
        for registration in course.employees_registered:
            course_registration_id = registration[0]
            email_id = registration[1]
            output.append(course_registration_id  + " " + email_id  + " " + course_offering_id  + " " + course.course_name  + " " + course.instructor  + " " + course.date_in_ddmmyyyy  + " " + course.course_status)
        
        output_str = "\n".join(output)
        return output_str