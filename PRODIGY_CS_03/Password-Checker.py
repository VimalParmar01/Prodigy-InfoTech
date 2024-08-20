<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Password Complexity Checker</title>
    <style>
        body {
            background-color: #c7c4c4;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 0px 10px rgb(144, 137, 137);
            text-align: center;
            max-width: 400px;
            width: 100%;
        }

        h1 {
            font-size: 24px;
            margin-bottom: 20px;
            color: #333333;
        }

        input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #dddddd;
            border-radius: 4px;
            font-size: 16px;
        }

        #feedback {
            font-size: 18px;
            padding: 10px;
            border-radius: 4px;
            display: none;
        }

        .weak {
            color: #ff4d4d;
            background-color: #ffe6e6;
            border: 1px solid #ff4d4d;
        }

        .medium {
            color: #ffa500;
            background-color: #fff2cc;
            border: 1px solid #ffa500;
        }

        .strong {
            color: #28a745;
            background-color: #e6ffed;
            border: 1px solid #28a745;
        }

        .very-strong {
            color: #007bff;
            background-color: #e6f0ff;
            border: 1px solid #007bff;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Password Complexity Checker</h1>
        <input type="password" id="password" placeholder="Enter your password">
        <div id="feedback"></div>
    </div>
    <script>
        const passwordInput = document.getElementById('password');
        const feedback = document.getElementById('feedback');

        passwordInput.addEventListener('input', () => {
            const password = passwordInput.value;
            let strength = '';
            let score = 0;

            // Criteria for password strength
            const lengthCriteria = password.length >= 8;
            const uppercaseCriteria = /[A-Z]/.test(password);
            const lowercaseCriteria = /[a-z]/.test(password);
            const numberCriteria = /\d/.test(password);
            const specialCharCriteria = /[!@#\$%\^&\*]/.test(password);

            // Score calculation
            if (lengthCriteria) score++;
            if (uppercaseCriteria) score++;
            if (lowercaseCriteria) score++;
            if (numberCriteria) score++;
            if (specialCharCriteria) score++;

            // Determine password strength
            if (score <= 2) {
                strength = 'Weak';
                feedback.className = 'weak';
            } else if (score === 3) {
                strength = 'Medium';
                feedback.className = 'medium';
            } else if (score === 4) {
                strength = 'Strong';
                feedback.className = 'strong';
            } else if (score === 5) {
                strength = 'Very Strong';
                feedback.className = 'very-strong';
            }

            // Display feedback
            feedback.textContent = `Password Strength: ${strength}`;
            feedback.style.display = 'block';
        });
    </script>
</body>
</html>
