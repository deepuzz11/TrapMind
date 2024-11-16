window.onload = function() {
    fetch('/get_attack_data')
        .then(response => response.json())
        .then(data => {
            document.getElementById('attackData').innerHTML = `
                <p><strong>Attack Type:</strong> ${data.attack_type}</p>
                <p><strong>Details:</strong> ${data.details}</p>
            `;
        })
        .catch(error => console.error('Error fetching attack data:', error));
};

function simulateVulnerability() {
    fetch('/simulate_vulnerability')
        .then(response => response.json())
        .then(data => {
            alert('Simulated Vulnerability: ' + data.vulnerability);
        })
        .catch(error => console.error('Error simulating vulnerability:', error));
}
