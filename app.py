from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    data = {
        "alumni": [
            {"name": "Pyush sir", "company": "Google", "image": "pyush.png"},
            {"name": "Priya Verma", "company": "Amazon", "image": "alumni2.jpg"},
            {"name": "Ajay Kumar", "company": "Microsoft", "image": "alumni3.jpg"},
            {"name": "Sneha Singh", "company": "Adobe", "image": "alumni4.jpg"},
            {"name": "Vikas Mehta", "company": "Tesla", "image": "alumni5.jpg"}
        ],
        "packages": [
            {"name": "Aryan Gupta", "company": "Google", "image": "package1.jpg"},
            {"name": "Shreya Das", "company": "Amazon", "image": "package2.jpg"},
            {"name": "Kunal Jain", "company": "Microsoft", "image": "package3.jpg"},
            {"name": "Niharika Patel", "company": "Adobe", "image": "package4.jpg"},
            {"name": "Manoj Yadav", "company": "Tesla", "image": "package5.jpg"}
        ],
        "gate_scores": [
            {"rank": 1, "name": "Aman Jain", "image": "pyush.jpg"},
            {"rank": 2, "name": "Anjali Gupta", "image": "gate2.jpg"},
            {"rank": 5, "name": "Ravi Kumar", "image": "gate3.jpg"},
            {"rank": 8, "name": "Sonal Sharma", "image": "gate4.jpg"},
            {"rank": 10, "name": "Rajiv Singh", "image": "gate5.jpg"}
        ],
        "workshops": [
            {"topic": "AI & ML", "image": "workshop1.jpg"},
            {"topic": "Cloud Computing", "image": "workshop2.jpg"},
            {"topic": "Cybersecurity", "image": "workshop3.jpg"},
            {"topic": "IoT", "image": "workshop4.jpg"},
            {"topic": "Blockchain", "image": "workshop5.jpg"}
        ]
    }
    return render_template('home.html', data=data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/departments')
def departments():
    return render_template('departments.html')


@app.route('/departments/<department_name>')
def department_detail(department_name):
    hods_with_images = {
        "CSE": [
            {"name": "Dr. Mayank Aggrawal", "image": "Mayank_sir.png"},
            {"name": "Suyash Gupta", "image": "Suyash_sir.png"},
            {"name": "Rahul Singh", "image": "hod3.jpg"},
            {"name": "Aditi Sharma", "image": "hod4.jpg"},
            {"name": "Ankit Raj", "image": "hod5.jpg"}
        ],
        "ECE": [
            {"name": "Prof. Vipul Sharma", "image": "Dean_sir.png"},
            {"name": "Dr. Tanuj Sir", "image": "Tanuj_sir.png"},
            {"name": "Rahul Singh", "image": "hod3.jpg"},
            {"name": "Aditi Sharma", "image": "hod4.jpg"},
            {"name": "Ankit Raj", "image": "hod5.jpg"}
        ],
        "EE": [
            {"name": "Mayank Aggrawal", "image": "hod1.jpg"},
            {"name": "Suyash Gupta", "image": "hod2.jpg"},
            {"name": "Rahul Singh", "image": "hod3.jpg"},
            {"name": "Aditi Sharma", "image": "hod4.jpg"},
            {"name": "Ankit Raj", "image": "hod5.jpg"}
        ],
        "ME": [
            {"name": "Mayank Aggrawal", "image": "hod1.jpg"},
            {"name": "Suyash Gupta", "image": "hod2.jpg"},
            {"name": "Rahul Singh", "image": "hod3.jpg"},
            {"name": "Aditi Sharma", "image": "hod4.jpg"},
            {"name": "Ankit Raj", "image": "hod5.jpg"}
        ]
    }
    return render_template(
        'department_detail.html',
        department=department_name,
        hods=hods_with_images[department_name]
    )


@app.route('/courses')
def courses():
    return render_template('courses.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
