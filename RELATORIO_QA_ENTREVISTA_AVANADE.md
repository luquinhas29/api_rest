# Relatório Q&A — Entrevista Técnica Avanade

**Vaga:** Desenvolvedor(a) Back-End Júnior (R00348516)  
**Candidato:** Lucas Williams César Pires  
**Quando:** quarta 26/08 às 13:00 (com desenvolvedor)

PDF: [`RELATORIO_QA_ENTREVISTA_AVANADE.pdf`](./RELATORIO_QA_ENTREVISTA_AVANADE.pdf)

> Estude em voz alta. As respostas são modelos — adapte com exemplos reais da MV e do GitHub.

---

## Pitch (60s)

> Sou desenvolvedor Java júnior na MV, atuando com Spring Boot, APIs REST, Oracle e Angular. No dia a dia investigo bugs em produção, integro front, back e banco, e trabalho com Git, Jira, Azure DevOps e Docker. Tenho projetos públicos no GitHub com JPA, Security, validação e testes. Estou aprofundando SQL Server, Redis, arquitetura hexagonal, microserviços e CI/CD — stack alinhada à vaga — e busco evoluir em um ambiente Microsoft/Azure como o da Avanade.

---

## Java / Spring / REST

### P1. Fluxo de uma requisição no Spring Boot
DispatcherServlet → Controller → Service → Repository (JPA) → banco → JSON (Jackson) + status HTTP.

### P2. @Controller vs @RestController
`@RestController` = `@Controller` + `@ResponseBody` (API JSON).

### P3. Status HTTP
200, 201, 204, 400, 401, 403, 404, 409, 500 — use com semântica correta.

### P4. DTO
Objeto de transporte; não expor entidade JPA direto (lazy, segurança, contrato).

### P5. Exceções
`@ControllerAdvice` + `@ExceptionHandler` → 404/400/500 sem vazar stack.

### P6. Injeção de dependência
Spring injeta beans; preferir construtor a `@Autowired` em campo.

### P7. PUT vs PATCH
PUT completo; PATCH parcial.

### P8. Security / JWT
Token no Authorization; filtro valida; roles no contexto. Citar projetos com Security.

---

## JPA / Banco

### P9–P10. JPA/Hibernate e anotações
ORM: `@Entity`, `@Id`, `@ManyToOne` (User → Department no `api_rest`).

### P11. Lazy vs Eager
LAZY sob demanda; EAGER junto. Cuidado com `LazyInitializationException` e over-fetch.

### P12. N+1
1 + N queries; evitar com `JOIN FETCH` / `@EntityGraph` / DTO.

### P13. @Transactional
Limite de commit/rollback no Service.

### P14. findById().get()
Perigoso → `orElseThrow` + 404.

### P15–P16. JPQL vs SQL; ddl-auto
JPQL em entidades; em prod preferir migrations (Flyway) a `update`.

---

## Arquitetura

### P17. Repository vs Service
Dados vs regra de negócio; Controller só HTTP.

### P18. Hexagonal
Domínio no centro; ports = contratos; adapters = HTTP/JPA/Redis.

### P19. Monólito vs microserviço
Simplicidade vs escala/complexidade; começar modular.

### P20. API REST de verdade
Recursos, verbos, status, DTO, erros consistentes, OpenAPI.

### P21. Falha em serviço externo
Timeout, log, retry cuidadoso, fallback; circuit breaker (avançado).

---

## SQL Server / Redis / Performance

### P22. SQL Server
Base Oracle/PostgreSQL; mesma lógica; muda dialeto/driver.

### P23. Redis (cache-aside)
GET: cache → miss → banco → grava TTL; UPDATE invalida key.

### P24. Quando não cachear
Dado volátil/sensível; invalidação cara.

### P25–P26. Performance e índice
Medir → SQL/N+1 → índice → cache → paginação.

---

## Testes / CI/CD

### P27. TDD
Red → Green → Refactor.

### P28. Unitário vs integração
Mock isolado vs contexto/banco.

### P29–P30. O que testar / mock
Regra do Service; mock do Repository.

### P31–P34. CI/CD, Git, Docker
CI = build+test no push; CD = entrega. Azure DevOps (MV) + GitHub Actions (lab).

---

## Azure / OpenShift

### P35–P36
Honestidade: Azure DevOps na prática; glossário App Service, Azure SQL, Redis, Key Vault, Insights; OpenShift = K8s enterprise.

---

## MV / Motivação

### P37–P41
Dia a dia MV; explicar `api_rest`; por que Avanade; fraqueza com plano; visão em 2 anos.

---

## STAR (comportamental)

- Bug difícil  
- Aprender sob prazo  
- Pedir ajuda / colaboração  
- Priorizar bug vs feature  
- Feedback / conflito  

Preencha com casos **reais** antes da entrevista.

---

## Lacunas (frases prontas)

| Tema | Frase |
|---|---|
| SQL Server | Venho de Oracle/PostgreSQL; estudei driver/datasource SQL Server no Spring. |
| Redis | Cache-aside + TTL + invalidação no update. |
| Hexagonal | Domínio no centro, ports e adapters; facilita teste. |
| Azure/OpenShift | Docker + Azure DevOps; estudei os serviços — sem inventar deploy. |

---

## Pergunte ao entrevistador

1. Principais desafios técnicos do time?  
2. Como é code review / CI?  
3. Rotina do júnior: feature vs manutenção?

---

## Dia da entrevista

- 10 min antes; câmera/link ok  
- Repo aberto; anotações de 1 página  
- Sem assunto novo na manhã  
- Se travar: sei → faria → validaria  
- Feche com 1 pergunta boa  

Boa entrevista, Lucas.
