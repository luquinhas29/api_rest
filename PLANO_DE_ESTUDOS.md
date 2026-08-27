# Plano de estudos — Backend Java / Spring Boot

> Para: Lucas Williams  
> Contexto: entrevista recente como experiência; base atual = API REST Spring Boot + JPA + PostgreSQL  
> Objetivo: fixar fundamentos, fechar lacunas típicas de entrevista e ter projetos que mostrem evolução real

Entrevista que “não foi bem” quase sempre mostra **onde estudar**, não que você “não serve”.  
Use o que travou como checklist — anote o que não soube explicar e priorize isso na Fase 1.

---

## 0. Diagnóstico rápido (faça hoje, 20–30 min)

Escreva em um caderno ou arquivo `GAPS.md` (só para você):

| Pergunta | Consegui explicar / fazer? | Prioridade |
|----------|----------------------------|------------|
| **Spring × Spring Boot** | **não (entrevista)** | **P0 — já** |
| O que é DI / IoC / Bean | | **P0** |
| O que faz `@SpringBootApplication` | | **P0** |
| O que é uma API REST? | | |
| Controller × Service × Repository | | |
| O que é `@Transactional` e ACID? | | |
| Diferença entre `GET/POST/PUT/PATCH/DELETE` | | |
| O que é JPA / Hibernate / Entity? | | |
| `ManyToOne` / `OneToMany` e lazy vs eager | | |
| Como tratar erro 404 / validação | | |
| O que é DTO e por que usar | | |
| SQL básico (JOIN, WHERE, INDEX) | | |
| Collections, equals/hashCode, Streams | | |
| Git: branch, commit, PR | | |

Marque **vermelho** o que falhou na entrevista → isso entra primeiro.  
Respostas-modelo das básicas: [`ENTREVISTA_FUNDAMENTOS.md`](./ENTREVISTA_FUNDAMENTOS.md).

---

## 1. Rotina semanal (sustentável)

**Meta:** 8–12h/semana (melhor constante do que maratona).

| Dia | Foco | Tempo |
|-----|------|-------|
| Seg / Qua / Sex | Teoria + anotações curtas | 45–60 min |
| Ter / Qui | Código no projeto | 60–90 min |
| Sáb | Projeto + README + commit | 2–3 h |
| Dom | Revisão ativa + simular entrevista (falar em voz alta) | 45–60 min |

### Método de fixação (obrigatório)

Para cada tema:

1. **Explicar em voz alta** em 2 minutos (como se fosse entrevista).
2. **Escrever 3–5 linhas** com suas palavras.
3. **Aplicar no código** no mesmo dia ou no dia seguinte.
4. **Commit** com mensagem clara (`feat: add UserService with @Transactional`).

Se não consegue explicar sem olhar, ainda não fixou.

---

## 2. Mapa de fases

### Fase A — Fundamentos que sustentam entrevista (2–3 semanas)

**Java**
- OOP: encapsulamento, herança, polimorfismo, interfaces
- `equals` / `hashCode` / `toString`
- Collections (`List`, `Set`, `Map`) e quando usar cada uma
- Streams + `Optional` (evitar `.get()` cego)
- Exceções: checked vs unchecked

**SQL + banco**
- `SELECT`, `JOIN`, `GROUP BY`, índices básicos
- Chave primária / estrangeira
- O que é uma transação no banco (ACID)

**HTTP / REST**
- Status codes: 200, 201, 204, 400, 404, 409, 500
- Idempotência (GET vs POST vs PUT)
- Path params vs query params vs body

**Checklist de saída da Fase A**
- [ ] Explico OOP com exemplos do meu domínio (User/Department)
- [ ] Escrevo um JOIN User × Department sem colar
- [ ] Explico REST + status codes sem ler

---

### Fase B — Spring Boot “de verdade” (3–4 semanas)

Camadas (seu projeto hoje pula a Service — isso é lacuna clássica de entrevista):

```
Controller  →  recebe HTTP, devolve resposta
Service     →  regra de negócio + @Transactional
Repository  →  acesso a dados (JPA)
Entity      →  mapeia tabela
DTO         →  o que entra/sai da API (não expor Entity direto)
```

**Temas**
- Injeção de dependência (construtor > `@Autowired` no campo)
- CRUD completo: GET, POST, PUT, DELETE
- `@Transactional` e `readOnly = true` (você já começou — continue aplicando)
- Validação: `@Valid`, `@NotBlank`, `@Email`
- Exception handler global (`@ControllerAdvice`)
- Relacionamentos JPA + cuidado com lazy loading / N+1
- Paginação e ordenação (`Pageable`)
- Testes: `@SpringBootTest` vs `@WebMvcTest` vs teste de Service unitário

**Checklist de saída da Fase B**
- [ ] Explico por que Service existe
- [ ] Explico `@Transactional` com exemplo de 2 saves atômicos
- [ ] API devolve 404/400 corretos
- [ ] Tenho pelo menos 3 testes passando

---

### Fase C — Nível entrevista júnior+ / pleno inicial (3–4 semanas)

- Spring Security básico (JWT ou Basic) — autenticação vs autorização
- Migrations com Flyway ou Liquibase (parar de depender só de `ddl-auto=update`)
- Docker Compose (app + Postgres)
- Logs e tratamento de erros com mensagem clara
- Documentação OpenAPI/Swagger
- Cache simples / performance (conceito)
- Mensageria (conceito: fila, evento) — overview, não deep dive

