# Steam Backend Project

This project is a backend implementation for an application that interacts with the Steam API to make requests and retrieve data. 
The application allows users to see their profile, list of friends and games.

## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [License](#license)

## Installation

1. Clone the repository:
   git clone https://github.com/AlexSoulJk/mini_lab_3.git
2. Change into the project directory:
   ```
   cd your-repo
   ```

## Configuration
Before running the application, you need to obtain a Steam API key. [Click here](https://steamcommunity.com/dev/apikey) to get it.
1. Create a new file named `.env` in the root directory of the project.
2. Set the following environment variables in the `.env` file: steam_api=your-steam-api-key

## Usage

Run the application using the following command:

```
python main.py
```

The application will start serving on port 8000.

## Endpoints

The following are the available API endpoints provided by the backend application you can find
in [postman](https://www.postman.com/alexsouljk/workspace/minilab3/collection/31491017-40c0f8c5-a94c-4aaf-a3b0-08b930267a29?action=share&creator=31491017)


## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
