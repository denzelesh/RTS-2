## Module Needed To Display Date,Time & Allow System To Wait
import time

## Example Conditions
## In a real scenario an external hardware device would provide these conidtions
## Changing These Conditions, such as PowerFailure = 'True' will make the system repsond differently
SmokeDetected = True
PowerFailure = False
PowerRegained = False
NameOfZone = "Ground Floor - (GF)"
ZoneAlarms = ['GF-Alarm-1', 'GF-Alarm-2', 'GF-Alarm-3']


# Function For The Entire Fire Alarm System
def fireAlarmSystem():
    global SmokeDetected
    if SmokeDetected:
        print("Smoke detected at", time.strftime("%Y-%m-%d %H:%M:%S"))
        manualAlarmConfirmation = input("For Confirmation, is there smoke present? (yes/no): ")
        ##Using "lower.()" so that even if the user does not tyep exactly 'yes' eg they type YES or Yes
        ## It would still work.
        if manualAlarmConfirmation.lower() == "yes":
            print("System activated at", time.strftime("%Y-%m-%d %H:%M:%S"))
            print("Activating alarm")
            print("Activating sprinklers")
            print("Closing doors")
            print("Activating emergency lighting")
            print("Calling emergency services")
            generateIncidentReportLog = input("Would you like to generate an incident report? (yes/no): ")
            if generateIncidentReportLog.lower() == "yes":
                print("Alarm system activated at", time.strftime("%Y-%m-%d %H:%M:%S"))
                print("Alarm zone:", NameOfZone)
                print("Alarms activated:", ', '.join(ZoneAlarms))
                terminateFireAlarmSystem()
                # Option to terminate,so staff can check for damnged compnenets & manually reset system.

            if generateIncidentReportLog.lower() == "no":
                terminateFireAlarmSystem()

        if manualAlarmConfirmation.lower() == "no":
            print("False alarm.")
            generateIncidentReportLog = input("Would you like to generate an incident report? (yes/no): ")
            if generateIncidentReportLog.lower() == "yes":
                print("False alarm triggered at ", time.strftime("%Y-%m-%d %H:%M:%S"))
                print("Alarm zone:", NameOfZone)
                print("Alarms activated:", ', '.join(ZoneAlarms))
                resetFireAlarmSystem()
            if generateIncidentReportLog.lower() == "no":
                resetFireAlarmSystem()

    else:
        print("No smoke detected.")




# Function To ** RESET ** Fire Alarm System

def resetFireAlarmSystem():
    resetManualConfirmation = input("Just to confirm, do you want to reset the system? ")
    if resetManualConfirmation.lower() == "yes":
        print("System reset at", time.strftime("%Y-%m-%d %H:%M:%S"))
        print(" ") #This is done just for better readabillity when system resets
        fireAlarmSystem()
    else:
        terminateFireAlarmSystem() # May be A fault that requires system to be offline therfore a termination is better.


# Function To ** TERMINATE ** Fire Alarm System

def terminateFireAlarmSystem():
    terminateManualConfirmation = input("Just to confirm, do you want to terminate the system?: ")
    if terminateManualConfirmation.lower() == "yes":
        print("System terminated at", time.strftime("%Y-%m-%d %H:%M:%S"))
    else:
        resetFireAlarmSystem()


# Function For System Response To Power Failure

def powerFailureResponse():
    print("Power failure detected")
    print("Waiting 20 seconds to regain power")
    time.sleep(20)
    if PowerRegained == False:
        print("Calling emergency services")
        print("Activating emergency lighting")
        generateIncidentReportLog = input("Would you like to generate an incident report? (yes/no): ")
        if generateIncidentReportLog.lower() == "yes":
            print("Power failure detected at", time.strftime("%Y-%m-%d %H:%M:%S"))
            print("Zone Name:", NameOfZone)
            print("Alarms activated:", ', '.join(ZoneAlarms))
            resetFireAlarmSystem()
        if generateIncidentReportLog.lower() == "no":
            resetFireAlarmSystem()
    else:
        fireAlarmSystem()




###### Essentially The Main Program
#####  Calls Correct Function Based On Example Conditions

if PowerFailure:
    powerFailureResponse()
else:
    fireAlarmSystem()
