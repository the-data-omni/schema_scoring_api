# Schema Scoring API

A lightweight Flask API designed to compute and return a score based on a given schema description, with optional override weights for various scoring criteria. This repository can help you evaluate how closely your database schema will be understood by your users and how easily it will work with Generative AI models.

---

## Features

- **Schema scoring**: Evaluates tables and columns based on:
  - Field names
  - Field descriptions
  - Field name similarity
  - Field types
  - Presence of primary/foreign keys
- **Customizable weights**: Override default weights for each criterion via the `weights_override` field.
- **RESTful API**: Easily integrate with other services by sending a JSON payload.

---

## Repository Structure

```bash
schema_scoring_api/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   └── schema_scoring_routes.py
│   ├── services/
│   │   └── scoring_service.py
│   ├── utils/
│   │   └── logging_config.py
├── requirements.txt
└── run.py
```

- **`app/routes/schema_scoring_routes.py`**: Contains the Flask route(s) for handling requests.
- **`app/services/scoring_service.py`**: Implements the core logic of the scoring process.
- **`app/utils/logging_config.py`**: Provides a logging configuration.
- **`app/__init__.py`**: Initializes the Flask application.
- **`run.py`**: Entry point for running the Flask development server.
- **`requirements.txt`**: Lists all the Python dependencies needed.

---

## Prerequisites

- **Python 3.7+**  
- **Git** (to clone the repository)

---

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/schema_scoring_api.git
   cd schema_scoring_api
   ```

2. **(Recommended) Create a virtual environment**:

   ```bash
   # For Windows
   python -m venv venv
   venv\Scripts\activate

   # For macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Run the Flask application**:

   ```bash
   python run.py
   ```
   
   By default, this will start the application on `http://127.0.0.1:5000`.

2. **Send a POST request** with the following JSON structure to the appropriate endpoint.  
   _For example, if the route is `/api/v1/score_schema`, you can do:_

   ```bash
   curl -X POST -H "Content-Type: application/json" \
   -d '{
         "schema": [
           {
             "table_catalog": "foreign-connect-48db5",
             "table_schema": "ga4_dataform_seed",
             "table_name": "non_custom_events",
             "column_name": "sdf",
             "field_path": "event_name",
             "data_type": "STRING",
             "description": "",
             "collation_name": "NULL",
             "rounding_mode": null,
             "primary_key": false,
             "foreign_key": false
           },
           {
             "table_catalog": "foreign-connect-48db5",
             "table_schema": "ga4_dataform_seed",
             "table_name": "source_categories",
             "column_name": "sdf",
             "field_path": "source_category",
             "data_type": "STRING",
             "description": null,
             "collation_name": "NULL",
             "rounding_mode": null,
             "primary_key": true,
             "foreign_key": false
           }
         ],
         "weights_override": {
           "field_names": 10,
           "field_descriptions": 40,
           "field_name_similarity": 10,
           "field_types": 90,
           "keys_presence": 10
         }
       }' http://127.0.0.1:5000/api/v1/score_schema
   ```

3. **Review the response** which should contain a JSON object with a `score` field or similar, depending on implementation details.

---

## Example JSON Payload

Below is the expected JSON payload format for scoring:

```json
{
  "schema": [
    {
      "table_catalog": "project_name",
      "table_schema": "dataset_name",
      "table_name": "table_name",
      "column_name": "column_name",
      "field_path": "field_path",
      "data_type": "STRING",
      "description": "example description",
      "collation_name": "NULL",
      "rounding_mode": null,
      "primary_key": boolean,
      "foreign_key": boolean
    },
    {
      "table_catalog": "project_name",
      "table_schema": "dataset_name",
      "table_name": "table_name",
      "column_name": "column_name",
      "field_path": "field_path",
      "data_type": "STRING",
      "description": "example description",
      "collation_name": "NULL",
      "rounding_mode": null,
      "primary_key": boolean,
      "foreign_key": boolean
    }
    // ... more schema entries
  ],
  "weights_override": {
    "field_names": 30,
    "field_descriptions": 25,
    "field_name_similarity": 25,
    "field_types": 10,
    "keys_presence": 10
  }
}
```

- **`schema`** (required): A list of objects, each describing a table’s column.
- **`weights_override`** (optional): Provides custom weights to adjust scoring criteria weights are percentage weights adding up to 100.

---

## Logging

- The application uses a basic logging configuration from `logging_config.py`.
- Logs will appear in the console by default. Update the configuration for more advanced logging needs.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork this repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes, then commit and push.
4. Submit a pull request describing your changes.

---

## Contact

For questions, suggestions, or feedback, please open an issue in the repository or reach out to the project maintainer(s).

---

**Happy Coding!**  
Feel free to file an issue for any bugs or feature requests. If you find this project useful, consider giving it a star on GitHub!
