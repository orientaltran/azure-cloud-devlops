# Overview

![oulinr](./screenshots/overview.png)
In this project, you will build a Github repository from scratch and create a scaffolding that will assist you in performing both Continuous Integration and Continuous Delivery. You'll use Github Actions along with a Makefile, requirements.txt and application code to perform an initial lint, test, and install cycle. Next, you'll integrate this project with Azure Pipelines to enable Continuous Delivery to Azure App Service.

## Project Plan
* Trello board: [Trello Board](https://trello.com/b/ZmXCqD4B/udacity-project-02)
* Project plan spreadsheet: [Project Plan](https://docs.google.com/spreadsheets/d/1ttoCh0Rcr2TrOr6ikpj6ZwxgfZ0UGhSptB6PCeKvsDM/edit#gid=0)

* For a visual demonstration of the project, please refer to this [YouTube video](https://www.youtube.com/watch?v=In43hcrVnCc).

## Instructions

* Connect Github with Azure Cloud Shell
   - SSH key generated:
     ```bash
     ssh-keygen -t rsa
     ```
   - Show and copy key:
     ```bash
     cat ~/.ssh/id_rsa.pub
     ```
   - Add new key to your GitHub profile (Settings => SSH keys > Add New)
   - Clone repository from GitHub to Azure Cloud Shell
     ```bash
     git clone git@github.com:orientaltran/azure-cloud-devlops.git
     ```

* Run and deploy the project
   - cd into the project directory
     ```bash
     cd azure-cloud-devlops
     ```
   - Run make file to install dependencies
     ```bash
     make install
     ```

* Run Locust Test

1. Goto the project directory
2. Run the script

   ```bash
   locust
   ```

3. Access link: http://0.0.0.0:8089
4. Run and check report

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


