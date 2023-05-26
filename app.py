from flask import Flask, render_template, request
from main import get_completion, get_prompt_response
from static_html import nav, scripts
app = Flask(__name__)

props = {"nav": nav, "scripts": scripts}

@app.route('/')
def index():
    return render_template('index.html', **props)


@app.route('/communication/student-narratives')
def student_narrative():
    return render_template('student-narratives.html', **props)


@app.route('/communication/course-narrative')
def course_narrative():
    return render_template('course-narrative.html', **props)


@app.route('/communication/parent-email')
def parent_email():
    return render_template('parent-email.html', **props)


@app.route('/communication/student-email')
def student_email():
    return render_template('student-email.html', **props)


@app.route('/planning/lesson-plan')
def lesson_plan():
    return render_template('lesson-plan.html', **props)


@app.route('/planning/emergency-sub')
def emergency_sub():
    return render_template('emergency-sub.html', **props)


@app.route('/planning/study-guides')
def study_guide():
    return render_template('study-guides.html', **props)


@app.route('/assessment/vocabulary-quiz')
def vocab_quiz():
    return render_template('vocab-quiz.html', **props)


@app.route('/assessment/formative-assessment')
def formative_assessment():
    return render_template('formative-assessment.html', **props)


@app.route('/get-completion')
def completion_handler():
    course_name = request.args.get('course_name')
    student_name = request.args.get('student_name')
    adjectives = request.args.get('adjectives')
    areas_for_improvement = request.args.get('areas_for_improvement')

    completion = get_completion(course_name, student_name, adjectives, areas_for_improvement)
    return completion


@app.route('/get-prompt-response')
def prompt_response():
    prompt = request.args.get('prompt')
    temp = request.args.get('temp')
    max_tokens = request.args.get('max_tokens')

    response = get_prompt_response(prompt, temp, max_tokens)
    return response


if __name__ == '__main__':
    app.run(debug=True)
