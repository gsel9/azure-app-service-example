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
  - Follow the deployment process under the repo's Actions/ tab
6. Test querying the URL
```
import requests
requests.get(url).json()
```

Debug: 
- In Configuration > General Settings, turn on/off: FTP State, only HTTPS, Always on, 

startup.sh:
- python -m uvicorn application:app --host 0.0.0.0
- gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT

URL: <>/hello

https://seelapp01-gse7e4ftfue0guf3.canadacentral-01.azurewebsites.net/hello