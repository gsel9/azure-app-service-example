# Deploy A FastAPI Endpoint To Azure App Services

Deployment hosts endpoints for querying. 

## Setup
1. Create a resource group
2. Create an App Services resource
3. In App Services, create a Web App
    - Runtime stack: Python 3.11
    - Continuous deployment: Enable (add gitHub details)
  - Creating the Web App with link to GitHub will add Action workflows that must be pulled into the app dev repo
5. Push the app code to git, triggering deployment process
  - Follow the deployment process under the repo's Actions/ tab
6. In the Azure portal, from the service menu on the left, choose Settings > Configuration > Stack Settings
7. Add `bash startup.sh` as Startup command and click refresh
8. Go to overview page and click restart app
9. Monitor application start-up process in the left service menu under Log Stream

Debug: 
- Refresh Configuration > Stack settings and restart App in overview page
- Tick "always on" in Configuration > General settings to avoid app timeouts

The code in `startup.sh` should be 
```
gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT
```