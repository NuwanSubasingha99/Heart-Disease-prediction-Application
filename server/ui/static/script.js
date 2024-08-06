document.getElementById('predictionForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const data = {
        age: parseInt(document.querySelector('[name="age"]').value),
        sex: parseInt(document.querySelector('[name="sex"]').value),
        cp: parseInt(document.querySelector('[name="cp"]').value),
        trestbps: parseInt(document.querySelector('[name="trestbps"]').value),
        chol: parseInt(document.querySelector('[name="chol"]').value),
        fbs: parseInt(document.querySelector('[name="fbs"]').value),
        restecg: parseInt(document.querySelector('[name="restecg"]').value),
        thalach: parseInt(document.querySelector('[name="thalach"]').value),
        exang: parseInt(document.querySelector('[name="exang"]').value),
        oldpeak: parseFloat(document.querySelector('[name="oldpeak"]').value),
        slope: parseInt(document.querySelector('[name="slope"]').value),
        ca: parseInt(document.querySelector('[name="ca"]').value),
        thal: parseInt(document.querySelector('[name="thal"]').value)
    };
    // const formData = new FormData(event.target);
    // const formObject = {};
    // formData.forEach((value, key) => formObject[key] = value);

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)

    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerText =
                data.prediction ? `Prediction: The patient is ${data.prediction} to have heart disease.` :
                    `Error: ${data.error}`;
        })
        .catch(error => console.error('Error:', error));
});
