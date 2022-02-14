## Overview

A Python script which allows you to send a REST HTTP GET Request to TfL and retrieve current service data for an Underground Line of my choice.

## Script Theory

The Script works in the following manner:

- Imports the necessary 3rd party libraries needed to work
- Presents the user with a list of available options to query
- Waits for input
- Makes a GET request to a specific TfL provided URL for line data
- Pulls, extracts and displays the requested information in a friendly format

## Caveats

Note that you must enter the Line names “Hammersmith-City” and “Waterloo-City” with the hyphen. Any other variants of the name and TfL wont recognise them.

## Expected Output

Should the Script execute as expected, we should receive output in the following form (taking the Central Line as an example):

```
Line: Central
Status: Good Service
```
