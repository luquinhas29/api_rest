# Roadmap de projetos — api_rest

Evolua **este repositório** em etapas. Cada etapa = branch + commits + README atualizado.

---

## Etapa 1 — Arquitetura limpa (semana 1–2)

**Por quê:** entrevistas júnior cobram camadas o tempo todo. Hoje o `UserController` fala direto com o `UserRepository`.

### Pacotes alvo

```
com.devlucaswilliams.apirest
├── controllers
├── services
├── repositories
├── entities
├── dto
├── exceptions
└── config          (depois)
```

### Tarefas

- [ ] Criar `UserService` e `DepartmentService`
- [ ] Controller só chama Service (sem Repository)
- [ ] Injeção por construtor (sem `@Autowired` no campo)
- [ ] `findById` com `orElseThrow` → 404
- [ ] Endpoints: `GET /users`, `GET /users/{id}`, `POST /users`, `PUT /users/{id}`, `DELETE /users/{id}`
- [ ] Mesmo CRUD para `Department`
- [ ] DTOs: `UserRequest`, `UserResponse` (não devolver Entity crua)

### Critério de pronto

Explicar em voz alta: *“A request entra no controller, a regra fica no service, o JPA fica no repository.”*

---

## Etapa 2 — Validação, erros e transação (semana 2–3)

- [ ] Dependência `spring-boot-starter-validation`
- [ ] `@Valid` no `@RequestBody` + anotações (`@NotBlank`, `@Email`)
- [ ] `@ControllerAdvice` com respostas JSON de erro
- [ ] `@Transactional` nos métodos de escrita do Service
- [ ] `@Transactional(readOnly = true)` nas leituras
- [ ] Caso de uso atômico: criar User + garantir Department (ou falhar tudo)

### Critério de pronto

Explicar ACID + o que o Spring faz no commit/rollback.

---

## Etapa 3 — Testes e qualidade (semana 3–4)

- [ ] Teste unitário do `UserService` (Mockito)
- [ ] Teste do Controller (`@WebMvcTest` ou MockMvc)
- [ ] `./mvnw test` passando
- [ ] Corrigir typo `inset` → `insert` / `create`

### Critério de pronto

Mostrar no terminal os testes verdes.

---

## Etapa 4 — Portfólio (semana 4–6)

- [ ] `docker-compose.yml` (Postgres)
- [ ] Flyway: scripts `V1__init.sql`
- [ ] Swagger/OpenAPI
- [ ] README com: o que é o projeto, como rodar, endpoints, decisões técnicas
- [ ] (Opcional) Spring Security + JWT

### Critério de pronto

Link do GitHub + README claro = peça de portfólio.

---

## Projeto paralelo (depois da Etapa 2)

**Nome sugerido:** `task-tracker-api` ou módulo `orders` neste repo.

Regras mínimas:
1. Entidade com status (`TODO` → `DOING` → `DONE`)
2. Transição de status validada no Service
3. Uma operação que altera 2 tabelas na mesma `@Transactional`
4. Listagem paginada

Isso treina o que entrevista ama: regra de negócio + consistência.

---

## Como usar este arquivo

1. Marque checkboxes conforme for terminando.
2. Um PR pequeno por etapa (ou por grupo de tarefas).
3. Depois de cada etapa, grave áudio de 3 min explicando o que fez (treino de entrevista).
