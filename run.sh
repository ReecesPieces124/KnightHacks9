#!/bin/bash

VENV_DIR=".venv"
OS="UNKNOWN"

# FIND OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="LINUX"
elif [[ "$OSTYPE" == "msys" ]]; then
    OS="WINDOWS"
elif [[ "$OSTYPE" == "cygwin" ]]; then
    OS="WINDOWS"
else
    echo "ERROR: Unsupported OS. Bash file can't be used. Manually create virtual environment and install dependencies."
    read -p "Press any key to exit..."
    exit 1
fi


# PY VERSION
PYTHON_CMD="python"

# SET DIRECTORY
cd "$(dirname "$0")"

# CHECK IF VENV EXISTS
if [ ! -d "$VENV_DIR" ]; then
  echo "Creating virtual environment..."$'\n'
  $PYTHON_CMD -m venv $VENV_DIR
fi

# LINUX
if [ "$OS" == "LINUX" ]; then
  # ACTIVATE VENV
  echo $'\n'"Activating venv..."$'\n'
  source $VENV_DIR/bin/activate || { echo "ERROR : Failed to activate venv."; read -p "Press any key to exit..."; exit 1; }

  # INSTALL DEPENDENCIES
  echo $'\n'"Installing dependencies..."$'\n'
  ./$VENV_DIR/bin/pip install -r requirements.txt || { echo "ERROR : Failed to install dependencies."; read -p "Press any key to exit..."; exit 1; }

  # RUN PROGRAM
  echo $'\n'"Running the program..."$'\n'
  ./$VENV_DIR/bin/python ./main.py || { echo "ERROR : Program failed to run."; read -p "Press any key to exit..."; exit 1; }

# WINDOWS
elif [ "$OS" == "WINDOWS" ]; then

  # ACTIVATE VENV
  echo $'\n'"Activating venv..."$'\n'
  ./$VENV_DIR/Scripts/activate.bat || { echo "ERROR : Failed to activate venv."; read -p "Press any key to exit..."; exit 1; }

  # INSTALL DEPENDENCIES
  echo $'\n'"Installing dependencies..."$'\n'
  ./$VENV_DIR/Scripts/pip install -r requirements.txt || { echo "ERROR : Failed to install dependencies."; read -p "Press any key to exit..."; exit 1; }

  # RUN PROGRAM
  echo $'\n'"Running the program..."$'\n'
  ./$VENV_DIR/Scripts/python.exe ./main.py || { echo "ERROR : Program failed to run."; read -p "Press any key to exit..."; exit 1; }

fi

read -p "Press any key to exit..."



