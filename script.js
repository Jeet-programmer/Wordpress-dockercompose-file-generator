function submitForm() {
    // Get values from the form
    var dockerFileName = document.getElementById('dockerFileName').value;
    var webUiPort = document.getElementById('webUiPort').value;
    var databasePort = document.getElementById('databasePort').value;

    // Build the query parameters string
    var queryParams = `?name=${encodeURIComponent(dockerFileName)}&web_port=${encodeURIComponent(webUiPort)}&db_port=${encodeURIComponent(databasePort)}`;

    // Send a GET request to the API to get the download URL
    var apiUrl = 'https://wp-docker.jeetghosh3.repl.co/download/' + queryParams; // Replace with your actual API URL
    window.location.href = apiUrl;

    var xhr = new XMLHttpRequest();
    xhr.open('GET', apiUrl, true);
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    xhr.setRequestHeader('Access-Control-Allow-Origin', '*'); // Allow cross-origin

    // Handle the response
    xhr.onload = function () {
        if (xhr.status == 200) {
            window.location.href = apiUrl;

            var response = JSON.parse(xhr.responseText);
            var downloadUrl = response.downloadUrl; // Adjust based on your API response

            // Redirect the page to the received download URL
            // window.location.href = downloadUrl;
        } else {
            console.error('Error fetching download URL');
        }
    };

    // Send the GET request
    xhr.send();
}
