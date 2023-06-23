const express = require('express');
const sqlite3 = require('sqlite3').verbose();

const app = express();
const db = new sqlite3.Database(''); // Provide the path to your database file

// Example route to fetch data from the candidates table
app.get('/candidates', (req, res) => {
  db.all('SELECT * FROM candidates', (err, rows) => {
    if (err) {
      console.error(err);
      res.status(500).send('Internal Server Error');
    } else {
      res.json(rows);
    }
  });
});

// Start the server
app.listen(3000, () => {
  console.log('Server started on port 3000');
});
