Objective:

To build a FastAPI (Python) application to manage Doctors and Patients with validations and GET and POST operations.

Steps for running this application in Windows 

1.	Install Python 3.9+ 
    Go to Python website: https://www.python.org/downloads/windows/
  	and download Python and install it in your system by double-clicking it.

    From the command prompt check the version of the Python installed using the command :
  	
        python –version
 
3.	Create a folder “doctor_patients_API” for the project and open it in VSCode

4.	Create a python virtual environment for this project in VSCode and activate it

        python -m venv venv
        ./venv/Scripts/activate

6.	Install the required software in this environment: fastapi, uvicorn, pydantic, SQLite
    Create a “requirements.txt” in the project folder and add the software with versions in it
  	
        fastapi==0.129.0
        uvicorn[standard]
        pydantic==2.12.5

      Run the following command:
  	
  	    pip install -r requirements.txt

      SQLite is available from Python’s built-in sqlite3 module

8.	Command to start the “uvocorn” server:
   
        uvicorn main:app –reload
  	
    where FastAPI “app” is created in main.py.

 10.  Use the http://localhost:8000 followed by the API name separated by “/” to access the services 
     from the server. The following APIs are available for GET and POST operations for Doctors and Patients data:
                     i) doctors – GET all doctors details
                    ii) add_doctor -  POST – add a new doctor details
                    iii) patients – GET all patients details
                    iv) add_patient – POST – add a new patient details

      To access the services from the API, we can use the FastAPI Swagger UI page available for with 
        the following address in the browser:
      
                 http:// localhost:8000/docs
 
       The FastAPI Swagger UI is interactive API documentation page to view and test the APIs.
     
       The data is stored in-memory in the lists:
