from flask import render_template, url_for, flash, redirect
from whr import app
from whr.models import User, Inquiry
from whr.forms import ContactForm

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/infographics')
def infographics():
    return render_template('infographics.html', title='Infographics')

@app.route('/dataset')
def dataset():
    return render_template('dataset.html', title='Data Set')

@app.route('/buzz')
def buzz():
    return render_template('buzz.html', title='Buzz')

@app.route('/faq')
def faq():
    return render_template('faq.html', title='FAQs')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Thank you!', 'success')
        return redirect(url_for('home'))
    return render_template('contact.html', title='Contact', form=form)