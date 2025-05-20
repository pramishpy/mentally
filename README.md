# Mentally: AR Mental Health Stigma Reduction

Mentally is a web application that uses Augmented Reality (AR) to reduce mental health stigma through educational simulations, interactive activities, and evidence-based resources.

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- Git (optional, for cloning the repository)
- Modern web browser with support for WebGL and camera access

### Step 1: Get the Code

Either clone the repository from GitHub:

```bash
git clone https://github.com/pramishpy/mentally.git
cd mentally
```

Or extract the downloaded ZIP file to a folder of your choice.

### Step 2: Create a Virtual Environment

It's recommended to use a virtual environment to avoid package conflicts.

On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

Install all the required packages using pip:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

Start the Flask development server:

```bash
python app.py
```

The application will be available at `http://localhost:5000/` in your web browser.

## Using the Application

1. **Home Page**: Navigate through the main sections of the application
2. **AR Experience**: Explore mental health concepts through augmented reality
3. **Learn**: Educational content about various mental health topics
4. **Simulations**: Experience simulations to gain perspective on mental health conditions
5. **Activities**: Interactive tasks to help reduce stigma
6. **Resources**: Find mental health information and support

## AR Features

To use the AR features:
- Allow camera access when prompted
- Make sure you're in a well-lit area
- For marker-based AR, print the markers located in `static/assets/markers/`
- Hold your device camera towards the marker to see the AR content

## Notes for Developers

- Configuration files are located in the project root directory
- The Flask application is defined in `app.py`
- Templates are stored in the `templates` directory
- Static assets (JS, CSS, images) are in the `static` directory

## Troubleshooting

- **AR not working**: Ensure your browser supports WebGL and has camera permissions
- **Module not found errors**: Make sure you've installed all dependencies from requirements.txt
- **Server not starting**: Check for error messages in the terminal, you might have another service using port 5000

## Credits

Created by the Mentally team as part of a mental health stigma reduction initiative.
