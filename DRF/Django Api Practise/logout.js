document.getElementById('logoutBtn').addEventListener('click', async function() {
  const token = localStorage.getItem('token');
  if (!token) {
    alert("You are not logged in.");
    return;
  }
  console.log(token);

  try {
    const response = await fetch('http://localhost:8000/patient/logout/', {  // <-- fixed here
      method: 'POST',
      headers: {
        'Authorization': 'Token ' + token,
        'Content-Type': 'application/json'
      },
    });

    if (response.ok) {
      localStorage.removeItem('token');
      window.location.href = "login.html";
    } else {
      alert("Logout failed or you're not logged in.");
    }
  } catch (error) {
    alert("Network error during logout.");
    console.error(error);
  }
});
