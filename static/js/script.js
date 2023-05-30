// Function that updates the download button's text when the download starts
function startDownload() {
  // Access the download-button element by its ID and change its innerHTML
  document.getElementById('download-button').innerHTML = 'Téléchargement en cours...';
}

// Function to refresh the current page
function refreshPage() {
  // Reload the current document
  window.location.reload();
}

// Event that fires after the HTML document has been completely loaded
document.addEventListener('DOMContentLoaded', (event) => {
  // Attempt to get the "output-format" cookie
  let outputFormatCookie = getCookie("output-format");
  
  // If the cookie exists, set the input field's value to the cookie's value
  if(outputFormatCookie) {
      document.getElementById('output-format').value = outputFormatCookie;
  }
});

// Listen for changes in the input field
document.getElementById('output-format').addEventListener('change', (event) => {
  // On change, set a new "output-format" cookie with the input's new value, which expires in 30 days
  setCookie("output-format", event.target.value, 30);
});

// Function to set a cookie
function setCookie(name, value, days) {
  // Create a new date instance
  let date = new Date();
  // Set the date to now plus the number of days to keep the cookie
  date.setTime(date.getTime() + (days*24*60*60*1000));
  // Define the time at which the cookie should expire
  let expires = "expires=" + date.toUTCString();
  // Set the cookie with the specified name, value, expiration time, and path
  document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

// Function to get a cookie by name
function getCookie(name) {
  // Define the search string
  let nameEQ = name + "=";
  // Split the document's cookies into an array
  let ca = document.cookie.split(';');
  // Loop through the array of cookies
  for(let i = 0; i < ca.length; i++) {
      let c = ca[i];
      // Remove leading whitespaces
      while (c.charAt(0) == ' ') c = c.substring(1, c.length);
      // If the cookie with the specified name is found, return its value
      if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
  }
  // If the cookie with the specified name isn't found, return null
  return null;
}
