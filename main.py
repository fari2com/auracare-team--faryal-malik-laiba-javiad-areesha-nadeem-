# AuraCare Health System Core
APP_VERSION = "1.0.0"
MODULES_ENABLED = []

def triage_patient(priority_level):
    if priority_level == 1:
        return "Critical: Immediate Doctor Attention Required"
    return "Stable: Regular Queue"