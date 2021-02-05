# CI-CD

Continuous Integration (CI)
Continuous delivery (CD)

Delivery process tools
- automate build testing
- reduces the risk of manual errors
- provides standardized development feedback loops
- enables fast product iterations.

With a deployment pipeline, teams can release software in a fast, repeatable and reliable manner 

![](assets/books/devops/assets/ci_cd_process01.png)

## Staging environment
- where changes are run against production-equivalent infrastructure and data to ensure that they will work properly when released.
- use the 'develop' branch
- deploy to the staging server

## Production environment
- use the 'master/main' branch
- deploy to the live server 
- master branch should always be ready for a deployment to live


A developer’s job typically ends at reviewing a pull request from a teammate and merging it to the master branch. Buddy then takes over from there by running all tests and deploying the code to production, while keeping the team notified through channels like Slack (we shall discuss setting up Slack notifications later).

download.page(devops/ci.md)

download.page(devops/cd.md)
