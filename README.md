# template_container
![Tests](https://github.com/Sleuth-Capital/template_container/workflows/Tests/badge.svg)
![Build](https://github.com/Sleuth-Capital/template_container/workflows/Build/badge.svg)
![Release](https://github.com/Sleuth-Capital/template_container/workflows/Release/badge.svg)


This is a template repository for a new Sleuth AI service.
Use the following steps to adapt it to a new container.

1. Click [use this template](https://github.com/Sleuth-Capital/template_container/generate)
2. Run ``poetry install``
3. Run ``poetry rename``
4. Modify ``reference/api.yaml``
5. Modify the contents of ``api`` to suit your ``api.yaml``
6. Run ``poetry run bumpversion [major|minor|patch]`` and the repository will automagically create a docker image and release

*Make sure to make the service available at* **``/template_container``** *in production!*

## Development
````
poetry install
poetry run container
````
## Test
````
poetry install
poetry run pytest
````
## Release
````
poetry run bumpversion [major|minor|patch]
git push --tags
````
## Container
````
docker build -t template_container .
docker run -p 9090:9090 template_container
````
