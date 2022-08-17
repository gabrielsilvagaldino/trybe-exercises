// apiScript.js
const API_URL = 'https://icanhazdadjoke.com/';

const fetchJoke = () => {

  const myObject = {
    method: 'GET',
    headers: { 'Accept': 'application/json' }
  };

  fetch(API_URL, myObject)
    .then((response) => {
      console.log(response);
      return response.json()
    })
    .then((data) => {
      const id = document.querySelector('#jokeContainer')
      id.innerHTML = data.joke
    })
  
};

window.onload = () => fetchJoke();