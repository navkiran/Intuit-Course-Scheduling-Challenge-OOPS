class Course:
    
    def __init__(self, course_name, instructor, date_in_ddmmyyyy, min_employees, max_employees) -> None:
        """Add a course.
        
        A course offering has course title, instructor and date_in_ddmmyyyy . 
        
        It also contains a minimum & maximum number of employees for the course offering.
        
        The format of course-offering-id is OFFERING-<COURSE-NAME>-<INSTRUCTOR>
        
        Parameters
        ----------
        course-name : str
        instructor : str
        date_in_ddmmyyyy : str
        min_employees : int
        max_employees : int
        
        Returns
        -------
        output: str
            course-offering-id
        
         The format of course-offering-id is "OFFERING-<COURSE-NAME>-<INSTRUCTOR>"
        """
        self.course_offering_id = None
        self.employees_registered = []
        self.course_status = "CONFIRMED"
        self.course_name = course_name
        self.instructor = instructor
        self.date_in_ddmmyyyy  = date_in_ddmmyyyy 
        self.min_employees = int(min_employees)
        self.max_employees = int(max_employees)
        self.course_offering_id = "OFFERING" + "-" + course_name + "-" + instructor