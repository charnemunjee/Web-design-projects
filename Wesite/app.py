
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET', 'dev_secret_key')

# Flask-Mail configuration (placeholders)
app.config.update(
    MAIL_SERVER = 'smtp.example.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USERNAME = 'your_email@example.com',
    MAIL_PASSWORD = 'your_email_password',
    MAIL_DEFAULT_SENDER = ('Movesby_Meg', 'your_email@example.com')
)

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clothing')
def clothing():
    items = [
        {'name':'VO2 Max Performance Tank','price':'R349','image':'/static/images/vo2_tank.jpg','desc':'Breathable training tank.'},
        {'name':'VO2 Max Compression Leggings','price':'R799','image':'/static/images/vo2_leggings.jpg','desc':'High-waist leggings for support.'},
        {'name':'VO2 Max Training Hoodie','price':'R999','image':'/static/images/vo2_hoodie.jpg','desc':'Lightweight warm-up hoodie.'}
    ]
    return render_template('clothing.html', items=items)

@app.route('/recipes')
def recipes():
    recipes = [
        {'title':'Green Protein Smoothie','desc':'Spinach, banana, protein powder, almond milk.','image':'/static/images/recipe1.jpg'},
        {'title':'Quinoa Buddha Bowl','desc':'Quinoa, roasted veg, chickpeas, tahini dressing.','image':'/static/images/recipe2.jpg'},
        {'title':'Baked Salmon & Veggies','desc':'Oven-baked salmon with lemon and seasonal vegetables.','image':'/static/images/recipe3.jpg'}
    ]
    return render_template('recipes.html', recipes=recipes)

@app.route('/testimonials')
def testimonials():
    notes = [
        {'author':'Samantha','text':'Meg transformed my energy and strength in 12 weeks!'},
        {'author':'Lerato','text':'Fun sessions, clear coaching and great results.'},
        {'author':'Daniel','text':'Professional and motivating — highly recommend.'}
    ]
    return render_template('testimonials.html', notes=notes)

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Send email via Flask-Mail (placeholder recipient)
        try:
            msg = Message(subject=f'Website contact from {name or "Guest"}',
                          recipients=['recipient@example.com'],
                          body=f'From: {name} <{email}>\n\n{message}')
            mail.send(msg)
            flash('Thanks {}, your message was sent.'.format(name or 'friend'))
        except Exception as e:
            # For demo, we'll flash a message but not fail
            flash('Message could not be sent (demo): {}'.format(str(e)))
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
