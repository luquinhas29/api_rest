# Guia de Estudo — Desenvolvedor(a) Back-End Júnior | Avanade

**Vaga:** Desenvolvedor(a) BackEnd Junior — Software Engineering AV  
**Código:** R00348516  
**Local:** São Paulo, SP  
**Link oficial:** [avanade.com/pt-br/career/job-details/R00348516](https://www.avanade.com/pt-br/career/job-details/R00348516)

Este guia foi montado a partir dos requisitos publicados da vaga e do perfil atual (Java, Spring Boot, APIs REST, Oracle/PostgreSQL, Git, Azure DevOps, Docker, testes). O foco é fechar lacunas e chegar na entrevista com evidências práticas no GitHub.

---

## 1. O que a vaga pede

### Responsabilidades

| Responsabilidade | O que isso significa na prática |
|---|---|
| Construir e automatizar funcionalidades de negócio | Entender regra de negócio, implementar em Java/Spring e entregar com qualidade |
| Implementar APIs e microserviços, integrando sistemas externos | REST bem desenhada, comunicação entre serviços, cliente HTTP, contratos |
| Soluções escaláveis em nuvem | Pensar em cache, banco, containers e serviços Azure |
| DevOps moderno: CI/CD e testes automatizados | Pipeline que builda, testa e publica; cobertura mínima de testes |

### Stack e competências exigidas

| Prioridade | Competência | Seu status aproximado |
|---|---|---|
| Crítica | Java + Spring Boot | Forte — base sólida |
| Crítica | Design de APIs REST | Forte |
| Crítica | Padrões Repository / Service | Forte |
| Crítica | Testes unitários + TDD | Médio — aprofundar TDD |
| Alta | SQL Server | Lacuna — migrar mentalidade Oracle → SQL Server |
| Alta | Redis (cache) | Lacuna |
| Alta | Arquitetura hexagonal | Lacuna conceitual + prática |
| Alta | Microserviços | Lacuna / nível introdutório |
| Alta | CI/CD + DevOps | Médio — Azure DevOps existe; formalizar pipeline |
| Média | Azure Cloud | Lacuna / introdutório |
| Média | OpenShift | Lacuna |
| Média | GitHub avançado (PRs, Actions, colaboração) | Médio |
| Média | Análise de performance de código | Lacuna |

---

## 2. Mapa mental: como estudar (ordem sugerida)

```
1. Consolidar Java/Spring (nível entrevista)
        ↓
2. SQL Server + Redis (dados e cache)
        ↓
3. Hexagonal + microserviços (arquitetura)
        ↓
4. Testes / TDD + performance
        ↓
5. Azure + OpenShift + CI/CD (entrega)
        ↓
6. Projeto capstone no GitHub + simulado de entrevista
```

Estude **em camadas**: conceito → exercício curto → projeto no GitHub → narrativa para entrevista.

---

## 3. Trilha por tópico

### 3.1 Java e Spring Boot (base da entrevista)

**Objetivo:** explicar e implementar com segurança o que a Avanade usa no dia a dia.

**Estudar**
- OOP, Collections, Streams, Optional, Exceptions
- Spring Boot: starters, `application.yml`, profiles
- Spring Web: Controllers, DTOs, `@Valid`, Exception Handler
- Spring Data JPA: entities, relationships, queries, transactions
- Injeção de dependência, escopos, beans
- Spring Security básico (JWT / OAuth — você já tem projetos)

**Prática mínima**
- Revisar um CRUD completo com validação, tratamento de erro e paginação
- Explicar em voz alta o fluxo: request → controller → service → repository → DB

**Checklist de entrevista**
- [ ] Diferença entre `@Component`, `@Service`, `@Repository`
- [ ] `@Transactional`: quando usar e o que acontece sem ele
- [ ] Lazy vs Eager e problema N+1
- [ ] Diferença entre checked/unchecked exceptions no Spring
- [ ] Como versionar API (`/api/v1`)

**Recursos**
- Documentação Spring Boot 3.x
- Baeldung (artigos pontuais)
- Seus repos: `webService`, `validacao_e_seguranca`, `dscommerce_jacoco`

---

### 3.2 Design de APIs

**Objetivo:** desenhar contratos claros, idempotentes e prontos para integração.

**Estudar**
- Verbos HTTP e códigos de status (200, 201, 204, 400, 401, 404, 409, 422, 500)
- Idempotência (PUT/DELETE vs POST)
- Paginação, filtros, ordenação
- Versionamento e documentação (OpenAPI / Swagger)
- Integração com sistemas externos: `WebClient` / `RestClient`, timeouts, retries

**Prática**
- Documentar uma API com SpringDoc OpenAPI
- Consumir uma API pública e mapear erros de integração

**Checklist**
- [ ] Quando usar 201 vs 200
- [ ] Como retornar erro padronizado (Problem Details / payload próprio)
- [ ] Diferença entre sync e async na integração

---

### 3.3 SQL Server

**Objetivo:** sair de “só Oracle/PostgreSQL” e demonstrar conforto com SQL Server.

**Estudar**
- Tipos comuns (`INT`, `BIGINT`, `NVARCHAR`, `DATETIME2`, `UNIQUEIDENTIFIER`)
- `JOIN`, subqueries, CTE (`WITH`)
- Índices, chaves primárias/estrangeiras
- Stored procedures básicas (comparar com PL/SQL)
- Transações e isolamento (visão prática)
- Connection string JDBC + driver `mssql-jdbc` no Spring Boot

**Prática**
1. Subir SQL Server em Docker
2. Conectar o projeto Spring Boot
3. Migrar um CRUD que hoje usa PostgreSQL/Oracle para SQL Server
4. Escrever 5 queries com JOIN + agregação + índice

**Comando útil (Docker)**

```bash
docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=Your_strong_Passw0rd" \
  -p 1433:1433 --name sqlserver \
  -d mcr.microsoft.com/mssql/server:2022-latest
```

**Checklist**
- [ ] Diferenças práticas Oracle/PostgreSQL vs SQL Server
- [ ] Como configurar datasource no Spring
- [ ] Explicar índice e quando ele ajuda/atrapalha

---

### 3.4 Redis

**Objetivo:** usar cache para performance e reduzir carga no banco.

**Estudar**
- Estruturas: String, Hash, List, Set
- TTL / expiração
- Cache-aside (padrão mais comum em apps Spring)
- `spring-boot-starter-data-redis` + `@Cacheable` / `@CacheEvict`
- Quando **não** cachear (dados muito voláteis, dados sensíveis sem cuidado)

**Prática**
1. Subir Redis no Docker
2. Cachear um endpoint de leitura (`GET /products/{id}`)
3. Invalidar cache no update/delete
4. Medir tempo com e sem cache (mesmo que simples com logs)

```bash
docker run --name redis -p 6379:6379 -d redis:7
```

**Checklist**
- [ ] Explicar cache-aside em 1 minuto
- [ ] O que é TTL e por que importa
- [ ] Risco de cache inconsistente após update

---

### 3.5 Arquitetura hexagonal

**Objetivo:** mostrar que você entende desacoplamento — ponto forte da vaga.

**Estudar**
- Domínio no centro; adapters de entrada (HTTP) e saída (DB, APIs)
- Portas (interfaces) vs adapters (implementações)
- Diferença em relação a “camadas clássicas” (Controller → Service → Repository)
- Benefício: testar domínio sem Spring/banco

**Estrutura alvo (exemplo)**

```
application/
  domain/          # entidades e regras
  ports/in/        # use cases (interfaces)
  ports/out/       # repositórios, clientes externos
  adapters/
    in/web/        # controllers
    out/persistence/
    out/redis/
```

**Prática**
- Refatorar um projeto seu (ex.: `webService` ou `api_rest`) para hexagonal **mínimo**:
  - 1 use case
  - 1 porta de saída
  - 1 adapter JPA
  - 1 adapter REST
  - testes do domínio sem subir Spring

**Checklist**
- [ ] Desenhar hexagonal no quadro em 2 minutos
- [ ] Diferença hexagonal vs MVC em camadas
- [ ] Onde ficam DTOs vs entidades de domínio

---

### 3.6 Microserviços

**Objetivo:** vocabulário e prática mínima — não precisa ser arquiteto.

**Estudar**
- Monólito vs microserviços (trade-offs)
- Comunicação síncrona (HTTP) vs assíncrona (fila — visão geral)
- API Gateway (conceito)
- Idempotência, timeouts, circuit breaker (ideia)
- Observabilidade: logs, correlation id
- Consistência eventual (ideia)

**Prática sugerida (capstone leve)**
- Serviço A: Cadastro de pedidos
- Serviço B: Catálogo/produtos
- A chama B via HTTP
- Redis no serviço de leitura
- SQL Server no serviço de escrita
- Docker Compose subindo tudo

**Checklist**
- [ ] Quando microserviço ajuda e quando atrapalha
- [ ] O que é acoplamento temporal (chamada síncrona)
- [ ] Como versionar contratos entre serviços

---

### 3.7 Padrões Repository e Service

**Objetivo:** reforçar o que a vaga cita explicitamente.

**Estudar / revisar**
- Repository: acesso a dados, sem regra de negócio pesada
- Service: orquestra casos de uso e regras
- Mapper/DTO: não vazar entidade JPA na API
- Facade (opcional) para orquestrações maiores

**Prática**
- Em um PR de estudo, separar claramente responsabilidades e escrever README explicando as camadas

---

### 3.8 Testes unitários, TDD e performance

**Objetivo:** TDD de verdade + olhar de performance — diferencial júnior.

**Testes / TDD**
- Ciclo Red → Green → Refactor
- JUnit 5 + Mockito
- `@WebMvcTest` vs `@DataJpaTest` vs `@SpringBootTest`
- Testar service puro (domínio) sem subir contexto Spring
- Cobertura com JaCoCo (você já usou)

**Performance (nível júnior aplicável)**
- Evitar N+1 (`join fetch` / entity graphs)
- Índices no banco
- Cache com Redis
- Não fazer lógica pesada no controller
- Logs/métricas simples de tempo de endpoint
- Profiling básico (VisualVM ou Actuator + métricas)

**Prática TDD (exercício diário de 45–60 min)**
1. Escolher uma regra (ex.: “pedido não pode ter item com quantidade <= 0”)
2. Escrever teste falhando
3. Implementar o mínimo
4. Refatorar

**Checklist**
- [ ] Explicar TDD sem enrolação
- [ ] Diferença teste unitário vs integração
- [ ] Dar 3 exemplos de gargalo comum em API Spring

---

### 3.9 CI/CD e DevOps

**Objetivo:** demonstrar entrega contínua — a vaga enfatiza isso.

**Estudar**
- Conceito de pipeline: build → test → package → deploy
- GitHub Actions (prioritário: a vaga cita GitHub)
- Azure DevOps Pipelines (você já teve contato)
- Artefatos (JAR), variáveis de ambiente, secrets
- Qualidade no pipeline: testes obrigatórios para merge

**Prática**
- No repositório capstone, criar `.github/workflows/ci.yml` que:
  1. Roda em push/PR
  2. `./mvnw test`
  3. `./mvnw package`
  4. (Opcional) build de imagem Docker

**Checklist**
- [ ] Explicar CI vs CD
- [ ] O que nunca deve ir commitado (secrets)
- [ ] Por que teste no pipeline importa mais que “rodar na minha máquina”

---

### 3.10 Azure Cloud e OpenShift

**Objetivo:** conversar com segurança no nível júnior — não precisa ser expert.

**Azure (fundamentos)**
- App Service / Container Apps (onde a API sobe)
- Azure SQL (equivalente gerenciado ao SQL Server)
- Azure Cache for Redis
- Key Vault (segredos)
- Application Insights (monitoramento — visão geral)
- Relação Avanade ↔ Microsoft (parceira estratégica): Azure é linguagem da empresa

**OpenShift (fundamentos)**
- É Kubernetes enterprise (Red Hat)
- Conceitos: Pod, Deployment, Service, Route
- Build/Deploy de imagem de container
- Diferença prática Docker local vs cluster

**Prática mínima**
1. Containerizar a API (`Dockerfile`)
2. `docker compose` com app + SQL Server + Redis
3. Ler 1 tutorial oficial de deploy Spring Boot no Azure Container Apps **ou** App Service
4. Ler overview do OpenShift (docs Red Hat) e anotar o glossário

**Checklist**
- [ ] O que é um container e por que facilita deploy
- [ ] Relação Docker → imagem → pod no OpenShift
- [ ] Citar 3 serviços Azure relevantes para backend

---

### 3.11 GitHub avançado (colaboração)

**Estudar / praticar**
- Branching (`main` + feature branches)
- Pull Request com descrição clara
- Code review: comentar e responder
- Conventional commits (opcional, mas ajuda)
- GitHub Actions
- Issues e Projects (organização)

**Prática**
- Tratar seu projeto de estudo como se fosse time: PRs pequenos, README forte, issues com tasks

---

## 4. Plano de estudo sugerido (6 semanas)

Ajuste o ritmo conforme sua rotina na MV. Prefira **consistência** (1–2h/dia) a maratonas.

### Semana 1 — Base + SQL Server
- Revisar Spring Boot (controllers, services, JPA, exceptions)
- SQL Server no Docker + CRUD migrado
- Anotar diferenças Oracle × SQL Server
- **Entrega:** repo `demo-sqlserver-spring` com README

### Semana 2 — Redis + performance básica
- Cache-aside em 2 endpoints
- Medir antes/depois
- Revisar N+1 e índices
- **Entrega:** mesmo repo com Redis + seção de performance no README

### Semana 3 — Hexagonal
- Refatorar para ports/adapters
- Testes de domínio sem Spring
- Desenhar diagrama no README
- **Entrega:** estrutura hexagonal documentada

### Semana 4 — Microserviços leves + APIs
- 2 serviços + comunicação HTTP
- OpenAPI nos dois
- Tratamento de timeout/erro de integração
- **Entrega:** `docker compose up` funcional

### Semana 5 — TDD + CI/CD
- Cobrir regras de negócio com TDD
- GitHub Actions (test + package)
- Revisar JaCoCo
- **Entrega:** badge de CI no README

### Semana 6 — Azure/OpenShift + entrevista
- Dockerfile polido + glossário Azure/OpenShift
- Simulado de entrevista (perguntas abaixo)
- Atualizar LinkedIn/GitHub destacando o projeto capstone
- Revisar currículo alinhado à vaga

---

## 5. Projeto capstone (o que colocar no GitHub)

Nome sugerido: `avanade-backend-lab` ou `order-hexagonal-lab`

**Escopo mínimo viável**
- Domínio: pedidos + produtos
- Hexagonal
- SQL Server
- Redis no GET de produto
- Testes (unitários + alguns de integração)
- OpenAPI
- Docker Compose
- GitHub Actions
- README com:
  - arquitetura (diagrama)
  - como subir
  - decisões técnicas
  - o que você aprenderia a melhorar

Isso vira sua prova social na entrevista: “implementei exatamente o stack da vaga”.

---

## 6. Preparação para entrevista

### Perguntas técnicas prováveis

1. Explique o fluxo de uma requisição no Spring Boot.
2. O que é arquitetura hexagonal e por que usar?
3. Diferença entre monólito e microserviço.
4. Como você usaria Redis numa API de produtos?
5. Como evitar N+1 no JPA?
6. O que é TDD? Mostre um exemplo.
7. Como montaria um pipeline CI para um serviço Java?
8. O que você sabe de Azure? E de OpenShift?
9. Repository vs Service — responsabilidades.
10. Como trataria falha ao chamar um serviço externo?

### Perguntas comportamentais (STAR)

- Conte um bug difícil que você investigou na MV.
- Como você aprende uma tecnologia nova sob prazo?
- Situação em que pediu ajuda / colaborou com o time.
- Como você prioriza correção vs feature.

**Método STAR:** Situação → Tarefa → Ação → Resultado.

### Pitch de 60 segundos (adapte)

> Sou desenvolvedor Java júnior na MV, atuando com Spring Boot, APIs REST, Oracle e Angular. Tenho projetos públicos com Security, JPA e testes. Estou aprofundando SQL Server, Redis, arquitetura hexagonal, microserviços e CI/CD com GitHub Actions — stack alinhada à vaga — e busco evoluir em um ambiente Microsoft/Azure como o da Avanade.

---

## 7. Como falar das suas lacunas sem se prejudicar

| Lacuna | Como posicionar |
|---|---|
| SQL Server | “Venho de Oracle/PostgreSQL; já pratiquei SQL Server em lab com Spring + Docker.” |
| Redis | “Implementei cache-aside com TTL e invalidação no update.” |
| Hexagonal | “Refatorei um CRUD para ports/adapters e testei o domínio isolado.” |
| Azure/OpenShift | “Tenho base em Docker/Azure DevOps; estudei os serviços Azure e o modelo OpenShift/K8s.” |
| Microserviços | “Montei lab com 2 serviços, contrato HTTP e compose.” |

Nunca diga só “não sei”. Digite o **plano + evidência**.

---

## 8. Rotina diária sugerida (90 minutos)

| Bloco | Tempo | Atividade |
|---|---|---|
| Teoria focada | 25 min | 1 tópico da trilha (doc/artigo/vídeo) |
| Hands-on | 45 min | Código no lab |
| Revisão ativa | 15 min | Anotar 5 bullets + 1 pergunta de entrevista |
| Commit | 5 min | Push com mensagem clara |

Nos fins de semana: consolidar README, diagramas e simulado oral (gravar áudio de 5–10 min).

---

## 9. Materiais recomendados (enxutos)

**Java / Spring**
- Docs oficiais Spring Boot / Spring Data / Spring Web
- Baeldung (consulta pontual)

**Arquitetura**
- Artigos sobre Hexagonal / Ports & Adapters (Alistair Cockburn — conceito)
- “Microservices Patterns” (conceito; não precisa ler o livro inteiro agora)

**Dados**
- Docs Microsoft SQL Server + Redis
- Spring Data Redis reference

**Cloud / DevOps**
- Microsoft Learn: caminhos introdutórios Azure para desenvolvedores
- GitHub Actions docs (workflow Java/Maven)
- Red Hat OpenShift: “Interactive Learning Portal” / overview

**Testes**
- JUnit 5 user guide
- Mockito + exemplos TDD curtos

---

## 10. Checklist final antes de candidatar / entrevista

- [ ] Currículo cita Java, Spring Boot, APIs, testes, Git, Docker, Azure DevOps
- [ ] Projetos no GitHub com README profissional
- [ ] Lab com SQL Server + Redis + hexagonal (mesmo simples)
- [ ] Pipeline CI verde
- [ ] Pitch de 60s ensaiado
- [ ] 10 respostas técnicas ensaiadas em voz alta
- [ ] 3 histórias STAR prontas (bug, aprendizado, colaboração)
- [ ] LinkedIn atualizado e coerente com o currículo

---

## 11. Prioridade se o tempo for curto (versão 2 semanas)

Se a entrevista estiver perto, foque nesta ordem:

1. **SQL Server + Redis** no projeto Spring (prova prática da stack)
2. **Hexagonal mínimo** + testes de domínio
3. **GitHub Actions** rodando testes
4. **Glossário Azure/OpenShift** (1 página de anotações)
5. **Simulado de entrevista** diário

Deixe microserviços “completos” em segundo plano se o tempo apertar; tenha pelo menos o discurso correto + 1 demo simples.

---

## 12. Benefícios citados pela Avanade (contexto)

Útil para a conversa com RH (não é foco técnico, mas mostra interesse):
- VR/VA, multibenefícios, médico/odontológico
- Certificações e treinamentos
- Wellhub, mentoria de carreira, Birthday Off
- Participação nos resultados, previdência, Avababy etc.

---

*Guia alinhado à vaga R00348516 (BackEnd Junior — Avanade / São Paulo) e ao perfil Java/Spring atual. Atualize este documento conforme o lab evoluir e marque os checklists.*
