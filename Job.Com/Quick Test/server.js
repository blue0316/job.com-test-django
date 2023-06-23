const express = require('express');
const sqlite3 = require('sqlite3').verbose();

const app = express();
const db = new sqlite3.Database('./database/jobdatabase.db');

// Enable detailed error reporting in development
if (app.get('env') === 'development') {
  app.use((err, req, res, next) => {
    res.status(err.status || 500);
    res.send({
      error: {
        message: err.message,
        error: err,
      },
    });
  });
}


// Add the body parsing middleware
app.use(express.urlencoded({ extended: true }));

// Route handler for form submission
app.post('/submit', (req, res) => {
  // Code for form submission
  // ...
});

// Route handler for fetching candidates data
app.get('/candidates', (req, res) => {
  try {
    db.all('SELECT * FROM candidates', (err, rows) => {
      if (err) {
        console.error(err);
        res.status(500).send('Internal Server Error');
      } else {
        res.json(rows);
      }
    });
  } catch (error) {
    console.error(error);
    res.status(500).send('Internal Server Error');
  }
});


// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
