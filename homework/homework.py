from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage
students = []


@app.route("/")
def home():
    return redirect(url_for("add_student"))


# ---------------------------------
# TODO: IMPLEMENT THIS ROUTE
# ---------------------------------
@app.route("/add", methods=["GET", "POST"])
def add_student():
    error = None

    if request.method == "POST":
        name = request.form.get("name")
        grade = request.form.get("grade")

        if not name or name.strip() == "":
            error = "Name is required"
        elif not grade or not grade.isdigit():
            error = "Grade must be a number"
        elif int(grade) < 0 or int(grade) > 100:
            error = "Grade must be between 0 and 100"
        else:
            students.append({"name": name, "grade": int(grade)})
            return redirect(url_for("display_students"))

    return render_template("add.html", error=error)


# ---------------------------------
# TODO: IMPLEMENT DISPLAY
# ---------------------------------
@app.route("/students")
def display_students():
    return render_template("students.html", students=students)


# ---------------------------------
# TODO: IMPLEMENT SUMMARY
# ---------------------------------
@app.route("/summary")
def summary():
    total_students = len(students)
    average_grade = None
    highest_grade = None
    lowest_grade = None

    if total_students > 0:
        grades = [student["grade"] for student in students]
        average_grade = sum(grades) / total_students
        highest_grade = max(grades)
        lowest_grade = min(grades)

    return render_template(
        "summary.html",
        total_students=total_students,
        average_grade=average_grade,
        highest_grade=highest_grade,
        lowest_grade=lowest_grade
    )


if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
