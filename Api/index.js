// start Api with npm start
const express = require('express');
const { promisify } = require('util');
const mysql = require('mysql');
const app = express();

// Connection stablished port 8080
const PORT = 8080;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// setting up connection parameters
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'joy_of_painting'
});

// promisify the query function
const queryAsync = promisify(connection.query).bind(connection);

// connect to db
connection.connect();

// Endpoint to get the information of the painting
app.get('/happy_bob', async (req, res) => {
    try {
        const rows = await queryAsync("SELECT * FROM happy_bob");
        res.json(rows);
    } catch (err) {
        console.error(err);
        res.status(500).send('Something happened');
    }
});

// Endpoint to get the paintings info by Month
app.get('/happy_bob/month/:month', async (req, res) => {
    const month = req.params.month;
    try {
        const rows = await queryAsync("SELECT * FROM happy_bob WHERE Month = ?", [month]);
        res.json(rows);
    } catch (err) {
        console.error(err);
        res.status(500).send('Something happened!');
    }
});

// Endpoint to get the paintings by subject
app.get('/happy_bob/subject/:subject', async (req, res) => {
    const subject = req.params.subject;
    const sqlQuery = `SELECT * FROM happy_bob WHERE Subject LIKE '%${subject}%'`;
    try {
        const rows = await queryAsync(sqlQuery);
        res.json(rows);
    } catch (err) {
        console.error('Error executing the query:', err);
        res.status(500).send('Internal server error');
    }
});

// Endpoint to get the paintings by color
app.get('/happy_bob/color/:color', async (req, res) => {
    const color = req.params.color;
    const sqlQuery = `SELECT * FROM happy_bob WHERE Colors LIKE '%${color}%'`;
    try {
        const rows = await queryAsync(sqlQuery);
        res.json(rows);
    } catch (err) {
        console.error('Error executing the query:', err);
        res.status(500).send('Internal server error');
    }
});

// it forces the connection to stop
// connection.end();
