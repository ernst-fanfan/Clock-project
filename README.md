# Time Project

This project is a web application that displays the current time for selected timezones. Users can select the timezones they want to display from a list of all available timezones.

## Features

- Display current time for selected timezones
- Select timezones from a list of all available timezones
- Automatically update the displayed time every second

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Docker

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/time-project.git
    cd time-project
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the Flask application:
    ```sh
    flask run
    ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

## Running with Docker

1. Build the Docker image:
    ```sh
    docker build -t time-project .
    ```

2. Run the Docker container:
    ```sh
    docker run -p 5000:5000 time-project
    ```

3. Open your web browser and go to `http://127.0.0.1:5000`.

## Running with Docker Compose

1. Start the services:
    ```sh
    docker-compose up
    ```

2. Open your web browser and go to `http://127.0.0.1:8050`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Time API](https://timeapi.io/) for providing the time data.
- Flask for the web framework.
- Docker for containerization.
