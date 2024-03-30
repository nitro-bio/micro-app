# Micro-App

[![Backend Lint](https://github.com/nitro-bio/micro-app/actions/workflows/backend_lint.yml/badge.svg)](https://github.com/nitro-bio/micro-app/actions/workflows/backend_lint.yml)

[![Frontend Lint](https://github.com/nitro-bio/micro-app/actions/workflows/frontend_lint.yml/badge.svg)](https://github.com/nitro-bio/micro-app/actions/workflows/frontend_lint.yml)


## Introduction

This project sets up a simple fullstack application. It includes a frontend built using React, a backend built with FastAPI, as well as a SQLite database. The frontend is bundeled via Vite and uses Tailwind CSS for styling. The application is (optionally) containerized using Docker.

## Technologies Used

- **Database**
  - SQLite
- **Backend**
  - FastAPI
- **Frontend**
  - React
  - Vite
  - TypeScript
  - Tailwind CSS

## Quickstart

After cloning the repository, you can start the application in one of two ways: using Docker or running natively.

### Using Docker

To quickly start the entire application in dev mode using Docker, run the following command:

```bash
docker-compose up --build
```

This command builds and runs the containers for both the frontend and backend parts of the application. The app will be then be available at http://localhost:8000.

### Running Natively

For a native setup, follow these steps:

#### Frontend

```bash
cd frontend
npm install
npm run dev
```

#### Backend

In a new shell, set up the backend:

```bash
cd backend

# If using venv
python3 -m venv venv
source venv/bin/activate

# If using conda
conda create --name myenv python=3.9
conda activate myenv

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn main:app --reload
```

The app will be then be available at http://localhost:8000.

#### Production builds

To spin up a production build, run
```bash
docker-compose -f docker-compose.production.yml up --build
```

## Directory Structure

- `backend/`:
  - `main.py`: The main application file where the FastAPI app is defined.
  - `requirements.txt`: Lists the Python dependencies for the backend.
  - `static/`: A directory to serve static files, like the index.html that bootstraps the frontend.
- `frontend/`:
  - `package.json`: Lists the npm dependencies and scripts for the frontend.
  - `src/`: Contains the source code for the React application, including App.tsx and other TypeScript files.
- `dockerfiles/`:
  - `Dockerfile.backend`: containerizes the backend app
  - `Dockerfile.frontend`: containerizes the frontend app
- `docker-compose.yml`: Defines the multi-container Docker applications and how they interact.
- `.github/`
  - `workflows/`
  - `backend_lint.yml` Defines the GitHub Actions workflow for linting the backend via ruff and black.
  - `frontend_lint.yml` Defines the GitHub Actions workflow for linting the frontend via ESLint, tsc, and Prettier.
