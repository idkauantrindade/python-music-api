# Python Music API

A **lightweight and easy-to-use music management API** built with **Python**.  
Supports **track and album retrieval**, **playlist management**, and **audio streaming**.  
The system can be used as a **CLI tool** or integrated into other Python projects.

---

## Table of Contents

- [Features](#features)  
- [Technologies](#technologies)  
- [Installation](#installation)  
- [Usage](#usage)  

---

## Features

- Search tracks, albums, and artists by name or genre  
- Retrieve detailed track and album information  
- Manage playlists: create, update, delete  
- Stream audio files  
- Lightweight, easy to integrate into Python projects  

---

## Technologies

- **Python 3.x** – core programming language  
- **Flask** – optional for API endpoints  
- **SQLite/MySQL** – database for storing music and playlists  
- **requests** – for handling HTTP requests  
- **pydub** or **pygame** – optional libraries for audio playback  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/python-music-api.git
```

2. Install the package

```bash
pip install python-music-api
```
---

## Usage

1. Running the API

```bash
uvicorn main:app --reload  
```

2. Accessing the API

```bash
http://127.0.0.1:8000/musics/<music_name>
```
