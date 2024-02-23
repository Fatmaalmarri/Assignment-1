#Importing Enum class from the enum python module
from enum import Enum
#Using an enumerator class for boarding classes, economy, business, and first class
class BoardingClass(Enum):
    Economy = "Economy"
    Business = "Business"
    First = "First"

#Using an enumerator class for the staff roles
class Roles(Enum):
    CustomerService = "Customer Service Agent"
    Pilot = "Pilot"
    FlightAttendant = "Flight Attendant"
    CheckIn = "Check-In Agent"

#Using an enumerator class for the staff job status
class StaffStatus(Enum):
    partTime = "Part Time"
    fullTime = "Full Time"

#Parent class
class Person:
    """Class to represent a Person"""
    #Using initializing constructor to initialize attributes of Person class
    def __init__(self, firstName, lastName, dateOfBirth, email, phoneNum):
        #Initializing attributes
        self._firstName = firstName
        self._lastName = lastName
        self._dateOfBirth = dateOfBirth
        self._email = email
        self._phoneNum = phoneNum

    #Implementing setter and getter functions for Person class attributes
    def set_firstName(self, firstName):
        self._firstName = firstName
    def get_firstName(self):
        return self._firstName

    def set_lastName(self, lastName):
        self._lastName = lastName
    def get_lastName(self):
        return self._lastName

    def set_dateOfBirth(self, dateOfBirth):
        self._dateOfBirth = dateOfBirth
    def get_dateOfBirth(self):
        return self._dateOfBirth

    def set_email(self, email):
        self._email = email
    def get_email(self):
        return self._email

    def set_phoneNum(self, phoneNum):
        self._phoneNum = phoneNum
    def get_phoneNum(self):
        return self._phoneNum

    #display Person information
    def displayPerson(self):
        print("Name:", self._firstName, self._lastName)
        print("Date of Birth:", self._dateOfBirth)
        print("Contact Information:", "E-mail:", self._email, "and Phone Number:", self._phoneNum)

#Child class
class Passenger(Person):
    """Class to represent Passenger as a child of Person class"""
    #Using constructor to initialize attributes of Passenger class
    def __init__(self, firstName, lastName, dateOfBirth, email, phoneNum, passportNum, idNumber, ticketNum, boardingClass, baggageID):
        #Calling the constructor of the parent class
        Person.__init__(self, firstName, lastName, dateOfBirth, email, phoneNum)
        #Initializing attributes
        self.__passportNum = passportNum
        self.__idNumber = idNumber
        self.__ticketNum = ticketNum
        self.__boardingClass = boardingClass
        self.__baggageID = baggageID

    #Implementing setter and getter functions for Passenger class attributes
    def set_passportNum(self, passportNum):
        self.__passportNum = passportNum
    def get_passportNum(self):
        return self.__passportNum

    def set_idNumber(self, idNumber):
        self.__idNumber = idNumber
    def get_idNumber(self):
        return self.__idNumber

    def set_ticketNum(self, ticketNum):
        self.__ticketNum = ticketNum
    def get_ticketNum(self):
        return self.__ticketNum

    def set_boardingClass(self, boardingClass):
        self.__boardingClass = boardingClass
    def get_boardingClass(self):
        return self.__boardingClass

    def set_baggageID(self, baggageID):
        self.__baggageID = baggageID
    def get_baggageID(self):
        return self.__baggageID

    #display Passenger information
    def displayPassenger(self):
        #Calling the display function from parent class to display its attributes
        Person.displayPerson(self)
        print("Passport Number:", self.__passportNum, "and ID:", self.__idNumber)
        print("Ticket Number:", self.__ticketNum, " -  Class:", self.__boardingClass.value)
        print("BaggageID:", self.__baggageID)

#Child class
class Staff(Person):
    """Class to represent Staff as a child of Person"""
    #Using constructor to initialize attributes of Staff class
    def __init__(self, firstName, lastName, dateOfBirth, email, phoneNum, staff_ID, airlineComp, role, salary, staffStatus):
        #Calling the constructor of the parent class
        Person.__init__(self, firstName, lastName, dateOfBirth, email, phoneNum)
        #Initializing attributes
        self.__staff_ID = staff_ID
        self.__airlineComp = airlineComp
        self.__role = role
        self.__salary = salary
        self.__staffStatus = staffStatus

    #Implementing setter and getter functions for Staff class attributes
    def set_staff_ID(self, staff_ID):
        self.__staff_ID = staff_ID
    def get_staff_ID(self):
        return self.__staff_ID

    def set_airlineComp(self, airlineComp):
        self.__airlineComp = airlineComp
    def get_airlineComp(self):
        return self.__airlineComp

    def set_role(self, role):
        self.__role = role
    def get_role(self):
        return self.__role

    def set_salary(self, salary):
        self.__salary = salary
    def get_salary(self):
        return self.__salary

    def set_staffStatus(self, staffStatus):
        self.__staffStatus = staffStatus
    def get_staffStatus(self):
        return self.__staffStatus

    #display Passenger information
    def displayStaff(self):
        #Calling the display function from parent class to display its attributes
        Person.displayPerson(self)
        print("Staff ID:", self.__staff_ID)
        print("Airline Company:", self.__airlineComp)
        print("Role:", self.__role.value )
        print("Salary:", self.__salary, "AED")
        print("Job Status:", self.__staffStatus.value)