**Checklist de saída da Fase C**
- [ ] Demo local sobe com `docker compose up`
- [ ] Endpoint protegido + um público
- [ ] README explica como rodar em 5 minutos
- [ ] Consigo defender decisões técnicas em entrevista

---

## 3. Projetos (evolução, não reinventar a roda)

Use **este repositório** como base. Um projeto bem documentado vale mais que cinco tutoriais incompletos.

### Projeto 1 — `api_rest` profissional (base atual)

**Objetivo:** transformar o CRUD básico em API de portfólio.

Entregas:
1. Camada `service` + DTOs de request/response
2. CRUD completo de `User` e `Department`
3. Validação + `@ControllerAdvice`
4. `@Transactional` nos use cases que alteram dados
5. Tratamento de `Optional` (sem `.get()` sem checagem)
6. Testes de Service e Controller
7. README: como subir Postgres + rodar a API
8. (Opcional) Docker Compose

**Critério de pronto:** alguém clona, segue o README e testa no Postman/Insomnia.

---

### Projeto 2 — Domínio com regra de negócio (novo módulo ou repo)

Sugestão: **gestão de tarefas / pedidos / biblioteca**

Regras obrigatórias (para forçar transação + domínio):
- Criar recurso com validação
- Mudança de status (ex.: `OPEN → IN_PROGRESS → DONE`)
- Operação que toca **duas tabelas** na mesma transação
- Histórico ou auditoria simples (`createdAt`, `updatedAt`)

Isso fixa o que entrevista cobra: regra de negócio + consistência.

---

### Projeto 3 — API “pronta para time”

Em cima do Projeto 1 ou 2:
- Auth JWT
- Flyway
- Swagger
- CI simples (GitHub Actions: `./mvnw test`)
- Paginação em listagens

**Critério de pronto:** você consegue gravar um vídeo de 5–8 min explicando a arquitetura.

---

## 4. Preparação de entrevista (paralelo a partir da semana 2)

### Banco de perguntas (pratique em voz alta)

**Java / OOP**
- Diferença entre `==` e `equals`
- `ArrayList` vs `LinkedList` vs `HashMap`
- O que é imutabilidade
- O que é `Optional` e quando usar

**Spring**
- Ciclo de uma request no Spring MVC
- Diferença entre `@Component`, `@Service`, `@Repository`
- O que o Spring Data JPA gera automaticamente
- O que acontece se uma RuntimeException cair dentro de `@Transactional`

**SQL / JPA**
- Lazy vs Eager — prós e contras
- O que é N+1 e como evitar (`join fetch` / `@EntityGraph`)
- Diferença entre `persist`, `merge`, `save` (visão prática)

**Comportamental**
- Conte a entrevista de ontem como aprendizado (honestidade + plano)
- “Me fala de um bug que você resolveu”
- “Como você estuda / evolui”

### Formato de simulação (domingo)
1. Pegue 5 perguntas
2. Responda em voz alta (cronômetro 2 min)
3. Anote o que travou
4. Estude só aquilo na segunda

---

## 5. Recursos (poucos e bons)

Não acumule curso. Escolha **um** por tema.

| Tema | Recurso sugerido |
|------|------------------|
| Java | Documentação oficial + exercícios (HackerRank / LeetCode Easy só Collections/Strings) |
| Spring Boot | Docs Spring + guias oficiais “Building a RESTful Web Service” |
| JPA | Baeldung (artigos pontuais: Transactional, LazyLoading, DTO) |
| SQL | Mode SQL Tutorial ou similar — prática diária 15 min |
| Entrevista | Anotar perguntas reais que te fizeram e montar flashcards |

Regra: **1 artigo → 1 commit no projeto** no mesmo dia.

---

## 6. Como medir progresso (a cada 2 semanas)

Responda com sim/não:

- [ ] Consigo explicar meu último commit em 3 minutos
- [ ] Minha API tem Service + DTO + erros tratados
- [ ] Tenho testes automatizados
- [ ] README permite outra pessoa rodar
- [ ] Fiz 1 simulação de entrevista
- [ ] Reduzi pelo menos 2 itens vermelhos do `GAPS.md`

Se 4+ forem “sim”, você está evoluindo de verdade — independente do resultado de ontem.

---

## 7. Próximos 7 dias (plano imediato)

| Dia | Ação concreta |
|-----|----------------|
| 1 | Preencher `GAPS.md` + treinar **Spring × Spring Boot** em voz alta (2x) — `ENTREVISTA_FUNDAMENTOS.md` |
| 2 | Flashcards 2–5 (DI, `@SpringBootApplication`, camadas, MVC vs Data) |
| 3 | Flashcards 6–10 + anotar outras perguntas da entrevista no `GAPS.md` |
| 4 | Estudar camadas + criar `UserService` e mover a lógica do controller |
| 5 | Trocar `.get()` por `orElseThrow` + PUT/DELETE |
| 6 | Revisar `@Transactional` e aplicar no Service |
| 7 | Simular 8 perguntas básicas em voz alta (cronômetro) + 1 commit no código |

---

## Mentalidade

Uma entrevista ruim é **dado**, não sentença.  
O que diferencia quem evolui: transformar vergonha em lista de estudo e **código commitado**.

Quando travar de novo, pergunte aqui com o tema exato (ex.: “lazy loading”, “JWT”, “teste do service”) — a gente aprofunda e aplica neste repo.
