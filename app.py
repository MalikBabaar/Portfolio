from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html',
                           name="Malik Muhammad Babar Khan",
                           title="AI Engineer at Systems Limited",
                           email="malikbabarkhan.sherpao@gmail.com",
                           location="Islamabad, Pakistan",
                           phone="+92-312-0960604",
                           about=(
                               "I am an AI Engineer at Systems Limited passionate about building intelligent systems. "
                               "I specialize in machine learning, deep learning, and full-stack development."
                           ),
                           skills=[
                               "Python", "PyTorch", "TensorFlow", "Flask", "Pandas", "NumPy",
                               "Scikit-learn", "Matplotlib", "Seaborn", "HTML", "CSS", "JavaScript"
                           ],
                           education=[
                               {"degree": "BS in Computer Science", "institution": "Agriculture University of Peshawar", "year": "2021"},
                               {"degree": "MS in Computer Science", "institution": "Agriculture University of Peshawar", "year": "2025"}
                           ])

# Projects route
@app.route('/projects')
def projects():
    projects_list = [
        {"title": "Image Classifier", "description": "CNN-based image classification model using PyTorch", "url": "#"},
        {"title": "House Price Prediction", "description": "Linear regression model for housing prices", "url": "#"},
        {"title": "Attan Dance Classification", "description": "Used CNN and LSTM for traditional dance classification", "url": "#"}
    ]
    return render_template('projects.html', projects=projects_list)

# About route
@app.route('/about')
def about():
    return render_template('about.html',
                           name="Malik Muhammad Babar Khan",
                           email="malikbabarkhan.sherpao@gmail.com",
                           location="Islamabad, Pakistan",
                           phone="+92-312-0960604",
                           about=(
                               "I am a passionate AI engineer with experience in designing and deploying machine learning models. "
                               "Currently working at Systems Limited to deliver cutting-edge AI solutions."
                           ))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
