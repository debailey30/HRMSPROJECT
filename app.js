const fs = require('fs');
const path = require('path');

// Step 1: Define the path to the config file
const configPath = path.join(__dirname, 'config.json');

// Step 2: Read and parse the config file
let config;
try {
    config = JSON.parse(fs.readFileSync(configPath, 'utf8'));
} catch (err) {
    if (err.code === 'ENOENT') {
        console.error(`Error: The config file at ${configPath} was not found.`);
    } else if (err.name === 'SyntaxError') {
        console.error(`Error: The config file at ${configPath} is not a valid JSON.`);
    } else {
        console.error(`Error: ${err.message}`);
    }
    config = {};
}

// Step 3: Access the configuration settings safely
const databaseHost = config.database?.host || 'default_host';
const serverPort = config.server?.port || 'default_port';
const loggingLevel = config.logging?.level || 'default_level';
const jwtSecret = config.security?.jwtSecret || 'default_secret';
const apiBaseUrl = config.api?.baseUrl || 'default_url';
const enableFeatureX = config.features?.enableFeatureX || false;

// Example usage in application logic
function connectToDatabase(host) {
    console.log(`Connecting to database at ${host}...`);
}

function startServer(port) {
    console.log(`Starting server on port ${port}...`);
}

connectToDatabase(databaseHost);
startServer(serverPort);
console.log('JWT Secret:', jwtSecret);
console.log('API Base URL:', apiBaseUrl);
console.log('Feature X Enabled:', enableFeatureX);

// Export the functions for testing
module.exports = {
    connectToDatabase,
    startServer
};