% Import necessary libraries
:- use_module(library(csv)).
:- use_module(library(http/thread_httpd)).
:- use_module(library(http/http_dispatch)).
:- use_module(library(http/http_parameters)).
:- use_module(library(http/http_json)).

% Dynamic facts for storing student data
:- dynamic student/3.

% Load CSV data into Prolog
load_csv(File) :-
    csv_read_file(File, Rows, [functor(student), arity(3)]),
    maplist(assert, Rows).

% Rules to check eligibility
eligible_for_scholarship(Student_ID) :-
    student(Student_ID, Attendance_percentage, CGPA),
    Attendance_percentage >= 75,
    CGPA >= 9.0.

permitted_for_exam(Student_ID) :-
    student(Student_ID, Attendance_percentage, _),
    Attendance_percentage >= 75.

% REST API Handlers
:- http_handler('/check_scholarship', check_scholarship, []).
:- http_handler('/check_exam_permission', check_exam_permission, []).

% Start the HTTP server
start_server(Port) :-
    http_server(http_dispatch, [port(Port)]).

% Handlers for the endpoints
check_scholarship(Request) :-
    http_parameters(Request, [student_id(Student_ID, [atom])]),
    (eligible_for_scholarship(Student_ID) ->
        Reply = json{status: "eligible"};
        Reply = json{status: "not eligible"}),
    reply_json(Reply).

check_exam_permission(Request) :-
    http_parameters(Request, [student_id(Student_ID, [atom])]),
    (permitted_for_exam(Student_ID) ->
        Reply = json{status: "permitted"};
        Reply = json{status: "not permitted"}),
    reply_json(Reply).