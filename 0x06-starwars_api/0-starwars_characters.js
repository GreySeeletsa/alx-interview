#!/usr/bin/node

// Import 'request' library
const request = require('request');

// Define constant with base URL of Star Wars API
const API_URL = 'https://swapi-api.alx-tools.com/api';

// Check if num of command line arguments is greater than 2
if (process.argv.length > 2) {
  // Make a request to film resource for specified film ID
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    // If an error occurred during request, log  error
    if (err) {
      console.log(err);
    }
    // Get char URL from film's response body
    const charactersURL = JSON.parse(body).characters;

    // Create an array of Promises that resolve with names of char
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        // Make a request to char resource
        request(url, (promiseErr, __, charactersReqBody) => {
          // If an error occurred during request, reject Promise with error
          if (promiseErr) {
            reject(promiseErr);
          }
          // Resolve Promise with name of char
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    // Wait for all Promises to resolve and log names of the char
    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
