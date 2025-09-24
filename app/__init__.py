"""

THIS IS THE OVERALL STRUCTURE OF THE TO DO LIST BACKEND APP

======================================================================
app/                                                                 |
├── main.py         # entry point                                    |
├── models/         # contains all Pydantic / DB models              |
│   ├── __init__.py                                                  |
│   ├── task.py                                                      |
│   ├── habit.py                                                     |
│   └── mood.py                                                      |
├── routes/         # optional but good for separating endpoints     |
│   ├── __init__.py                                                  |
│   ├── task_routes.py                                               |
│   ├── habit_routes.py                                              |
│   └── mood_routes.py                                               |
└── database/       # optional now, for later DB integration         |
    ├── __init__.py                                                  |
    └── db.py                                                        |
======================================================================
"""