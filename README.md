## personalExperimentTracker
A Personal Experiment Tracker is a web application that helps users create and manage experiments or habits, log daily entries, and track progress over time. It includes features like metrics, reminders, and tagging to improve consistency, organization, and insights, enabling users to make data-driven decisions and achieve their personal goals effectively.

# Features
- Authentication (Register, Login, Logout)
- Experiment Management (CRUD operations)
- Daily Entry Logging
- Metrics & Progress Tracking
- Reminders & Notifications
- Tagging & Filtering

#Structure
personal-experiment-tracker/
- app.py                  # Main Flask app
- config.py              # Config (DB, secret keys)
- requirements.txt

- /models                # Database models
user.py
experiment.py
entry.py
tag.py

- /routes                # All routes (API / pages)
auth_routes.py
experiment_routes.py
entry_routes.py
dashboard_routes.py

- /templates             # HTML pages
home.html [done]
login.html [done]
register.html [done]
dashboard.html [done]
experiment.html [done]
analytics.html [done]

- /static                # CSS, JS
css/
js/

- /utils                 # Helper functions
auth.py
reminders.py

/instance
    users.db          # SQLite DB
