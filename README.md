# Reproduction Steps to run on Your Local System.

## Phase1

Step1: Navigate to the above github link and clone it, to run on your VS code. 

Step2: Open ScrapeCode.py and in the URL section, paste the targeted website url to extract needed file data. 

Step3: Run and it will automatically get downloaded.

Note: On my end, I'm sharing the target URL i.e gobritanya.com (assumed to be an Amber competitor) along with the output I’m receiving which I have attached with this mail. You can do with any URL and follow the Phase 2, to get output files. 

Targeted URL: https://w ww.gobritanya.com/student-residences/london


## Phase2
Step 1: As mentioned in Phase 1-> Step1

Step 2: set up the environment and Install the required libraries from requirements.txt

Step 3: Open the Backend Folder

Note: I’ve used my own Gemini API key(backend folder->main.py). On your end, please create one and replace it accordingly. Keep the model_name as is unless you're referring to the documentation to change it.

Now, On the backend path folder in the terminal run uvicorn main:app --reload --host 0.0.0.0 --port 8000 , you see it start running and leave the terminal as it is and move to step 4.

Step 4: Open Frontend folder And,

run cmd npx create-react-app ui
cd ui
npm install axios
if you encountered problem, then i have attached App.js file link, copy the code and paste it to Frontend->ui->src->App.js Link: https://drive.google.com/file/d/1EvxW_qy31MtbSSNXIVnjcEVrwe_gxYI-/view?usp=sharing
on your terminal use npm start
