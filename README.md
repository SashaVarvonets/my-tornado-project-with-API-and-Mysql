# my tornado project


1. Install requirements
2. Add params about MySQL connection to the file torndb_conector.py
3. If it needed configure url, endpoint, apikey for API requests in the file script_name.py in line 25-27
4. Launch script_name.py to collect data and save it to the database. You can to pass on additional argument:
- to configure date ranges --date_ranges=dd-mm-yyyy_dd-mm-yyyy
- to configure creating new DB --new_db=True

5. Launch main.py and go to localhost:8888 in your browser.