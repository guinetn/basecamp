# AZURE

https://azure.microsoft.com/
https://docs.microsoft.com/en-us/cli/azure/install-azure-cli

[Azure for Python Developers](https://docs.microsoft.com/en-us/azure/developer/python/)
[app-service](https://docs.microsoft.com/en-us/azure/app-service/)


200 produits et services cloud 

## AZURE TRAINING
https://www.youtube.com/watch?v=O_u2oPuZ8Mw

00:00​ = Introduction
00:21​ = Agenda
03:00​ = Cloud computing overview
06:22​ = Scalability vs Elasticity
07:32​ = Bring your own license: BYOL
09:33​ = Cloud service model : IaaS, PaaS, SaaS
16:33​ = Cloud Deployment models: Public, Private, Hybrid
21:53​ = Account,Subscriptions & Billing
28:03​ = Compute service: VM, App service, Functions, Logic Apps, Container, Kubernetes
01:00:25​ = Network Service: VNet, Subnet, VPN Getaway, Express Route, NSG, Bastion Host
01:08:04​ = Storage Service: Storage Account, Blob, File, Disk, Queue
01:13:00​ = Database Service Azure SQL,Cosmos, Synaps, Azure Data factory, Azure Data Lake
01:19:54​ = Data Protection: VM Backups, Azure site Recovery
01:24:25​ = Monitoring Service: Monitor, Alerts, Log Analytics
01:33:43​ = VM Migration Service: VMware & Hyper-V
01:36:01​ = Data Transfer Service
01:38:05​ = Data Box & Import/Export
01:41:10​ = Azure DevOps: Boards, Repos, Pipelines, Test Plans, Azure Artifacts
01:48:24​ = Al & ML on Azure for Data Scientists
01:58:21​ = Global Infrastructure: Region, paired Region, Availability Zone, Update & Fault Domain
02:07:03​ = Resource, ARM, Resource & Management Group
02:13:08​ = Management Tools: portal, Cloud Shell, CLI, power Shell, ARM Templates
02:24:36​ = Lab: Create Azure Cloud Account
02:40:02​ = Azure Road-map
02:41:54​ = FREE Class
02:42:14​ = Registration link for FREE Class

## Containerize Your Application With Docker

Docker CLI or Visual Studio 

Right-click the project in Solution Explorer, and add DockerFile
- DOCKERFILE file
- launchSettings.json     
    "Docker": {        
        "commandName" : "Docker", 
        "launchBrowser": true,         
        "launchUrl":  "httos://localhost:5001", 
        "publishAllPorts": true, 
        "useSSL": true, 
        "sslPort": 5001
    } 
- Deploy
    Right-click the project in Solution Explorer, and select “Publish…“
    Azure Container Registry
    ...Publish 
    >The resource group containing the newly created resources
    >The Azure Container Registry
    >The Docker image
    >An app service plan
    >The application instance itself, up and running
    https://localhost/5001

## Serverless Functions in azure

VSCode Azure Functions Extension: https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions

easy to get a basic API/microservice up and running quickly!
set-up an API endpoint using the HTTP Trigger invocation that you can use with any front-end site

* Azure Function HTTP trigger
- To build serverless APIs and respond to webhooks
- Invoke a function with an HTTP request/webhooks
- JavaScript, Python, C#, F#, Java

- Az login
- Create a resource
- Function App
- Once it has successfully been deployed, click Go to resource to view your new function app.
Click the + sign next to Functions on the left-hand side menu
select New Function 
Click Create: base function is generated with some default code

* Secure your Serverless HTTP Trigger by Adding Identity Management

Go to your function and select Integrate underneath it. Uncheck the POST checkbox, change the Authorization Level to Anonymous (users will not be prompted to log) and click Save.

* Azure Functions

Azure Functions can run in a serverless mode, which means that you only pay for the virtual machine executing the scheduled task as long as it is running. Azure Functions is a great and cheap way to implement scheduled tasks if you are already on Azure.

```C#
// Azure Function scheduled to run hourly
public class MyScheduledFunction
{
    [FunctionName("MyScheduledFunction")]
    public async Task Run([TimerTrigger("0 0 * * * *")]TimerInfo myTimer)
    {
        // Add your scheduled code here
        
        return Task.CompletedTask;
    }
}
```

## Devops: automate building and deployment

Azure DevOps Project simplifies the setup of an entire continuous integration (CI) and continuous delivery (CD) pipeline to Azure  
Deploy to Azure services
- Virtual Machines
- App Service
- Azure Kubernetes Services (AKS)
- Azure SQL Database
- Azure Service Fabric

DevOps Projects does all the work to configure of a DevOps pipeline
- setting up initial Git repository
- configuring the CI/CD pipeline
- creating an Application Insights resource for monitoring
- providing a single solution's view with the creation of a DevOps Projects dashboard in the Azure portal

## create an Azure DevOps CI/CD Pipeline For Your Containerised Application

Visual Studio has a built-in wizard to get you up with a templated pipeline.
Publish → Continuous delivery → Configure  
GitHub Personal Access Token. 

- https://www.azuredevopslabs.com/labs/vstsextend/azuredevopsprojectdotnet/

## DEPLOY

* 1. Creating an Azure App Service using Command Line

|||
|---|---|
|az login  |Login to Azure<br/>A browser window will open asking for your Microsoft Account credentials|
|az group create --name myResourceGroup --location westus|Add a Resource Group|
|az configure --defaults group=myResourceGroup location=westus|Set the default resource group and location for all subsequent commands|
|az appservice plan create --name myPlan --sku F1|Create an App Service plan|
|az webapp create --name __your_app_name__ --plan myPlan --runtime "DOTNETCOREi3.1"|Create the App Service itself|
|http://__your_app_name__.azurewebsites.net|Check app Service is running|

* 2. Deploying the App to Azure App Service using Command Line

|||
|---|---|
|az webapp deployment user set --user-name &lt;username&gt; --password &lt;password&gt;|Set deployment credentials. Replace username and password with your azure credentials.|
|az webapp deployment source config-local-git --name &lt;your_app_name&gt;|Retrieve the Git endpoint to which we want to push the app code:<br/>output: { "url": "https://gergely.sinka@mydomain.com@&lt;your_app_name&gt;.scm.azurewebsites.net/&lt;your_app_name&gt;.git"}|
|git remote add azure https://&lt;your_app_name&gt;.scm.azurewebsites.net/<your_app_name>.git|Set output URL without credentials as a remote for the local git repository:|
|git push azure master|Push the code to the new remote repository:|
|Open http://&lt;your_app_name&gt;.azurewebsites.net|Make sure the app is running|


##### Articles
- https://developer.okta.com/blog/2018/06/19/deploy-your-aspnet-core-app-to-azure
- https://developer.okta.com/blog/2020/10/07/dotnet-container-azure-devops
- https://www.azuredevopslabs.com/labs/vstsextend/azuredevopsprojectdotnet
- [Azure API Management](https://www.youtube.com/playlist?list=PLDUPL1iASgCwBa00t1fTqZrclVWip4THZ)
- https://www.compilemode.com/2020/12/what-is-azure-resource-and-resource-group.html
- https://dotnet.developpez.com/actu/311473/Apprendre-a-deployer-un-bot-sur-Microsoft-Azure-avec-le-CLI-un-billet-blog-d-Hinault-Romaric/

- https://www.thomasmaurer.ch/2020/12/how-to-learn-microsoft-azure-in-2021/
- https://docs.microsoft.com/en-gb/learn/?WT.mc_id=modinfra-12190-thmaure
- https://www.c-sharpcorner.com/article/how-to-integrate-application-insights-into-azure-functions/
- https://2bcloud.io/8-simple-steps-to-create-pub-sub-on-your-azure-environment/
- https://levelup.gitconnected.com/how-to-implement-azure-functions-in-any-language-with-custom-handlers-78e627264ccb

## API Management
https://www.youtube.com/watch?v=k_1391989z0

### Azure API Management - Transformation Policies

inboud policies
outboud policies
backend  policies
on-error  policies

- Replace in Body
- Set Http Header (add/remove)
- Set query string parameter
- Rewrite url
- Xslt Transform
- Convert Json ←→ xlm

Ex: https://www.youtube.com/watch?v=X6PqZ0HzG_c

## Azure Cloud identity
https://github.com/Daniel-Krzyczkowski/IdentityDeveloperTemplates
https://github.com/Daniel-Krzyczkowski/Cars-Island-On-Azure

## Azure Databricks

Azure Databricks = Databricks + Apache Spark + enterprise cloud

easy, fast, and collaborative Apache spark-based analytics platform. It accelerates innovation by bringing data science data engineering and business together. Making the process of data analytics more productive more secure more scalable and optimized for Azure.

https://k21academy.com/microsoft-azure/dp-200/azure-databricks

## Azure Event Hubs
https://azure.microsoft.com/services/event-hubs/
Azure Event Hubs is a highly scalable publish-subscribe service that can ingest millions of events per second and stream them to multiple consumers. This lets you process and analyze the massive amounts of data produced by your connected devices and applications. Once Event Hubs has collected the data, you can retrieve, transform, and store it using any real-time analytics provider, such as Azure Stream Analytics, or with batching/storage adapters.

## Azure cli: commands used to create and manage Azure resources

- https://docs.microsoft.com/en-us/cli/azure/
- https://docs.microsoft.com/en-us/cli/azure/get-started-with-azure-cli 

>az login
>az find secret
>az network nsg --help
>az account list

az group create --name <resource-group> --location <location>
>az group create --location westus --resource-group MyResourceGroup
>az group create --location westeurope --resource-group MyResourceGroup --tags {tags}
>az group list --query "[?location=='westeurope']"
>az group create --name TutorialResources --location eastus

>az vm list
>az vm show
>az vm create --resource-group TutorialResources --name TutorialVM1 --image UbuntuLTS --generate-ssh-keys --output json --verbose
    --generate-ssh-keys → SSH key named id_rsa
    SSH key files 'C:\Users\nguin\.ssh\id_rsa' and 'C:\Users\nguin\.ssh\id_rsa.pub' have been generated 
    under ~/.ssh to allow SSH access to the VM. If using machines without permanent storage, back up your keys     to a safe location.
    It is recommended to use parameter "--public-ip-sku Standard" to create new VM with Standard public IP. 
{
  "fqdns": "",
  "id": "/subscriptions/3f4...121b7/resourceGroups/TutorialResources/providers/Microsoft.Compute/virtualMachines/TutorialVM1",
  "location": "eastus",
  "macAddress": "00-0D-3A-8A-83-62",
  "powerState": "VM running",
  "privateIpAddress": "10.0.0.4",
  "publicIpAddress": "13.92.183.89",          → CONNECT TO ssh <PUBLIC_IP_ADDRESS>
  "resourceGroup": "TutorialResources",
  "zones": ""
}

>ssh 13.92.183.89
    The authenticity of host '13.92.183.89 (13.92.183.89)' can't be established.
    ECDSA key fingerprint is SHA256:Fk...Qg.
    Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
    Warning: Permanently added '13.92.183.89' (ECDSA) to the list of known hosts.    

    Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 5.4.0-1051-azure x86_64)

    * Documentation:  https://help.ubuntu.com
    * Management:     https://landscape.canonical.com
    * Support:        https://ubuntu.com/advantage

    System information as of Thu Jul  8 09:53:14 UTC 2021

    System load:  0.13              Processes:           112
    Usage of /:   4.6% of 28.90GB   Users logged in:     0
    Memory usage: 5%                IP address for eth0: 10.0.0.4
    Swap usage:   0%

C:\Users\nguin\.ssh
    📝 known_hosts
    13.92.183.89 ecdsa-sha2-nistp256 AAA5446...dU8=
    📝 id_rsa
    -----BEGIN RSA PRIVATE KEY-----
    MIIEp...
    📝 id_rsa.pub
    ssh-rsa AAAA...xX
    
>az vm show --name TutorialVM1 --resource-group TutorialResources
Get the network interface controller (NIC) object ID: 
>az vm show --name TutorialVM1 --resource-group TutorialResources --query 'networkProfile.networkInterfaces[].id' --output tsv
>az group delete --name TutorialResources --no-wait     ui not blocked
>az group wait --name TutorialResources --deleted       ui blocked



Resource type	Azure CLI command group
Resource group	az group
Virtual machines	az vm
Storage accounts	az storage account
Key Vault	az keyvault
Web applications	az webapp
SQL databases	az sql server
CosmosDB	az cosmosdb

--help          commands information, lists available subgroups and commands.
--output   -o   output format. json (default), jsonc (colorized JSON), tsv (Tab-Separated Values), table, yaml
--verbose       information about resources created in Azure during an operation...
--debug         more information about CLI operations
--query         uses the JMESPath query language to filter the output returned from Azure services
                [JMESPath query language](http://jmespath.org/)
                Queries are written in the JMESPath query language.
                Get the network interface controller (NIC) object ID: az vm show --name TutorialVM1 --resource-group TutorialResources --query 'networkProfile.networkInterfaces[].id' --output tsv
--resource-group  -g
--name -n

## more

- https://docs.microsoft.com/en-us/learn/azure/
- [Setting up an azure vm +  honeypot in Azure](https://www.youtube.com/watch?v=XDSar2i4s-s&t=1s)
https://github.com/telekom-security/tpotce
- https://github.com/microsoft/AzureTipsAndTricks

- https://hub-binder.mybinder.ovh/user/dotnet-interactive-cb9ukwlm/lab/tree/powershell/Samples/Managing-Azure.ipynb


