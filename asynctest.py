import asyncio
from fhirpy import AsyncFHIRClient
from fhirpy.base.searchset import Raw

async def main():
    # Create an instance
    client = AsyncFHIRClient(
    )

    # Search for patients
    resources = client.resources('Patient').search(identifier='3200083271').revinclude('ImagingStudy','patient')  # Return lazy search set
    #resources.search(general_practitioner__Organization__name='Hospital')
    #resources = resources.search(identifier='3200083271')
    patients = await resources.fetch_raw()  # Returns list of AsyncFHIRResource        

    org_resources = client.resources('Organization')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())