## Flask Application Design for Historical Temperature Data Exploration

### HTML Files
- **index.html:**
  - Displays the interactive map and temperature slider.
  - Includes necessary HTML, CSS, and JavaScript components for UI and interactivity.
- **details.html:**
  - Displays detailed information about a specific location when clicked on the map.
  - Includes data on current temperature, historical averages, and weather forecasts.
  - Provides a form for users to enter a location name or zip code to search for a specific location.

### Routes
- **@app.route('/')**:
  - Renders the index.html file, serving the interactive map and temperature slider.
- **@app.route('/details', methods=['GET', 'POST'])**:
  - Handles GET requests to display the details.html file for a specific location.
  - Processes POST requests from the search form in details.html to redirect to the relevant location.
- **@app.route('/data/<date>')**:
  - Returns the historical temperature data for a given date in JSON format.
  - The date is passed as a parameter in the URL.
- **@app.route('/average-data/<location>')**:
  - Returns the historical average temperature data for a given location in JSON format.
  - The location is passed as a parameter in the URL.
- **@app.route('/forecast-data/<location>')**:
  - Returns the weather forecast data for a given location in JSON format.
  - The location is passed as a parameter in the URL.