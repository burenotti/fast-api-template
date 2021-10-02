# Fast API project template

This is a project template for [**Fast API**](https://fastapi.tiangolo.com/) projects. It is not a minimal kit, so it has some additionals preinstalled. Also it use [**poetry**](https://python-poetry.org/), so you need it installed.

Here is additional packages those have been added to *pyproject.toml*:
1. [*Uvicorn*](https://www.uvicorn.org/) is ASGI web server.
2. [*python-dotenv*](https://pypi.org/project/python-dotenv/) gives capability to pydantic of loading settings from environment variables and `.env` file.
3. [*SQLAlchemy*](https://www.sqlalchemy.org/) is the most popular ORM for python. SQLAlchemy is provided with asyncpg driver preinstalled and should be used with asynchronous interface.
4. [*Alembic*](https://alembic.sqlalchemy.org/) is excelent migration tool for SQLAlchemy. It's need to be configured before use.

## Get started
### Creating project
To create a new project clone this repository using `git clone`...
```bash
git clone https://github.com/burenotti/fast-api-template project-name
cd project-name
```
... then install dependencies.
```bash
poetry install
```
### Configuring project
#### Poetry
Open `pypoject.toml` and provide name, version, description and authors of the project.
```toml
# Example
[tool.poetry]
name = "Awesome FastAPI project"
version = "0.1.0"
description = "Awesome FastAPI project"
authors = ["Awesome Developer <developer@example.com>"]
```
### Alembic
As documentation says, you need to provide database url in `alembic.ini` file. Open this file then replace `sqlalchemy.url` value with corrent database url.
If you use default `docker-run-postgres.sh` script, your database url will be `asyncpg+postgresql://postgres:password@localhost:5432/database`.

### Running uvicorn

To run your project run `poetry run python -m app`
