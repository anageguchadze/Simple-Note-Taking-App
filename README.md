# Django Notes Application

This project is a simple note-taking web application built using Django. It allows users to create, edit, and delete notes. Each note consists of a title, content, and a creation date.

## Features

- **View Notes**: List all notes stored in the database.
- **Add Note**: Create new notes by providing a title, content, and date of creation.
- **Edit Note**: Update the title of existing notes.
- **Delete Note**: Remove notes from the system.

## Models

1. **Note**
   - `title`: A string field that holds the note's title (max length: 50).
   - `content`: A text field that stores the content of the note.
   - `date_created`: A string field representing the date the note was created.

## Installation and Setup

### Prerequisites

- Python 3.x
- Django 4.x
- A virtual environment (recommended)

### Steps to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/anageguchadze/Simple-Note-Taking-App
