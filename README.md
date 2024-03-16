# Whales tracker

Showing whales holdings on different chains, using llamafolio.
Feel free to add your own 'wallets.json' or modify the existing one, but use the same structure.

## Prerequisites

Before you begin, ensure you have met the following requirements:

1. You have installed Python 3. If not, you can download it from the official site

    You can check your Python version with the following command:

    ```bash
    python --version
    ```

## Setting Up the Project
Follow these steps to set up the project:

1. Create a virtual environment:

    For macOS:
    ```bash
    python3 -m venv .venv
    ```

    For Windows:
    ```bash
    py -m venv .venv
    ```

2. Activate the virtual environment:

    For macOS:
    ```bash
    source .venv/bin/activate
    ```

    For Windows:
    ```bash
    \.venv\Scripts\activate
    ```

3. Install the requirements: 

    After activating the virtual environment, you can install the project dependencies from the ```requirements.txt``` file:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Providing your address is completely optional. Use it only if you want to see your own portfolio.

For Windows:
```bash
python wt.py
python wt.py --address=[your address]
```

For Mac:
```bash
python3 wt.py
python3 wt.py --address=[your address]
```