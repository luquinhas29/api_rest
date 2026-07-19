# AGENTS.md

## Cursor Cloud specific instructions

This repo is a single Spring Boot 3.2.4 REST API (`apirest`, Java 17) built with Maven (use the `./mvnw` wrapper). It manages `User` records linked to `Department`, exposing `GET /users`, `GET /users/{id}`, and `POST /users` on port `8080`.

### Database (required, must be started manually)
- The app connects to PostgreSQL at `jdbc:postgresql://localhost:5432/DB_API_REST`, user `postgres`, password `123` (see `src/main/resources/application.properties`). It will not start without it.
- PostgreSQL 16 is installed but does NOT auto-start in this environment. Start it each session with: `sudo pg_ctlcluster 16 main start`.
- One-time data setup (already applied, re-run only if the cluster is reset): `sudo -u postgres psql -c "ALTER USER postgres PASSWORD '123';"` and `sudo -u postgres psql -c 'CREATE DATABASE "DB_API_REST";'`.
- `ddl-auto=update` creates tables on boot. `import.sql` seed data is NOT loaded (Hibernate only runs it on create/create-drop), so the DB starts empty — create rows via `POST /users`.

### Build / test / run
- Test: `./mvnw test` (the single `contextLoads` test boots the full context and needs the DB running).
- Run (dev): `./mvnw spring-boot:run` — serves on `http://localhost:8080`.
- There is no separate lint step configured; there is no README or Dockerfile in the repo.
- `JAVA_HOME` is unset (a harmless warning); the wrapper still works with the system JDK.

### Quick smoke test
```
curl -X POST http://localhost:8080/users -H "Content-Type: application/json" -d '{"name":"Test","email":"test@example.com"}'
curl http://localhost:8080/users
```
