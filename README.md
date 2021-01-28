# template_container

This is a template repository for a new Sleuth AI service.
Use the following steps to adapt it to a new container.

1. Clone this repository
2. Run ``poetry install``
3. Run ``poetry run rename``
4. Run ``git --bare init``
5. Create new repository on gitlab and run
    ```
    git remote add origin https://gitlab.com/sleuth-ai/template_container.git
    git push -u origin --all
    git push -u origin --tags
    ```

*Make sure to make the service available at* **``/template_container``** *in production!*

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
docker build -t template_container .
docker run -p 9090:9090 template_container
````
