# Formula 1 Speed & Corner Maps

A Flask-based web application that visualizes Formula 1 telemetry data using speed maps and corner maps.

---

## Project Overview

This project analyzes Formula 1 session data and generates:
- Driver speed maps
- Circuit corner maps
- Visual insights using telemetry data

The application runs locally using Flask.

---

## Features

- Speed map visualization for F1 drivers  
- Circuit corner mapping  
- Flask-based web interface  
- Custom Formula 1 display fonts  
- Image generation using Matplotlib  

---

## Tech Stack

- Python
- Flask
- FastF1
- Matplotlib
- NumPy
- HTML and CSS

---

## Tech Stack

1. Clone the Repository : `git clone https://github.com/vrunstar/f1_maps.git`
2. Create a Virtual Environment : `python  -m venv venv`
3. Activate the environemnt : `venv\Scripts\activate`
4. Install Dependencies : `pip install flask fastf1 matplotlib numpy`
5. Run the Application : `python app.py`

---

## Notes
- FastF1 data is cached locally for better performance
- Cache directory is ignored using `.gitignore`
- Fonts and static assets are required for correct rendering

---

## License

This project is licensed under the MIT License.

