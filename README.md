# Croptimized

**Croptimized** is a web application designed to optimize and visualize agricultural crop rotation data using Linear Programming (CPLEX), with a forward-looking design that is quantum-ready. It integrates with an API to process and analyze data, helping in the decision-making process for sustainable agricultural practices.

## Setup Instructions

Before diving into running the application locally, ensure your environment is prepared with the necessary tools and configurations.

### Environment Variables

Set up the following environment variable in your system to connect to the MongoDB database.

| Variable  | Default    | Purpose                                |
|-----------|------------|----------------------------------------|
| MONGO_DB  | start-hack | Specifies the target database in MongoDB for the application to use. |

### Frontend (F/E) Setup

#### Prerequisites

- Ensure you have Node.js installed on your system to handle the project's dependencies and scripts.
- Navigate to your project's root directory before executing the following commands.

#### Dependencies Installation

Install the necessary dependencies for the frontend:

```bash
npm install tailwindcss postcss autoprefixer
```
Compile and Run CSS
To enable styling and auto-reload features, compile and run the CSS in a separate terminal window:

```bash
cd src/app/frontend/static
npm run build
```


### Running Locally with Docker
Prerequisites
- Docker and docker-compose must be installed on your system.
- Start your Docker client to ensure Docker commands can be executed.


#### Starting Docker Client
```bash
sudo systemctl start docker
```

#### Running the Application
To run the FastAPI instance locally with Docker, ensuring your project's root directory is your current working directory:

```bash
sudo docker-compose up --build
```