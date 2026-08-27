# api_rest

API REST em **Spring Boot 3** + **JPA** + **PostgreSQL**.

Projeto de estudo de [Lucas Williams](https://github.com/luquinhas29) — parte da **Trilha A** (Java/Spring).

## Stack

- Java 17
- Spring Boot 3.2
- Spring Data JPA
- PostgreSQL

## Estado atual

CRUD inicial de `User` e `Department` (ManyToOne).  
Em evolução: Service/DTO, validação, testes, Docker — ver [PROJETOS.md](./PROJETOS.md).

## Plano de evolução (multi-trilha)

- [PLANO_DE_ESTUDOS.md](./PLANO_DE_ESTUDOS.md) — rotina + blocos (Java/Spring · PLSQL · panorama)
- [FUNDAMENTOS_SPRING.md](./FUNDAMENTOS_SPRING.md) — Bloco A
- [FUNDAMENTOS_PLSQL.md](./FUNDAMENTOS_PLSQL.md) — Bloco B
- [PANORAMA.md](./PANORAMA.md) — Docker / microsserviços / AWS
- [PROJETOS.md](./PROJETOS.md) — práticas e labs
- [CADERNO.md](./CADERNO.md) — registro do que está estudando

## Como rodar (local)

1. Suba um PostgreSQL e crie o banco `DB_API_REST`
2. Ajuste usuário/senha em `src/main/resources/application.properties`
3. Execute:

```bash
./mvnw spring-boot:run
```

### Endpoints atuais

| Método | Path | Descrição |
|--------|------|-----------|
| GET | `/users` | Lista usuários |
| GET | `/users/{id}` | Busca por id |
| POST | `/users` | Cria usuário |

## Próximo passo

Ativar o bloco no `CADERNO.md` e seguir a semana correspondente no plano.
