# Profile Submission Flask Application

This is a simple Flask application that allows users to submit their profile information, including their name and city. The city list is dynamically populated from a `cities.csv` file, and submitted profiles are stored in a separate `user_profiles.csv` file.

## Features

- **Dynamic City Dropdown**: The dropdown list of cities is automatically updated every 5 seconds, allowing for real-time updates if new cities are added to the `cities.csv` file.
- **Form Submission**: Users can submit their name and selected city.
- **Data Storage**: Submitted profiles are appended to a `user_profiles.csv` file in the format: `name, city_id`.
- **Error Handling**: Displays an error message for empty submissions.
- **Responsive Design**: A clean and user-friendly interface for submitting profiles.

## Project Structure
