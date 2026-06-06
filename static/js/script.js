// Tab switching
document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const tabName = btn.getAttribute('data-tab');
        
        // Remove active class from all buttons and sections
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(section => section.classList.remove('active'));
        
        // Add active class to clicked button and corresponding section
        btn.classList.add('active');
        document.getElementById(tabName).classList.add('active');
    });
});

// Type Detection
function detectType() {
    const input = document.getElementById('typeInput').value.trim();
    
    if (!input) {
        alert('Please enter a value');
        return;
    }

    fetch('/api/detect-type', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ input: input })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('detectedType').textContent = data.type;
        document.getElementById('detectedValue').textContent = data.value;
        document.getElementById('typeResult').classList.remove('hidden');
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error detecting type');
    });
}

// Price Prediction
document.getElementById('priceForm').addEventListener('submit', (e) => {
    e.preventDefault();
    
    const engineSize = document.getElementById('engineSize').value;
    const horsepower = document.getElementById('horsepower').value;
    const age = document.getElementById('age').value;
    const mileage = document.getElementById('mileage').value;
    const brandValue = document.getElementById('brandValue').value;

    fetch('/api/predict-price', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            engine_size: engineSize,
            horsepower: horsepower,
            age: age,
            mileage: mileage,
            brand_value: brandValue
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById('predictedPrice').textContent = data.predicted_price.toLocaleString();
            document.getElementById('priceResult').classList.remove('hidden');
        } else {
            alert('Error: ' + data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error predicting price');
    });
});

// Batch Analysis
function analyzeValues() {
    const input = document.getElementById('batchInput').value.trim();
    const predict = document.getElementById('predictCheckbox').checked;
    
    if (!input) {
        alert('Please enter values');
        return;
    }

    // Parse input - split by comma or newline
    const values = input.split(/[,\n]+/).map(v => v.trim()).filter(v => v.length > 0);

    fetch('/api/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            inputs: values,
            predict: predict
        })
    })
    .then(response => response.json())
    .then(data => {
        displayBatchResults(data, values);
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error analyzing values');
    });
}

function displayBatchResults(data, originalValues) {
    let html = '<strong>Data Type Detection Results:</strong><br>';
    
    data.detected_types.forEach((result, index) => {
        html += `<div class="type-item">
                    <strong>Value ${index + 1}:</strong> "${originalValues[index]}" → <strong>${result.type}</strong>
                 </div>`;
    });

    document.getElementById('typesList').innerHTML = html;

    if (data.price_prediction && data.price_prediction.success) {
        const priceHtml = `<div style="margin-top: 20px; padding: 15px; background: #f1f8f4; border-left: 4px solid #4caf50; border-radius: 5px;">
                              <strong>Predicted Car Price:</strong> <span style="font-size: 1.5em; color: #4caf50; font-weight: bold;">$${data.price_prediction.predicted_price.toLocaleString()}</span>
                          </div>`;
        document.getElementById('priceInfo').innerHTML = priceHtml;
    } else {
        document.getElementById('priceInfo').innerHTML = '';
    }

    document.getElementById('batchResult').classList.remove('hidden');
}

// Allow Enter key for type detection
document.getElementById('typeInput').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        detectType();
    }
});
