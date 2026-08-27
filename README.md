# api_rest

API REST em **Spring Boot 3** + **JPA** + **PostgreSQL**.

Projeto de estudo e portfólio de [Lucas Williams](https://github.com/luquinhas29).

## Stack

- Java 17
- Spring Boot 3.2
- Spring Data JPA
- PostgreSQL

## Estado atual

CRUD inicial de `User` e entidade `Department` (ManyToOne).  
Em evolução: camadas Service/DTO, validação, testes e Docker — ver [PROJETOS.md](./PROJETOS.md).

## Plano de evolução

- [PLANO_DE_ESTUDOS.md](./PLANO_DE_ESTUDOS.md) — rotina, fases e preparação de entrevista
- [ENTREVISTA_FUNDAMENTOS.md](./ENTREVISTA_FUNDAMENTOS.md) — flashcards (Spring × Boot, DI, camadas…)
- [PROJETOS.md](./PROJETOS.md) — etapas concretas neste repositório
- [GAPS.md](./GAPS.md) — lacunas da última entrevista (preencher)

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

Seguir a **Etapa 1** em [PROJETOS.md](./PROJETOS.md): extrair `UserService` e completar o CRUD.
