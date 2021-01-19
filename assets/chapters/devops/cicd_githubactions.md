## GitHub Actions

An API that can react to any event (on push event on the repository run test cases)

For continuous integration of your app
For continuous deployment (ex, pushing a Docker image to a Docker registry Docker Hub)

Tool to perform CI/CD
Run automatically tasks/actions on certain events (SDLC workflows in your GitHub Repo directly)

Salient Features of GitHub Actions
You can create, share, reuse, and fork your software development practices.
It is fully integrated with GitHub, making it manageable from a single place.
You can perform multi-container testing by adding support for Docker.
You can choose from multiple CI templates or even create your own.
Include 2000 free build minutes/month for all your private repositories.

1. Create   .github/workflows folder
2. push.yml
```yaml
on: push
name: npm build, lint, test and publish
jobs:
  build-and-publish:
    name: build and publish
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@master
      - name: npm install
        uses: actions/npm@master
        with:
          args: install
      - name: npm test
        uses: actions/npm@master
        with:
          args: run test
      - name: npm lint
        uses: actions/npm@master
        with:
          args: run lint
      - name: docker build
        uses: actions/docker/cli@master
        with:
          args: build -t abhinavdhasmana/github-action-example-node .
      - name: docker login
        uses: actions/docker/login@master
        env:
          DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}
          DOCKER_USERNAME: ${{ secrets.DOCKER_USERNAME }}
      - name: docker push
        uses: actions/docker/cli@master
        with:
          args: push abhinavdhasmana/github-action-example-node
```

On every push, perform these actions in the given order
- git clone the repo
- run npm install
- run npm lint
- run npm test
- build the docker image
- login to docker hub
- Push the image to docker hub

## More
- https://blog.bitsrc.io/https-medium-com-adhasmana-how-to-do-ci-and-cd-of-node-js-application-using-github-actions-860007bebae6