# applications_container
This is a coding assignment for Sleuth AI applicants. The deadline for this assignment is **7. April 2021 at 16:00 GMT**.
When the assignment is complete, please add @PatrickTourniaire and @MiniXC as collaborators to your private fork of this repository.

We are asking you to implement a function which finds valid stock tickers in a given string.
You can find it under `api/get_ticker.py`.
Optionally, you also expand the tests found in `tests/test_applications_container.py`.

*This functionality has already been solved in the Sleuth AI platform, and your implementation remains your personal intellectual property.*

If you feel like your implementation could be expanded, please add a comment below said function.

Your first steps could be:
1. create a private fork of this repository
2. install [poetry](https://pypi.org/project/poetry/) for package management
2. run `poetry install`
3. run `poetry run pytest`

Feel free to use any publicly available pypi packages, you can add them by using `poetry add some-package`.
For any questions about the assignment, please open an issue on this repository.

## Test
````
poetry install
poetry run pytest
````

## Development (Optional)
````
poetry install
export DISABLE_OAUTH="True"
poetry run container
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
