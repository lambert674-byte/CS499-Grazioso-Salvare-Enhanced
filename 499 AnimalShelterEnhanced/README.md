
# Grazioso Salvare Animal Shelter Dashboard
## CS 499 Computer Science Capstone — Database Enhancement

### Project Overview

The Grazioso Salvare Animal Shelter Dashboard is a Python-based application that uses MongoDB to manage and retrieve animal shelter records. The dashboard provides interactive filtering, data visualization, and animal information to help identify dogs that may qualify for different rescue training programs.

This project was originally developed during my CS 340 Client/Server Development course at Southern New Hampshire University. I selected it for my CS 499 Computer Science Capstone because it demonstrates my ability to work with databases, develop Python applications, and create interactive dashboards.

### Purpose of the Enhancement

The purpose of this enhancement was to improve database performance, security, data validation, and overall application functionality.

The enhancements include:

- Implementing MongoDB indexes to improve query performance.
- Optimizing database queries to reduce unnecessary record scanning.
- Using environment variables for database credentials.
- Improving input validation and database error handling.
- Adding pagination to manage large datasets.
- Improving rescue-type filtering and data retrieval.
- Integrating interactive data visualizations, including a breed distribution pie chart and a location reference map.
- Testing database operations and measuring query performance.

These improvements demonstrate my ability to enhance an existing application using database design principles, secure coding practices, and performance optimization techniques.



## Technical Enhancements

### 1. MongoDB Database Indexing

I enhanced the original MongoDB database by creating indexes on five frequently searched fields:

- Animal ID
- Animal Type
- Breed
- Outcome Type
- DateTime

The database contains 173,775 historical Austin Animal Center outcome records. Indexing allows MongoDB to locate matching records without always scanning the entire collection.

### 2. Database Performance Testing

I compared indexed queries against full collection scans using Python and MongoDB execution statistics.

**Dog Query Results:**
- Full collection scan: 133.56 ms
- Indexed query: 167.99 ms
- Matching records: 94,505

The indexed query was slower because dogs represent a large portion of the dataset. This demonstrated that indexes do not always improve performance.

**Bird Query Results:**
- Full collection scan: 52.55 ms
- Indexed query: 2.19 ms
- Documents examined without index: 173,775
- Documents examined with index: 877

The indexed bird query was approximately 24 times faster. These results demonstrate how query selectivity affects database performance.

### 3. Secure Database Configuration

I updated the MongoDB connection logic to support environment variables rather than hardcoded credentials.

The application supports authenticated database connections when credentials are provided.

During local development, MongoDB was configured to listen on localhost without authentication. Authentication must be enabled before deploying the application to a shared or publicly accessible environment.

### 4. Input Validation and Pagination

I added a search_animals() method to the CRUD module that supports:

- Filtering by approved database fields
- Validating search parameters
- Rejecting unsupported filter fields
- Limiting the number of returned records
- Retrieving records using pagination

Testing confirmed that filtering, pagination, and invalid-field rejection worked successfully.

### 5. Dashboard Improvements

I updated the dashboard to work with the imported Austin Animal Center Outcomes dataset.

Improvements included:

- Correcting MongoDB field names
- Updating Water, Mountain, and Disaster Rescue filters
- Restoring Reset functionality
- Displaying animal records in an interactive table
- Visualizing breed distribution with a pie chart
- Displaying an interactive Austin, Texas reference map
- Updating animal information when a different record is selected

Because the dataset does not contain individual animal coordinates, the map uses Austin as a reference location rather than displaying actual animal locations.




## Testing and Validation

I performed functional and database testing to verify that the enhanced application operates correctly.

### Database Testing

The following tests were completed:

- CRUD module syntax validation: PASSED
- MongoDB database connection: PASSED
- Animal filtering by type: PASSED
- Search pagination: PASSED
- Invalid search field rejection: PASSED
- MongoDB index creation and query analysis: PASSED

The search validation test returned 10 bird records, confirmed that pagination produced different results across two pages, and successfully rejected an invalid filter field.

### Dashboard Functional Testing

I tested the enhanced dashboard using the local Dash application.

| Test | Result |
|------|--------|
| Dashboard loads successfully | PASSED |
| Water Rescue filtering | PASSED |
| Mountain Rescue filtering | PASSED |
| Disaster Rescue filtering | PASSED |
| Reset filtering | PASSED |
| Data table pagination | PASSED |
| Breed distribution pie chart | PASSED |
| Interactive map displays | PASSED |
| Animal information popup | PASSED |
| Popup updates after selecting another animal | PASSED |

### Testing Limitations

