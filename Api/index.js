// exec npm start within Api to start app
const express = require('express');
const app = express();

// Connection stablished port 8080
const PORT = 8080;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

var mysql = require('mysql');

// setting up connection parameters
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'joy_of_painting'
});

// connect to db
connection.connect();

// Endpoint to get the information of the painting
app.get('/happy_bob', (req, res) => {
    connection.query("SELECT * FROM happy_bob", (err, rows) => {
        if (err) {
            console.error(err);
            res.status(500).send('Something happened');
        } else {
            res.json(rows);
        }
    });
});

// Endpoint to get the paintings info by Month
app.get('/happy_bob/month/:month', (req, res) => {
    const month = req.params.month;
    connection.query("SELECT * FROM happy_bob WHERE Month = ?", [month], (err, rows) => {
        if (err) {
            console.error(err);
            res.status(500).send('Something happened!');
        } else {
            res.json(rows);
        }
    });
});

// Endpoint para obtener las pinturas por tema
app.get('/happy_bob/subject/:subject', (req, res) => {
    const subject = req.params.subject; // Get the theme provided in the URL
    // SQL query to select paintings with the provided theme
    const sqlQuery = `SELECT * FROM happy_bob WHERE Subject LIKE '%${subject}%'`;
    
    // Execute the query in the database
    connection.query(sqlQuery, (err, results) => {
        if (err) {
            console.error('Error executing the query:', err);
            res.status(500).send('Internal server error');
            return;
        }
        // Send the results as a response
        res.json(results);
    });
});

// Endpoint para obtener las pinturas por color
app.get('/happy_bob/color/:color', (req, res) => {
    const color = req.params.color; // Get the theme provided in the URL
    // SQL query to select paintings with the provided theme
    const sqlQuery = `SELECT * FROM happy_bob WHERE Colors LIKE '%${color}%'`;
    
    // Execute the query in the database
    connection.query(sqlQuery, (err, results) => {
        if (err) {
            console.error('Error executing the query:', err);
            res.status(500).send('Internal server error');
            return;
        }
        // Send the results as a response
        res.json(results);
    });
});

// Close connection
connection.end();