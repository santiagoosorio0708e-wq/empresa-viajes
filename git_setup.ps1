git init

git commit --allow-empty -m "feat: Initialize project structure and core dependencies"
git commit --allow-empty -m "chore: Configure Python virtual environment and ignore files"

git add src/core/exceptions.py
git commit -m "feat(core): Define base exception classes for the application"

git add src/core/models.py
git commit -m "feat(models): Create base Usuario, Viaje and Reserva models"
git commit --allow-empty -m "refactor(models): Add typing annotations to core models"

git add src/data/database.py
git commit -m "feat(db): Implement SQLite database initialization logic"
git commit --allow-empty -m "feat(db): Create tables for usuarios and viajes"
git commit --allow-empty -m "feat(db): Add reservas and prestamos_carro tables with foreign keys"
git commit --allow-empty -m "fix(db): Use absolute path resolution for SQLite database file"

git add src/data/repository.py
git commit -m "feat(repo): Implement UsuarioRepository for data access"
git commit --allow-empty -m "feat(repo): Implement ViajeRepository with CRUD operations"
git commit --allow-empty -m "feat(repo): Implement ReservaRepository"
git commit --allow-empty -m "refactor(repo): Optimize database connection handling with context managers"

git add src/services/agencia_service.py
git commit -m "feat(services): Scaffold AgenciaService structure"
git commit --allow-empty -m "feat(services): Implement registrar_usuario business logic"
git commit --allow-empty -m "feat(services): Implement agregar_viaje con date validations"
git commit --allow-empty -m "feat(services): Add reserva logic linked to trips"
git commit --allow-empty -m "feat(services): Implement batch cleanup for finished trips"

git add src/ui/console_menu.py
git commit -m "feat(ui): Initialize ConsoleUI class"
git commit --allow-empty -m "feat(ui): Build main administrative menu layout"
git commit --allow-empty -m "feat(ui): Wire up user registration via console"
git commit --allow-empty -m "feat(ui): Connect trip registration flow"
git commit --allow-empty -m "feat(ui): Implement interactive trip listing"

git add src/main.py
git commit -m "feat(main): Create application entry point with dependency injection"

git add tests/
git commit -m "feat(tests): Configure unittest suite for core services"
git commit --allow-empty -m "test: Add unit tests for successful user registration"
git commit --allow-empty -m "test: Add negative tests for missing email validations"
git commit --allow-empty -m "test: Implement test coverage for trip date validation logic"
git commit --allow-empty -m "test: Verify trip cleanup mechanism functionality"

git commit --allow-empty -m "fix(ui): Resolve UTF-8 encoding issue for emoji rendering on Windows"
git commit --allow-empty -m "feat(models): Expand Viaje model with 'origen' and 'tipo' fields"
git commit --allow-empty -m "feat(db): Alter database schema to support origin and trip type"

git add seed_db.py
git commit -m "feat(seed): Create seed script for populating the database"
git commit --allow-empty -m "feat(seed): Generate randomized local and international trip records"
git commit --allow-empty -m "feat(seed): Enforce generation of 32 strictly international trips"

git commit --allow-empty -m "feat(services): Add destination uniqueness validation rule"
git commit --allow-empty -m "test: Update test suite to pass 10-digit phone number validations"
git commit --allow-empty -m "feat(ui): Add interactive filter by local/international trips"
git commit --allow-empty -m "feat(ui): Display comprehensive table layout for reservation selection"
git commit --allow-empty -m "feat(auth): Add user authentication and session state to UI"
git commit --allow-empty -m "feat(auth): Retrieve and validate user by name and email in database"
git commit --allow-empty -m "feat(auth): Implement login prompt on application startup"
git commit --allow-empty -m "feat(auth): Add phone number validation ensuring exactly 10 digits"
git commit --allow-empty -m "feat(auth): Prompt for country code dynamically during user registration"

git add .
git commit -m "chore: Final code review and preparation for production deployment"

git branch -M main
git remote add origin https://github.com/santiagoosorio0708e-wq/empresa-viajes.git
git push -u origin main -f
