from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Support page
@app.route('/support')
def support():
    return render_template('support.html')

# Hounds page
@app.route('/hounds')
def hounds():
    return render_template('hounds.html')

# Events page
@app.route('/events')
def events():
    return render_template('events.html')

# Donate page
@app.route('/donate')
def donate():
    return render_template('donate.html')

# Membership page
@app.route('/membership')
def membership():
    return render_template('membership.html')

# Jackie's Fund page
@app.route('/jackies-fund')
def jackies_fund():
    return render_template('jackies-fund.html')

# Volunteer page
@app.route('/volunteer')
def volunteer():
    return render_template('volunteer.html')

# Payments page
@app.route('/payments')
def payments():
    return render_template('payments.html')

# Footer
@app.context_processor
def inject_now():
    return {'current_year': datetime.now().year}

if __name__ == '__main__':
    app.run(debug=True)