class Ticket:
    """Class to represent a Ticket"""
    #Using initializing constructor to initialize attributes of Ticket class
    def __init__(self, seat, destination, departFrom, departTime, arrivalTime, gate, terminal, flightDate):
        #Initializing attributes
        self._seat = seat
        self._destination = destination
        self._departFrom = departFrom
        self._departTime = departTime
        self._arrivalTime = arrivalTime
        self._gate = gate
        self._terminal = terminal
        self._flightDate = flightDate

    #Implementing setter and getter functions for Ticket class attributes
    def set_seat(self, seat):
        self._seat = seat
    def get_seat(self):
        return self._seat

    def set_destination(self, destination):
        self._destination = destination
    def get_destination(self):
        return self._destination

    def set_departFrom(self, departFrom):
        self._departFrom = departFrom
    def get_departFrom(self):
        return self._departFrom

    def set_departTime(self, departTime):
        self._departTime = departTime
    def get_departTime(self):
        return self._departTime

    def set_arrivalTime(self, arrivalTime):
        self._arrivalTime = arrivalTime
    def get_arrivalTime(self):
        return self._arrivalTime

    def set_gate(self, gate):
        self._gate = gate
    def get_gate(self):
        return self._gate

    def set_terminal(self, terminal):
        self._terminal = terminal
    def get_terminal(self):
        return self._terminal

    def set_flightDate(self, flightDate):
        self._flightDate = flightDate
    def get_flightDate(self):
        return self._flightDate

    #defining a method to generate the ticket's QR code
    def generateCode(self):
        """Generate a QR code for the ticket"""
        #Adding a pass statement as a placeholder for future code
        pass

    #Defining a method to print the passenger's ticket
    def printTicket(self):
        """Print the ticket for the passenger"""
        #Adding a pass statement as a placeholder for future code
        pass

    #display Ticket information
    def displayTicket(self):
        print("Ticket Details:")
        print("Seat:", self._seat)
        print("From:", self._departFrom, " -  To:", self._destination)
        print("Flight Date:", self._flightDate)
        print("Departure Time:", self._departTime, " -  Arrival Time:", self._arrivalTime)
        print("Terminal:", self._terminal, " -  Gate:", self._gate)

#Creating objects
#Creating passenger 1 as an object and display all passenger details
passenger_1 = Passenger("James", "Smith", "04/02/1998", "james.smith@gmail.com", "050123567", "A64329", "782198743", "NA4321", BoardingClass.First, "D2371")
passenger_1.displayPassenger()
print(" ")  #Adding an empty line for spacing between objects
#Creating staff 1 as an object and display staff details
staff_1 = Staff("Asma", "Almazrooie", "01/05/1990", "asma.almazrooie@gmail.com", "055134972", "Y276", "Emirates", Roles.CustomerService, 6500.0, StaffStatus.partTime)
staff_1.displayStaff()
print(" ")  #Adding an empty line for spacing between objects
#Creating ticket 1 as an object and display all ticket details
ticket_1 = Ticket("09A", "New York, JFK", "Chicago, ORD", "11:40", "13:30", "03", "2", "06/12/20")
ticket_1.displayTicket()

print(" ") #Adding an empty line for spacing between objects
#Creating passenger 2 as an object and display passenger details
passenger_2 = Passenger("Fatma", "Almarri", "04/03/2001", "fatma.almarri@gmail.com", "050345669", "G45687", "712168845", "LN1234", BoardingClass.Business, "C1692")
passenger_2.displayPassenger()
print(" ") #Adding an empty line for spacing between objects
#Creating staff 1 as an object and display staff details
staff_1 = Staff("Mohammad", "Almuheiri", "01/05/1993", "mohammad.almuheiri@gmail.com", "055357031", "Z519", "Etihad", Roles.CheckIn, 7000.0, StaffStatus.fullTime)
staff_1.displayStaff()
print(" ") #Adding an empty line for spacing between objects
#Creating ticket 2 as an object and display all ticket details
ticket_1 = Ticket("06J", "Riyadh, RUH", "Dubai, DXB", "10:00", "11:15", "02", "1", "07/03/24")
ticket_1.displayTicket()
