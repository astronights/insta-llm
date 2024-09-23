from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data: An image and the options to choose from
image_url = "https://example.com/path-to-your-image.jpg"  # Replace with your actual image URL
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

@app.route('/')
def index():
    return render_template('index.html', image_url=image_url, options=options)

@app.route('/submit_choice', methods=['POST'])
def submit_choice():
    choice = request.form.get('choice')
    # Do something with the choice, e.g., save it to a database
    print(f"User selected: {choice}")
    
    # Redirect back to the main page or a confirmation page
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
