# Violent Python scripts - Python 3 Port
This repository contains Python 3 versions of the scripts from the book "Violent Python" by TJ O'Connor. The scripts have been updated to work with Python 3 and are organized by chapters as in the book.

## Project Structure
```
├── Chapter_1
│   ├── bannerscanner.py
│   └── vuln_banners.txt
├── .gitignore
├── README.md
├── requirements.txt
└── .venv
```

## Setup Instructions
Follow these steps to set up the project on your local machine 

### 1. Clone the Repository
Clone this repository to your local machine with the following command 
```bash
git clone git@github.com:paul9115/violent_python.git
```

### 2. Create and activate a virtual environment 
Navigate to the project root and create a virtual environment 
```bash
cd violent_python
python3 -m venv .venv
```
Activate the virtual environment 
* On Windows:
```bash
.venv\Scripts\activate
```
* On MacOS/Linux:
```bash
source .venv/bin/activate 
```

### 3. Installing the dependencies
Install the required dependencies with the following command:
```bash
pip install -r requirements.txt
```

## Running the scripts
To run the scripts navigate to the respective chapter directory and execute the script 
For example to run the `bannerscanner.py` script from Chapter 1 use the following command:

```bash
python Chapter_1/bannerscanner.py
```

## Contributing 
If you would like to contribute to this project, please follow these steps 
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.