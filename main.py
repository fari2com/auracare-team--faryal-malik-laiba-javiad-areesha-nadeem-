# AuraCare Health System Core
APP_VERSION = "1.0.0"
MODULES_ENABLED = []
def get_doctor_schedule(doctor_name):
    schedules = {"Dr. Smith": "9:00 AM - 1:00 PM", "Dr. Jones": "2:00 PM - 6:00 PM"}
    return schedules.get(doctor_name, "Doctor not found")
