# applications_container

## Development
````
poetry install
export DISABLE_OAUTH="True"
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
docker build -t applications_container .
docker run -p 9090:9090 applications_container
````
