# Spec: Login And Logout

## Overview

Implement user authentication by adding login and logout functionality to Spendly. Users will be able to log in with their email and password, and log out to end their session. This builds on the registration feature from step 02, completing the core authentication flow.

## Depends on

- Step 01 — Database Setup (users table exists)
- Step 02 — Registration (users can register and passwords are hashed)

## Routes

- `POST /login` — process login form — public
- `GET /logout` — log out user and redirect — logged-in

The `GET /login` route already exists as a placeholder rendering `login.html`.
The `GET /logout` route exists as a placeholder returning text.

## Database changes

No database changes. The `users` table from step 01 has everything needed.

## Templates

- **Create:** none
- **Modify:** none — `templates/login.html` already has the form, error block, and POST action

## Files to change

- `app.py` — add POST handling to `/login` route, implement `/logout` route
- `templates/login.html` — if modifications needed (e.g., flash messages, error display)

## Files to create

None

## New dependencies

No new dependencies (werkzeug and sqlite3 already available)

## Rules for implementation

- No SQLAlchemy or ORMs
- Parameterised queries only
- Passwords verified with werkzeug (`check_password_hash`)
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`
- Do not use Flask-Login — session management is manual via Flask's built-in `session`
- After successful login, store `user_id` and `user_name` in `session`
- Redirect to dashboard/home route after successful login
- Logout clears the session and redirects to landing page
- Show error message for invalid email/password combinations

## Definition of done

- [ ] Submitting login form with valid credentials logs user in
- [ ] Invalid email shows error message on form
- [ ] Invalid password shows error message on form
- [ ] Empty email or password shows error message
- [ ] Successful login sets Flask session with `user_id` and `user_name`
- [ ] Successful login redirects to `/` (or dashboard)
- [ ] Logout clears session data
- [ ] Logout redirects to landing page or login page
- [ ] App starts without errors
