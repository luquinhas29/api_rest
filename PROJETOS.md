# Roadmap de prática — projetos e labs

Trilhas alinhadas aos blocos do `PLANO_DE_ESTUDOS.md`.  
Evolua com commit + nota no `CADERNO.md`.

---

## Trilha A — `api_rest` (Java / Spring)

### Etapa 1 — Arquitetura limpa

Hoje o `UserController` fala direto com o `UserRepository`.

```
controllers · services · repositories · entities · dto · exceptions
```

- [ ] `UserService` / `DepartmentService`
- [ ] Controller só chama Service
- [ ] Injeção por construtor
- [ ] `orElseThrow` → 404
- [ ] CRUD completo User e Department
- [ ] DTOs request/response

### Etapa 2 — Validação, erros, transação

- [ ] `spring-boot-starter-validation` + `@Valid`
- [ ] `@ControllerAdvice`
- [ ] `@Transactional` (escrita) e `readOnly` (leitura)
- [ ] Caso de uso atômico em 2 tabelas

### Etapa 3 — Testes

- [ ] Teste do Service
- [ ] Teste do Controller
- [ ] `./mvnw test` ok
- [ ] Renomear `inset` → nome claro

### Etapa 4 — Empacotar / operar

- [ ] `docker-compose.yml` (encaixa no Bloco D Docker)
- [ ] Flyway
- [ ] OpenAPI/Swagger
- [ ] README completo

### Projeto paralelo (quando quiser)

Domínio com status (`TODO` → `DOING` → `DONE`) + regra no Service + paginação.

---

## Trilha B — Angular

App de estudo separado **ou** exercício mínimo (sem código do trabalho).

- [ ] 1 component de listagem
- [ ] 1 service com `HttpClient` (mock ou `api_rest`)
- [ ] 2 rotas navegáveis
- [ ] 1 formulário com validação
- [ ] README: como subir o front e apontar pra API
- [ ] (Depois) consumir CRUD completo da `api_rest`

---

## Trilha C — SQL / PLSQL

Pasta sugerida: `estudo-plsql/` (só scripts de estudo).

- [ ] `01_selects.sql` — filtros e ordenação
- [ ] `02_joins.sql` — INNER/LEFT comentados
- [ ] `03_aggregates.sql` — GROUP BY / HAVING
- [ ] `04_anon_block.sql` — bloco anônimo + exception
- [ ] `05_procedure.sql` — procedure insert/update
- [ ] `06_function.sql` — function usada em SELECT
- [ ] `07_package.sql` — spec + body mínimos
- [ ] `README.md` na pasta: como rodar no seu ambiente

Sem dado real de produção/cliente.

---

## Trilha D — Labs de panorama

Siga `PANORAMA.md` na semana do tema:

- [ ] Docker: Compose com Postgres (e depois a API)
- [ ] Microsserviços: diagrama + nota de trade-offs
- [ ] AWS: mapa + lab leve (S3 ou desenho app+RDS)

---

## Como usar

1. Ative o bloco no `CADERNO.md`
2. Marque tarefas da trilha correspondente
3. Prefira PRs/commits pequenos e frequentes
