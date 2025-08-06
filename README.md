1. Scraping Logic:

Loads the web page using the requests library.

Parses the HTML content with BeautifulSoup.

Creates a DataFrame with pandas.

2. Data Cleaning:

Uses a regular expression in re.sub() to filter out unwanted characters from names and addresses.

3. Error Handling:

Wraps the CSV read operation in a try-except block:

If data.csv exists, it’s read.

If reading fails , it proceeds to save the DataFrame to CSV in append mode.

requests: Used to send HTTP requests and retrieve the HTML content of the target webpage. It’s a widely used library for making web requests in Python because it is simple and efficient for static page fetching.

BeautifulSoup : Used for parsing and navigating the HTML content to extract specific data elements. Chosen because it provides a straightforward API for HTML parsing and is commonly combined with requests for basic web scraping workflows.

re : Used for data cleaning, specifically to remove unwanted  characters from text data. Chosen for its robust pattern matching and string manipulation capabilities.

datetime.date: Used to get the current date.

pandas: Used to structure the extracted data into a DataFrame and handle CSV file operations. Chosen for its powerful data manipulation, tabular data representation, and ease of integrating with CSV and other data formats.
