const firebase = require('firebase/app');
require('firebase/firestore'); // Import the Firestore module if you need it

const firebaseConfig = {
  apiKey: "AIzaSyBMsTrZWHksrZhddX9iS1VgFQ54wMrP9lc",
  authDomain: "testjob-409b8.firebaseapp.com",
  projectId: "testjob-409b8",
  storageBucket: "testjob-409b8.appspot.com",
  messagingSenderId: "973850947957",
  appId: "1:973850947957:web:e1e82dfd8c4b11ec05e33c",
  measurementId: "G-35J6TPLQ9M"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();

// Access the form element
const form = document.querySelector('#sec-a2ae form');

// Handle form submission
form.addEventListener('submit', async (event) => {
  event.preventDefault();

  // Get form field values
  const nameInput = document.querySelector('#name-c07d');
  const emailInput = document.querySelector('#email-c07d');
  const skillsInput = document.querySelector('#skillsinput-23123');
  const salaryInput = document.querySelector('#text-8b19');
  const jobTypeInput = document.querySelector('#text-9e22');
  const phoneInput = document.querySelector('#phone-17ec');

  const name = nameInput.value;
  const email = emailInput.value;
  const skills = skillsInput.value;
  const salary = salaryInput.value;
  const jobType = jobTypeInput.value;
  const phone = phoneInput.value;

  try {
    // Store data in Firestore
    await db.collection('candidates').add({
      name,
      email,
      skills,
      salary,
      jobType,
      phone,
    });

    // Reset form fields
    form.reset();
    // Show success message or redirect to another page
    alert('Form submitted successfully!');
  } catch (error) {
    console.error('Error adding document:', error);

    // Extract the error message
    let errorMessage = 'Error submitting form. Please try again.';
    if (error instanceof Error && error.message) {
      errorMessage = error.message;
    }

    // Show error message to the user
    const errorMessageElement = document.querySelector('.u-form-send-error');
    errorMessageElement.textContent = errorMessage;
    errorMessageElement.style.display = 'block';
  }
});