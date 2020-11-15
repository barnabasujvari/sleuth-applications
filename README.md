# template_container
![Build](https://github.com/Sleuth-Capital/template_container/workflows/Build/badge.svg)

This is a template repository for a new Sleuth AI service.
Use the following steps to adapt it to a new container.

1. Click [use this template](https://github.com/Sleuth-Capital/template_container/generate)
2. Run ``poetry install``
3. Run ``poetry rename``
4. Modify ``reference/api.yaml``
5. Modify the contents of ``api`` to suit your ``api.yaml``

*Make sure make the service available at* **``/template_container``** *in production!*

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
## Container
````
docker build -t template_container .
docker run -p 9090:9090 template_container
````
