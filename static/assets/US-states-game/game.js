const states = {}; // Object to hold state coordinates
const guessedStates = new Set(); // Set to track guessed states

// Load state data from CSV
$.get("static/assets/US-states-game/50_states_normalized.csv", function(data) {
    const lines = data.split('\n');
    lines.forEach((line, index) => {
        if (index === 0) return; // Skip header
        const [state, x, y] = line.split(',');
        states[state.trim()] = { x: parseInt(x), y: parseInt(y) };
    });
    console.log("States loaded:", states); // Debugging line
    drawMap();
});

// Function to draw the map
function drawMap() {
    const canvas = document.getElementById("usMap");
    const ctx = canvas.getContext("2d");

    // Load and draw the map image
    const img = new Image();
    img.src = "static/assets/US-states-game/blank_states_img.jpeg"; // Path to your image
    img.onload = () => {
        ctx.drawImage(img, 0, 0);
    };
}

// Function to convert input to title case
function toTitleCase(str) {
    return str
        .toLowerCase() // Convert the string to lowercase
        .split(' ') // Split the string into words
        .map(word => word.charAt(0).toUpperCase() + word.slice(1)) // Capitalize the first letter of each word
        .join(' '); // Join the words back into a single string
}

// Function to handle state submission
function submitState() {
    const inputField = document.getElementById("stateInput"); // Get the input field
    const answer = toTitleCase(inputField.value); // Use the new function
    console.log("Submitted state:", answer); // Debugging line

    if (states[answer] && !guessedStates.has(answer)) {
        guessedStates.add(answer);
        const { x, y } = states[answer];
        drawState(answer, x, y);
        document.getElementById("result").innerText = `${guessedStates.size}/${Object.keys(states).length} states guessed.`;

        if (guessedStates.size === Object.keys(states).length) {
            document.getElementById("result").innerText = "Great! You know all the states!";
        }
    } else if (guessedStates.has(answer)) {
        document.getElementById("result").innerText = "You've already guessed that state!";
    } else {
        document.getElementById("result").innerText = "State not found. Try again.";
    }

    inputField.value = ""; // Reset the input field
}

// Event listener for button click
document.getElementById("submitBtn").addEventListener("click", submitState);

// Event listener for pressing 'Enter' key
document.getElementById("stateInput").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        submitState();
    }
});

// Function to draw the guessed state on the map
function drawState(stateName, x, y) {
    const canvas = document.getElementById("usMap");
    const ctx = canvas.getContext("2d");
    ctx.font = "12px Arial";
    ctx.fillStyle = "black"; // Change text color if needed
    ctx.fillText(stateName, x, y);
}
