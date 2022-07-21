from fhirpy import SyncFHIRClient

from fhir.resources.patient import Patient
from fhir.resources.observation import Observation
from fhir.resources.humanname import HumanName
from fhir.resources.contactpoint import ContactPoint
from fhir.resources.imagingstudy import ImagingStudy

import json

client = SyncFHIRClient()
patients_resources = client.resources('Patient')
patient0 = Patient.parse_obj(patients_resources.search(family='Shen').first().serialize())
print("Our paitent:", patient0.name)