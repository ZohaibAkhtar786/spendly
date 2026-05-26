# Spec: Registration

## Overview
Implement the POST handler for the `/register` route so users can create an account. The registration template and users table already exist from step 01. This step wires them together — accepting form data, validating uniqueness, hashing the password, inserting into the database, and starting the user session.

## Depends on
- Step 01 — Database Setup (users table + werkzeug already available)

## Routes
- `POST /register` — process registration form — public (no existing session)

The `GET /register` route already exists and renders `register.html`.

## Database changes
No new tables or columns. The `users` table from step 01 has everything needed.

## Templates
- **Create:** none
- **Modify:** none — `templates/register.html` already has the form, error block, and POST action

## Files to change
- `app.py` — add POST handling to the `/register` route

## Files to create
None

## New dependencies
No new dependencies (werkzeug and sqlite3 already available)

## Rules for implementation
- No SQLAlchemy or ORMs
- Parameterised queries only
- Passwords hashed with werkzeug (`generate_password_hash`)
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`
- Do not use Flask-Login — session management is manual via Flask's built-in `session`
- After successful registration, store `user_id` and `user_name` in `session` so the user is logged in
- Redirect to a dashboard/home route after successful registration (even if that route is a placeholder)

## Definition of done
- [ ] Submitting the registration form with valid data creates a new user row
- [ ] Password is stored hashed, not plaintext
- [ ] Duplicate email shows an error message on the form
- [ ] Empty name, email, or password shows an error
- [ ] Password shorter than 8 characters shows an error
- [ ] Successful registration sets Flask session and redirects to `/`
- [ ] App starts without errors and `GET /register` still renders the form