# SecureAuth - FastAPI Authentication System

A clean and professional authentication system built with FastAPI and styled with Tailwind CSS.

## Features

- **User Registration** - Create new accounts with validation
- **User Login** - Secure authentication with password hashing
- **Password Security** - bcrypt hashing with strength validation
- **Show/Hide Password** - Toggle password visibility
- **Responsive Design** - Works on desktop and mobile devices
- **Form Validation** - Real-time input validation
- **Professional UI** - Clean, minimalist design

## Screenshots

![alt text](image-2.png)

![alt text](image-1.png)

![alt text](image-3.png)
## Tech Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL with SQLAlchemy
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Icons**: Lucide Icons
- **Password Hashing**: bcrypt via Passlib
- **Validation**: Pydantic

## Installation

1. Clone the repository
```bash
git clone https://github.com/gajjarkav/Auth-System.git
cd authentication
```

2. Install dependencies using uv
```bash
uv sync
```

3. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your database URL
```

4. Run the application
```bash
uv run uvicorn app.main:app --reload
```

5. Open your browser and go to `http://127.0.0.1:8000`

## Environment Variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://username:password@host:port/database
```

## Project Structure

```
authentication/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── models.py        # Database models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # Database operations
│   ├── database.py      # Database configuration
│   ├── settings.py      # Application settings
│   └── templates/       # HTML templates
│       ├── base.html
│       ├── home.html
│       ├── login.html
│       └── register.html
├── .env                 # Environment variables
├── pyproject.toml       # Project dependencies
└── README.md
```

## API Endpoints

- `GET /` - Home page
- `GET /login` - Login page
- `POST /login` - User authentication
- `GET /register` - Registration page
- `POST /register` - User registration

## Usage

### Registration
1. Navigate to `/register`
2. Fill in username, email, and password
3. Password strength is validated in real-time
4. Submit the form to create your account

### Login
1. Navigate to `/login`
2. Enter your email and password
3. Use the eye icon to show/hide password
4. Submit to authenticate

## Development

This project uses:
- **uv** for dependency management
- **SQLAlchemy** for database operations
- **Jinja2** for HTML templating
- **Tailwind CSS** for styling

## License

MIT License

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request
