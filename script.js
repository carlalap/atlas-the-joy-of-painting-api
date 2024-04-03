// Define API base URL
const apiUrl = 'http://localhost:3000';

// Function to fetch paintings by month
async function getPaintingsByMonth(month) {
    try {
        const response = await fetch(`${apiUrl}/happy_bob/month/${month}`);
        const data = await response.json();
        // Handle data and update UI
    } catch (error) {
        console.error('Error fetching paintings by month:', error);
    }
}

// Function to fetch paintings by subject
async function getPaintingsBySubject(subject) {
    try {
        const response = await fetch(`${apiUrl}/happy_bob/subject/${subject}`);
        const data = await response.json();
        // Handle data and update UI
    } catch (error) {
        console.error('Error fetching paintings by subject:', error);
    }
}

// Function to fetch paintings by color
async function getPaintingsByColor(color) {
    try {
        const response = await fetch(`${apiUrl}/happy_bob/color/${color}`);
        const data = await response.json();
        // Handle data and update UI
    } catch (error) {
        console.error('Error fetching paintings by color:', error);
    }
}
