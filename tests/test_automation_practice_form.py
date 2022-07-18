__author__ = 'miserylab'



from demoqa_tests.app import app
from demoqa_tests.data import Student, Gender, Subjects, Hobbies


def test_student_registration_form():
    app.given_student_registration_form_opened()

    # WHEN
    app.form.set_first_name(Student.name) \
        .set_last_name(Student.surname) \
        .set_email(Student.email) \
        .set_gender(Gender.female) \
        .set_number(Student.mobile_number) \
        .set_date_of_birth(Student.year, Student.month, Student.day) \
        .set_subjects(Subjects.computer_science, Subjects.english) \
        .set_hobbies(Hobbies.reading, Hobbies.music) \
        .upload_picture(Student.image) \
        .set_current_address(Student.address) \
        .set_state(Student.state) \
        .set_city(Student.city) \
        .submit()


    # THEN

    app.results.should_have_row_with_exact_texts(0, 1, Student.name, Student.surname)
    app.results.should_have_row_with_exact_texts(1, 1, Student.email)
    app.results.should_have_row_with_exact_texts(2, 1, Gender.female)
    app.results.should_have_row_with_exact_texts(3, 1, Student.mobile_number)
    app.results.should_have_row_with_exact_texts(4, 1, Student.date_of_birth)
    app.results.should_have_row_with_exact_texts(5, 1, Subjects.computer_science, Subjects.english)
    app.results.should_have_row_with_exact_texts(6, 1, Hobbies.reading, Hobbies.music)
    app.results.should_have_row_with_exact_texts(7, 1, Student.image)
    app.results.should_have_row_with_exact_texts(8, 1, Student.address)
    app.results.should_have_row_with_exact_texts(9, 1, Student.state, Student.city)
