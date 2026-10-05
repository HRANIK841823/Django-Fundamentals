const patient = () => {
    fetch('http://127.0.0.1:8000/patient/list/?format=json')
        .then(res => res.json())
        .then(data => displayPatient(data))

}
const displayPatient = (patients) => {
    patients.forEach(element => {
        const container = document.getElementById('patientContainer');
        const div = document.createElement('div');
        div.className="w-96 border border-gray-200 mt-10 mx-auto p-6 rounded-2xl";
        div.innerHTML = `
        <img class="" src="${element.image}" alt="">
        <h3>Patient Mobile Number: ${element.mobile}</h3>
        <h3>User ID: ${element.user}</h3>
        `;
        container.appendChild(div);

    });
}
patient();
document.getElementById('userForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm_password').value;

    if (password !== confirmPassword) {
        alert("Passwords do not match!");
        return;
    }

    const formData = new FormData();
    formData.append('username', document.getElementById('username').value);
    formData.append('first_name', document.getElementById('first_name').value);
    formData.append('last_name', document.getElementById('last_name').value);
    formData.append('email', document.getElementById('email').value);
    formData.append('password', password);
    formData.append('confirm_password',confirmPassword);
    fetch('http://127.0.0.1:8000/patient/register/', {
        method: 'POST',
        body: formData
    })
    .then(res => {
        if (res.ok) {
            alert("User registered successfully!");
            document.getElementById('userForm').reset();
        } else {
            return res.json().then(err => {
                console.error(err);
                alert("Registration failed. See console for errors.");
            });
        }
    })
    .catch(err => {
        console.error(err);
        alert("Something went wrong.");
    });
});





