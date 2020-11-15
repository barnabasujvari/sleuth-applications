# container_template
![Build](https://github.com/Sleuth-Capital/template_container/workflows/Build/badge.svg)

template for sleuth containers
## development
````
poetry install
poetry run python main.py
````
## container
````
docker build -t container_template .
docker run -p 9090:9090 container_template
````