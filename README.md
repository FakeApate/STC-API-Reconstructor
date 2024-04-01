# Swiss Tax Calculator (STC) API Reconstructer

## Overview

This project is designed to fetch JavaScript files and their source maps from the Swiss Tax Calculator website. The primary goal is to analyze these files to reconstruct the API used by the web application, allowing for direct REST API calls without interacting with the official web interface. This can be particularly useful for automation, research, or integrating Swiss tax calculation features into third-party applications.

## Features

- Automatically downloads JavaScript files and their source maps from the Swiss Tax Calculator website.
- Analyzes downloaded files to identify API endpoints and data structures used by the web application.
- Provides a foundation for making direct calls to the Swiss Tax Calculator's REST API, bypassing the need for manual interaction with the web interface.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.x and pipenv: Required for running the script that fetches JavaScript files and source maps.
- Node.js and npm: Needed for any JavaScript-based analysis or reconstruction tasks.

## Setup

### Clone the Repository

1. Clone this repository to your local machine using:

   ```sh
   git clone git@github.com:FakeApate/STC-API-Reconstructor.git
   ```

### Install Dependencies

2. **Python Dependencies**

   Navigate to the project directory and install Python dependencies:

   ```sh
   pipenv install
   ```

3. **Node.js Dependencies**

   Install Node.js dependencies specified in `package.json`:

   ```sh
   npm install
   ```

## How to Use

1. **Fetch JavaScript Files**

   Run the Python script to download JavaScript files and their source maps from the Swiss Tax Calculator website:

   ```sh
   pipenv get_app.py
   ```

   This script will save the downloaded files in the `out` directory.

## Note

This project is intended for educational and research purposes. Always ensure compliance with the [Swiss Tax Calculator website's terms of service](https://www.admin.ch/gov/de/start/rechtliches.html) and use the API responsibly.

## Contributing

Contributions to improve the script or extend its capabilities are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.