The dashboard uses a fixed Austin, Texas reference location because the imported dataset does not include individual animal coordinates.

Although the CRUD module supports paginated searches, the dashboard currently retrieves matching records into memory. Implementing server-side pagination would improve scalability for larger datasets.

### Testing Summary

The completed tests demonstrate that the enhanced application can retrieve, filter, validate, and visualize animal shelter records.

The enhancements improved database functionality, strengthened input handling, and provided a more interactive interface for reviewing animals eligible for rescue training programs.




## Installation and Execution

### Requirements

The following software is required:

- Python 3
- MongoDB Community Server
- Visual Studio Code
- Jupyter Notebook
- Python libraries: pymongo, pandas, dash, plotly, dash-leaflet, and notebook

### 1. Install Python Dependencies

Open a terminal in the project directory and run:

```bash
py -m pip install pymongo pandas dash plotly dash-leaflet notebook
```

### 2. Start MongoDB

Start the local MongoDB server.

The application uses the following connection during local development:

```text
mongodb://127.0.0.1:27017/
```

Database: aac
Collection: animals

### 3. Prepare the Database

If the database has not been populated, use the provided import script and the original dataset to import animal shelter records.

Run:

```bash
py import_animals.py
```

Create the database indexes:

```bash
py create_indexes.py
```

The import step is not necessary when the database already contains the required records.

### 4. Run Database Tests

Run the search and validation tests:

```bash
py test_search_animals.py
```

Run the query performance tests:

```bash
py test_query_performance.py
```

### 5. Launch the Dashboard

Open ProjectTwoDashboard.ipynb in VS Code.

Select the Python environment containing the required libraries and execute the notebook cells.

The dashboard uses Dash and runs locally at:

http://127.0.0.1:8050/

Open this address in a web browser to access the dashboard.

### 6. Using the Dashboard

The dashboard provides the following features:

- Water Rescue: Displays animals matching water rescue criteria.
- Mountain Rescue: Displays animals matching mountain rescue criteria.
- Disaster Rescue: Displays animals matching disaster rescue criteria.
- Reset: Displays the complete dataset.
- Data Table: Allows users to browse and select animal records.
- Pie Chart: Displays breed distribution.
- Interactive Map: Displays an Austin reference marker and information about the selected animal.

### Security Note

The local MongoDB configuration is intended for development and testing.

Before deployment, database authentication, appropriate network restrictions, and secure credential management should be configured.





## CS 499 Course Outcomes and Enhancement Reflection

### Applying Computer Science Skills

Enhancing the Grazioso Salvare Animal Shelter Dashboard allowed me to apply the knowledge and technical skills I developed throughout the Computer Science program at Southern New Hampshire University.

Rather than creating an entirely new application, I improved an existing project by identifying weaknesses, implementing enhancements, and testing the results.

### Software Design and Engineering

I improved the organization and reliability of the application by updating the Python CRUD module, adding input validation, and improving database error handling.

I also updated the Dash dashboard to work with the imported MongoDB dataset and provide interactive filtering and visualizations.

These changes demonstrate my ability to maintain, troubleshoot, and improve existing software.

### Algorithms and Data Structures

I applied problem-solving techniques when designing database search functionality and implementing pagination.

I also evaluated how query selectivity and indexing affect database performance.

Performance testing demonstrated that indexed queries are not always faster, especially when a query matches a large percentage of the dataset.

### Databases

The primary focus of this enhancement was improving database functionality and performance.

I implemented MongoDB indexes, strengthened database connection configuration, added query validation, and tested database operations.

These improvements demonstrate my understanding of database management, efficient data retrieval, and secure coding practices.

### Professional Growth

This project helped me better understand the importance of testing and improving software after its initial development.

I gained additional experience troubleshooting Python applications, analyzing MongoDB query performance, and integrating database operations with an interactive user interface.

The enhancement also strengthened my ability to document technical decisions and explain how software improvements benefit users.

### Future Improvements

Although the enhanced application meets its current functional goals, several improvements could be implemented in the future:

- Add server-side pagination to reduce memory usage.
- Implement automated unit and integration tests.
- Add database authentication for deployment.
- Improve dashboard responsiveness and accessibility.
- Integrate verified geographic coordinates if suitable location data becomes available.

### Conclusion

The Grazioso Salvare Animal Shelter Dashboard enhancement demonstrates my growth as a computer science student.

Through database optimization, validation, troubleshooting, testing, and visualization, I improved the original application while applying skills developed throughout my degree program.

This project represents the database enhancement component of my CS 499 Computer Science Capstone ePortfolio.
