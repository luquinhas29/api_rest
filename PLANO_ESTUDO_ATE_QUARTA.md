# Plano de estudo — entrevista técnica Avanade

**Entrevista:** quarta-feira 26/08 às **13:00** com desenvolvedor  
**Vaga:** Desenvolvedor(a) Back-End Júnior — Avanade (R00348516)  
**Hoje:** sexta 21/08 · faltam **5 dias** (sex noite → qua manhã)

Foco: explicar o que você já faz bem (Java/Spring/MV) e ter discurso honesto nas lacunas (SQL Server, Redis, hexagonal, Azure).

Guia completo: [PR #3](https://github.com/luquinhas29/api_rest/pull/3) · Currículo: [PR #2](https://github.com/luquinhas29/api_rest/pull/2)

---

## Visão geral

| Dia | Data | Foco | Meta do dia |
|---|---|---|---|
| Sex | 21/08 | Spring + JPA + seu projeto | Contar 1 API ponta a ponta em voz alta |
| Sáb | 22/08 | SQL Server + Redis | Cache-aside + diferença vs Oracle |
| Dom | 23/08 | Hexagonal + microserviços | Desenhar hexagonal em 2 min |
| Seg | 24/08 | TDD + CI/CD + Azure glossário | 1 exemplo TDD + 3 serviços Azure |
| Ter | 25/08 | Simulado oral + STAR | Pitch 60s + 10 perguntas + 3 histórias |
| Qua | 26/08 manhã | Revisão leve | Só anotações — **zero assunto novo** |

**Carga sugerida:** 90–120 min/dia (sáb/dom pode alongar até 2h30). Qualidade > quantidade.

---

## Sexta 21/08 — Spring Boot + JPA + narrativa

### Por quê
O entrevistador vai testar se você entende o fluxo real do código — não se decorou cloud.

### Bloco (90–120 min)

| Tempo | O quê |
|---|---|
| 20 min | Abra `api_rest` (ou outro repo favorito). Trace: request → Controller → Repository → banco → JSON |
| 25 min | Revise e anote em 1 página: `@RestController`, `@GetMapping`/`@PostMapping`, `@PathVariable`, `@RequestBody`, status HTTP (200/201/400/404/500) |
| 25 min | JPA: `@Entity`, `@ManyToOne`, lazy vs eager, N+1, `@Transactional` (quando e por quê) |
| 20 min | **Em voz alta:** explique o projeto como se estivesse na entrevista |
| 10 min | Liste 3 decisões técnicas que você tomaria diferente hoje (ex.: service layer, Exception Handler, DTO) |

### Checklist — precisa saber falar
- [ ] Fluxo completo de um GET `/users/{id}`
- [ ] Diferença Repository vs Service
- [ ] Por que `findById().get()` é perigoso (Optional / 404)
- [ ] Lazy vs Eager com exemplo User → Department
- [ ] O que é N+1 e como evitar (`JOIN FETCH` / `@EntityGraph`)
- [ ] Para que serve `@Transactional`

### Frase-âncora
> “Na MV / nos meus projetos, a requisição entra no Controller, a regra fica no Service e a persistência no Repository. Uso JPA com relacionamentos e cuido de lazy loading e N+1 quando listo coleções.”

---

## Sábado 22/08 — SQL Server + Redis

### Por quê
A vaga cita SQL Server e Redis. Você vem de Oracle/PostgreSQL — mostre transferência de conhecimento + lab mental (ou Docker se der).

### Bloco (2h)

| Tempo | O quê |
|---|---|
| 30 min | SQL Server vs Oracle/PostgreSQL: tipos comuns, `IDENTITY`, schemas, driver JDBC no Spring (`com.microsoft.sqlserver`) |
| 20 min | Anote datasource Spring típico (URL, driver, `ddl-auto`) |
| 40 min | Redis: o que é, quando usar, **cache-aside**, TTL, invalidação no update |
| 20 min | (Opcional) Docker: subir Redis e anotar `@Cacheable` / `@CacheEvict` |
| 10 min | Ensaie a frase de lacuna (abaixo) em voz alta |

### Checklist
- [ ] “SQL Server é relacional como Oracle; mudam dialeto, tipos e driver — a modelagem JPA continua igual”
- [ ] Explicar cache-aside: lê cache → miss → banco → grava cache com TTL
- [ ] Invalidar cache no PUT/POST que altera o dado
- [ ] Quando **não** cachear (dado muito volátil / dado sensível sem cuidado)

### Frases prontas
- SQL Server: “Venho de Oracle/PostgreSQL; a lógica SQL é a mesma e já estudei o driver/datasource do SQL Server no Spring.”
- Redis: “Usaria cache-aside no GET com TTL e invalidação no update para reduzir carga no banco.”

### Mini-lab mental (sem código)
Produto `GET /products/{id}`:
1. Redis key `product:{id}`
2. Hit → retorna
3. Miss → SQL Server → grava no Redis 5–10 min → retorna
4. `PUT` → atualiza SQL Server → apaga key no Redis

---

## Domingo 23/08 — Hexagonal + microserviços

### Por quê
A vaga pede hexagonal e microserviços. Não precisa de lab perfeito — precisa **desenhar e explicar**.

### Bloco (2h)

| Tempo | O quê |
|---|---|
| 40 min | Hexagonal: domínio no centro, **ports** (contratos), **adapters** (HTTP, JPA, Redis) |
| 20 min | Desenhe no papel (2 min): Controller = adapter in · Service/Domain = centro · Repository = adapter out |
| 40 min | Monólito vs microserviço: quando cada um, trade-offs (deploy, rede, consistência, complexidade) |
| 20 min | Ensaio oral: “como eu refatoraria o `api_rest` para hexagonal mínimo” |

### Checklist
- [ ] Desenhar hexagonal em ≤ 2 minutos
- [ ] Repository vs Service (responsabilidades)
- [ ] Port = interface; Adapter = implementação
- [ ] 3 prós e 3 contras de microserviço vs monólito
- [ ] “Começo em monólito modular e extraio serviço quando o bounded context estiver claro”

### Frase pronta
> “Hexagonal coloca o domínio no centro, com ports como contratos e adapters para HTTP e banco — facilita testar a regra sem subir o Spring inteiro.”

### Desenho rápido (memorize)

```
        [ HTTP Controller ]  ← adapter in
                 │
            [ Port in ]
                 │
          [ Domínio / Use case ]
                 │
            [ Port out ]
           /            \
  [ JPA Adapter ]   [ Redis Adapter ]
```

---

## Segunda 24/08 — TDD + CI/CD + Azure/OpenShift

### Por quê
Fecha o pacote “como você trabalha”: testes, pipeline e cloud Microsoft (Avanade).

### Bloco (2h)

| Tempo | O quê |
|---|---|
| 40 min | TDD: Red → Green → Refactor. Escreva (ou narre) 1 teste de Service com JUnit + Mockito |
| 20 min | Unitário vs integração vs e2e — o que você testa em cada camada |
| 30 min | CI vs CD; GitHub Actions: checkout → JDK → `mvn test` → (opcional) build imagem |
| 30 min | Glossário Azure + OpenShift (abaixo) — **1 página de anotações** |

### Checklist TDD/CI
- [ ] Exemplo TDD: “primeiro falha o teste do cálculo/regra, depois implemento, depois limpo”
- [ ] Unitário = isolado com mock; integração = sobe contexto/banco
- [ ] CI = validar a cada push; CD = entregar com frequência de forma segura
- [ ] Citar Azure DevOps (você já usa na MV) + GitHub Actions (lab pessoal)

### Glossário (decore o essencial)

| Tema | Em 1 frase |
|---|---|
| Azure App Service / Container Apps | Hospeda API web / containers gerenciados |
| Azure SQL | SQL Server gerenciado na nuvem |
| Azure Cache for Redis | Redis gerenciado |
| Key Vault | Segredos (senhas, connection strings) |
| Application Insights | Monitoramento e telemetria |
| OpenShift | Kubernetes enterprise (Red Hat): Pod, Deployment, Service, Route |

### Frase pronta
> “Tenho Docker e Azure DevOps na prática; estudei App Service, Azure SQL, Redis e OpenShift como Kubernetes enterprise. Ainda não tenho deploy produtivo na Azure, mas sei o papel de cada serviço.”

---

## Terça 25/08 — Simulado + histórias STAR

### Por quê
Amanhã é a entrevista. Hoje é dia de **falar**, não de aprender.

### Bloco (2h–2h30)

| Tempo | O quê |
|---|---|
| 15 min | Ensaiar pitch de 60s (gravar no celular) |
| 50 min | Responder as **10 perguntas técnicas** em voz alta |
| 40 min | Montar e ensaiar **3 histórias STAR** |
| 15 min | 2 perguntas que você vai fazer ao entrevistador |
| 10 min | Checklist logístico (link, câmera, repo aberto) |

### Pitch 60s (use este)

> Sou desenvolvedor Java júnior na MV, atuando com Spring Boot, APIs REST, Oracle e Angular. Tenho projetos públicos com Security, JPA e testes. Estou aprofundando SQL Server, Redis, arquitetura hexagonal, microserviços e CI/CD — stack alinhada à vaga — e busco evoluir em um ambiente Microsoft/Azure como o da Avanade.

### 10 perguntas — responda em voz alta

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

### 3 histórias STAR (preencha com casos reais da MV)

| Tema | Situação → Tarefa → Ação → Resultado |
|---|---|
| Bug difícil | ________________ |
| Aprender sob prazo | ________________ |
| Colaboração / pedir ajuda | ________________ |

Dica: escolha bugs de produção, integração front/back/DB ou SQL lento — isso pesa mais que feature genérica.

### Perguntas para o entrevistador (escolha 1–2)
- “Quais são os principais desafios técnicos do time hoje?”
- “Como é o fluxo de code review e CI no projeto?”
- “No dia a dia do júnior, o quanto é API nova vs manutenção/bug?”

---

## Quarta 26/08 — manhã (só revisão)

### Até ~11h30
- [ ] Folhear **só** suas anotações (1–2 páginas)
- [ ] Repetir pitch 1–2 vezes
- [ ] Abrir o repo favorito no GitHub
- [ ] Testar câmera, microfone, link, fone, internet
- [ ] Água + ambiente silencioso

### Não faça
- Não abra tutorial novo
- Não tente “terminar” um lab
- Não revise 10 assuntos superficiais

### Na hora (13:00)
- Entre **10 min antes**
- Se travar: diga o que sabe → o que faria → como validaria
- Não invente experiência em Azure/OpenShift/Redis
- Feche com 1 pergunta boa

---

## Folha de cola (imprimir / tela ao lado no estudo)

### Stack da vaga × seu nível

| Tema | Seu nível | Na entrevista |
|---|---|---|
| Java / Spring Boot / REST | Forte (MV + GitHub) | Contar fluxo + decisões |
| JPA / Oracle / PostgreSQL | Forte | N+1, lazy, transação |
| Testes / Git / Docker / Azure DevOps | Bom | Exemplos concretos |
| SQL Server / Redis | Em estudo | Conceito + frase pronta |
| Hexagonal / microserviços | Em estudo | Desenho + trade-offs |
| Azure / OpenShift | Glossário | Honestidade + interesse |

### Se não souber
> “Não usei isso em produção ainda. O que eu sei é X. Na prática eu faria Y e validaria com Z.”

---

## Meta mínima de sucesso (se o tempo apertar)

Se só conseguir 60 min/dia, faça **nesta ordem**:

1. Narrativa do seu projeto Spring (sex)
2. Redis cache-aside + SQL Server em 10 frases (sáb)
3. Desenho hexagonal (dom)
4. Pitch + 5 perguntas técnicas (ter)
5. Quarta: revisão leve

Boa entrevista, Lucas. Você já tem base de júnior em produção — o diferencial agora é **falar com clareza**.
