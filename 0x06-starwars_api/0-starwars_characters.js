#!/usr/bin/node
const request = require('request');

// Function to get movie details and print characters
function getStarWarsCharacters(movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  // Make request to SWAPI for the movie details
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error fetching data:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.log(`Failed to retrieve movie. Status code: ${response.statusCode}`);
      return;
    }

    const movieData = JSON.parse(body);

    // Retrieve characters list and print names
    const characters = movieData.characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error fetching character:', error);
          return;
        }

        if (response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        } else {
          console.log(`Failed to retrieve character. Status code: ${response.statusCode}`);
        }
      });
    });
  });
}

// Check for movie ID argument
const movieId = process.argv[2];
if (!movieId) {
  console.log('Please provide a movie ID as a positional argument.');
  process.exit(1);
}

// Call the function to get characters for the provided movie ID
getStarWarsCharacters(movieId);
