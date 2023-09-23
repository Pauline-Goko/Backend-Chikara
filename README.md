# Projects Template

# Carbon Emissions Backend

## Overview

Welcome to Chikara Backend repository. This repository contains the backend code for an Assembly Company's carbon emissions tracking system. The system allows the assembly company to monitor and analyze the emissions produced by their vehicles. Additionally, it provides insights into the total number of vehicles and the corresponding carbon credits earned over a specified period.

## Features

- **User Authentication**: Users (assembly company) can securely log in to access their account.

- **Vehicle Emissions Dashboard**: Provides a detailed view of the emissions data for each vehicle, including emission levels, vehicle information, and historical data.

- **Vehicle Inventory Management**: Allows the user to track the total number of vehicles owned by the company.

- **Carbon Credits Accumulation**: Displays the total number of carbon credits earned based on emission limits and reductions.

## Getting Started
- To set up and run the Backend on your local development environment,
Follow these steps:
1. Begin by cloning this repository to your local machine using the git clone command.
```
https://github.com/akirachix/Chikara-Backend.git
```
2. Navigate to the project directory
```
cd Chikara-Backend
```
3. Install the required dependencies. We recommend using a virtual environment for this step.
```
python3 -m venv venv
```
4. Activate the virtual environment using:
```
source venv/bin/activate
```
5.  Install Project Dependencies using:
```
pip install -r requirements.txt
```
6. Check the installed dependancies using:
```
pip freeze
```
12. Make migrations using:
```
python3 manage.py makemigrations
```
13. Migrate using :
```
python3 manage.py migrate
```
14. Runserver using:
 ```
python3 manage.py runserver
```

## Usage

1. **User Authentication**:
   - Log in to the system using your credentials.

2. **Vehicle Emissions Dashboard**:
   - Navigate to the "Dashboard" section to view detailed emissions data for each vehicle.

3. **Vehicle Inventory Management**:
   - Access the "Inventory" section to track the total number of vehicles owned.

4. **Carbon Credits Accumulation**:
   - Visit the "Carbon Credits" section to see the total number of carbon credits earned based on emission limits and reductions.

## Contributing

If you'd like to contribute to the development of this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

```bash
git checkout -b feature/your-feature-name
```

3. Make your changes and commit them:

```bash
git commit -m "Add your commit message here"
```

4. Push the changes to your forked repository:

```bash
git push origin feature/your-feature-name
```

5. Create a pull request on the original repository.
