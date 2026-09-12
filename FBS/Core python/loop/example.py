<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Phishing URL Detector</title>
  <style>
    body { max-width: 720px; margin: 64px auto; padding: 0 20px; font: 16px/1.5 Arial, sans-serif; background: #f6f8fb; color: #172033; }
    main { background: white; padding: 32px; border-radius: 14px; box-shadow: 0 6px 22px #17203318; }
    input { width: 100%; box-sizing: border-box; padding: 12px; border: 1px solid #aab3c2; border-radius: 7px; font-size: 16px; }
    button { margin-top: 12px; padding: 11px 18px; border: 0; border-radius: 7px; background: #155eef; color: white; font-weight: bold; cursor: pointer; }
    .card { margin-top: 24px; padding: 18px; border-radius: 8px; background: #f1f5f9; }
    .danger { color: #b42318; } .safe { color: #067647; } .error { color: #b42318; }
    code { word-break: break-all;}
  </style>
</head>
<body><main>
  <h1>Two-Phase Phishing Detector</h1>
  <p>URL आणि domain feature .</p>
  <form method="post"><input name="url" required placeholder="https://example.com/login"><button type="submit">Check URL</button></form>
  {% if error %}<p class="error">{{ error }}</p>{% endif %}
  {% if result %}<section class="card"><h2 class="{{ 'danger' if result.result == 'Phishing' else 'safe' }}">{{ result.result }}</h2>
    <p>Phishing probability: <strong>{{ result.phishing_probability }}%</strong></p><code>{{ result.url }}</code></section>{% endif %}
</main></body></html>