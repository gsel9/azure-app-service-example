# Deploy A FastAPI Endpoint To Azure App Services

Deployment hosts endpoints for querying. 

## Setup
1. Create a resource group
2. Create an App Services resource
3. In App Services, create a Web App
  - Runtime stack: Python 3.11
  - Continuous deployment: Enable
4. Creating the Web App with link to GitHub will add Action workflows that must be pulled into the app dev repo
5. In the Azure portal, from the service menu on the left, choose Settings > Configuration. On the Configuration page for the App Service, select General settings, enter the name of your startup file (startup.sh) under Stack settings > Startup Command, then select Save.
5. Push the app code to git, triggering deployment process


 On Linux App Service, Python apps don’t auto‑start Uvicorn for FastAPI—you must provide a Startup Command (or a startup script). Microsoft’s guidance explicitly says to set a custom startup command for frameworks that aren’t auto-detected (e.g., FastAPI) or when your entry point isn’t the default Flask names. You can put the command directly in the Startup Command field or reference a script checked into your repo. [dev.to]
