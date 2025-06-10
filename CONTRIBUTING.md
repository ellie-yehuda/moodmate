# Contributing to MoodMate

Thank you for considering contributing to MoodMate! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please be respectful, inclusive, and considerate in all interactions.

## Getting Started

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/your-username/moodmate-app.git
   cd moodmate-app
   ```
3. **Set up your development environment**
   - Follow the installation instructions in the README.md

## Development Process

### Branching Strategy

- `main` branch is the stable, production-ready code
- Create feature branches from `main` using the format:
  - `feature/feature-name` for new features
  - `bugfix/bug-description` for bug fixes
  - `docs/description` for documentation changes

### Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

Types include:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `style`: Changes that don't affect code functionality (formatting, etc.)
- `refactor`: Code changes that neither fix bugs nor add features
- `test`: Adding or correcting tests
- `chore`: Changes to build process or auxiliary tools

### Pull Request Process

1. Update the README.md with details of changes if applicable
2. Ensure all tests pass and add new tests for new functionality
3. Update documentation as needed
4. Submit your pull request with a clear title and description
5. Link any related issues using GitHub keywords (fixes, resolves, etc.)

## Frontend Development Guidelines

- Follow React best practices and hooks patterns
- Use functional components with hooks instead of class components
- Maintain responsive design for all UI components
- Follow the established project structure
- Document complex components with JSDoc comments

## Backend Development Guidelines

- Follow PEP 8 style guide for Python code
- Document all functions, classes, and modules with docstrings
- Write unit tests for new functionality
- Keep API endpoints RESTful and consistent

## Testing

- Write tests for new features or bug fixes
- Make sure all existing tests pass before submitting a pull request
- Frontend tests use Vitest
- Backend tests use pytest

## Documentation

- Keep documentation up-to-date with code changes
- Use clear, concise language
- Include examples where appropriate

## Questions?

If you have any questions or need help, please open an issue with the "question" label or reach out to the maintainers.

Thank you for contributing to MoodMate! 