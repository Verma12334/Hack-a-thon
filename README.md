<!DOCTYPE html>
<html>
<head>
    <title>Predicting Vaccination Likelihood: A Multilabel Classification Problem</title>
</head>
<body>
    <h1>Problem Description</h1>
    <p>Your goal is to predict how likely individuals are to receive their <em>xyz</em> and seasonal flu vaccines.</p>
    <p>Specifically, you'll be predicting two probabilities: one for <strong>xyz_vaccine</strong> and one for <strong>seasonal_vaccine</strong>.</p>

    <h2>Labels</h2>
    <p>For this competition, there are two target variables:</p>
    <ul>
        <li><strong>xyz_vaccine</strong> - Whether respondent received xyz flu vaccine.</li>
        <li><strong>seasonal_vaccine</strong> - Whether respondent received seasonal flu vaccine.</li>
    </ul>
    <p>Both are binary variables: 0 = No; 1 = Yes. Some respondents didn't get either vaccine, others got only one, and some got both. This is formulated as a multilabel (and not multiclass) problem.</p>
</body>
</html>
