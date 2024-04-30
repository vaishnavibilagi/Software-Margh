from flask import *
app=Flask(__name__)

#home page
@app.route('/')
def home():
    return render_template('home.html')

#about swm
@app.route('/about')
def about():
    return render_template('about.html')

#guide registration
@app.route('/guideregister')
def guideregister():
    return render_template('guideregister.html')

#student registration
@app.route('/sturegister')
def sturegister():
    return render_template('sturegister.html')

#guide login 
@app.route('/guidelogin')
def guidelogin():
    return render_template('guidelogin.html')

#student login
@app.route('/stulogin')
def stulogin():
    return render_template('stulogin.html')


#view for guide
@app.route('/guideprofile')
def guideprofile():
    return render_template('guideprofile.html')

#contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/go_to')
def go_to():
    return render_template('go_to.html')
@app.route('/download_pdf')
def download_pdf():
    filename = 'certificate.pdf'
    return send_file(filename, as_attachment=True)
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/prolang')
def prolang():
    return render_template('prolang.html')

@app.route('/webdev')
def webdev():
    return render_template('webdev.html')

@app.route('/frameworks')
def frameworks():
    return render_template('frameworks.html')

@app.route('/mobileapp')
def mobileapp():
    return render_template('mobileapp.html')

@app.route('/data_ana')
def data_ana():
    return render_template('data_ana.html')

@app.route('/cyber')
def cyber():
    return render_template('cyber.html')

@app.route('/software')
def software():
    return render_template('software.html')

@app.route('/cloud')
def cloud():
    return render_template('cloud.html')

@app.route('/ai')
def ai():
    return render_template('ai.html')

