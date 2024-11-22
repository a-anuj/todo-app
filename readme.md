# To-Do List Application with Flask and PostgreSQL

## Introduction

This is a simple To-Do List web application built using **Flask**, **PostgreSQL**, and **Bootstrap**. It allows users to register, log in, and manage their tasks with features like marking tasks as complete, adding new tasks, and deleting tasks.

---

## Features

- **User Authentication**:
  - Register new users with a username and password.
  - Secure login with password hashing.
  - User-specific task management.
  
- **Task Management**:
  - Add new tasks.
  - Mark tasks as complete or incomplete.
  - Delete tasks.
  
- **Visual Design**:
  - Responsive layout powered by **Bootstrap**.
  - Task images can be added to enhance visualization.

- **Database**:
  - **PostgreSQL** is used to store user information and tasks.

---

## Prerequisites

Before running this application, you need the following:

- Python 3.10 or higher
- PostgreSQL database
- A virtual environment to manage dependencies

---

## Installation Guide

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/a-anuj/todo-app.git
cd todo-list-app
```

### Step 2 : Set-Up the virtual environment
- For linux/macOS

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
- For windows

    ```
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

### Step 3 : Initialize the database
- Create the database in the pgadmin application

### Step 4 : Run the Application
```bash
python app.py
```

## Screenshots

1. **Login Page**:
   ![Login Page](images/Screenshot%20from%202024-11-22%2015-51-02.png)

2. **To-Do List Page**:
   ![To-Do List Page](images/Screenshot%20from%202024-11-22%2015-51-22.png)
