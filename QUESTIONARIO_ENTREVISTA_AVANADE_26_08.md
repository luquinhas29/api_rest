# Questionário — Entrevista Técnica Avanade (26/08 às 13h)

**Vaga:** Desenvolvedor(a) BackEnd Junior — R00348516  
**Como usar:** leia pergunta → tente responder em voz alta → compare com a resposta.  
**Meta até quarta:** dominar as seções 1 a 8; seções 9 e 10 são bônus.

---

## 1. Java (fundamentos)

### P1. Qual a diferença entre `==` e `.equals()` em Java?

**R:** `==` compara referências (se apontam para o mesmo objeto na memória). `.equals()` compara o conteúdo, quando a classe sobrescreve o método (como `String`, `Integer`, entidades bem implementadas). Para `String`, sempre use `.equals()` para comparar valor.

---

### P2. O que é imutabilidade? Dê um exemplo.

**R:** Objeto imutável não muda depois de criado. Exemplo: `String` — métodos como `toUpperCase()` retornam nova instância, não alteram a original. Imutabilidade ajuda em concorrência e evita efeitos colaterais.

---

### P3. Diferença entre `ArrayList` e `LinkedList`?

**R:** `ArrayList` usa array interno — acesso por índice O(1), inserção/remoção no meio é mais lenta. `LinkedList` usa nós encadeados — inserção/remoção no meio pode ser mais eficiente, mas acesso por índice é O(n). Na prática, `ArrayList` é usado na maioria dos casos.

---

### P4. O que faz o `Optional`?

**R:** Evita `NullPointerException` deixando explícito que um valor pode não existir. Em vez de retornar `null`, retorna `Optional<T>`. Exemplo: `usuarioRepository.findById(id).orElseThrow(() -> new ResourceNotFoundException("Usuário não encontrado"))`.

---

### P5. O que são Streams em Java?

**R:** API funcional para processar coleções de forma declarativa: `filter`, `map`, `sorted`, `collect`. Exemplo: `lista.stream().filter(u -> u.isAtivo()).map(User::getNome).toList()`.

---

### P6. Diferença entre checked e unchecked exception?

**R:** **Checked** (ex.: `IOException`) — o compilador obriga tratar ou declarar com `throws`. **Unchecked** (ex.: `NullPointerException`, `IllegalArgumentException`) — herdam de `RuntimeException`, não precisam ser declaradas. Em APIs Spring, regras de negócio costumam lançar exceções unchecked customizadas tratadas pelo `@ControllerAdvice`.

---

### P7. O que são os pilares da POO?

**R:**
- **Encapsulamento** — esconder detalhes internos (atributos privados, getters/setters)
- **Herança** — reutilizar código de uma classe pai
- **Polimorfismo** — mesma referência pode apontar para objetos diferentes com comportamentos diferentes
- **Abstração** — expor só o essencial (classes abstratas, interfaces)

---

### P8. O que é SOLID? (resumo júnior)

**R:**
- **S** — Single Responsibility: uma classe, uma responsabilidade
- **O** — Open/Closed: aberta para extensão, fechada para modificação
- **L** — Liskov Substitution: subtipos devem substituir o tipo base sem quebrar
- **I** — Interface Segregation: interfaces específicas, não gigantes
- **D** — Dependency Inversion: depender de abstrações, não de implementações concretas

---

## 2. Spring Boot

### P9. Explique o fluxo de uma requisição REST no Spring Boot.

**R:** Cliente faz HTTP request → **Controller** recebe, valida DTO (`@Valid`) → chama **Service** (regra de negócio) → Service chama **Repository** (acesso a dados) → JPA/Hibernate persiste no banco → resposta sobe a cadeia → Controller retorna JSON com status HTTP adequado. Erros são capturados por `@ControllerAdvice` / `@ExceptionHandler`.

---

### P10. Diferença entre `@Component`, `@Service` e `@Repository`?

**R:** Todos são beans gerenciados pelo Spring (estereótipos de `@Component`):
- `@Component` — bean genérico
- `@Service` — camada de negócio
- `@Repository` — camada de acesso a dados; traduz exceções de persistência

Funcionalmente similares para injeção de dependência; a diferença é semântica/organizacional.

---

### P11. O que é Injeção de Dependência (DI)?

**R:** Em vez de a classe criar suas dependências (`new UserService()`), o Spring injeta via construtor, setter ou campo (`@Autowired`). Benefícios: desacoplamento, facilita testes com mocks e centraliza configuração.

---

### P12. Por que preferir injeção por construtor?

**R:** Dependências ficam explícitas e obrigatórias, facilita testes unitários, evita `@Autowired` em campo (menos testável), e o objeto fica imutável após construção.

---

### P13. O que faz `@Transactional`?

**R:** Delimita uma transação de banco: se tudo der certo, faz **commit**; se lançar exceção não tratada, faz **rollback**. Deve ficar na camada **Service**, não no Controller. Sem ela, cada operação JPA pode commitar separadamente.

---

### P14. O que acontece se `@Transactional` estiver no Controller?

**R:** Funciona tecnicamente, mas é má prática: controller deve só receber/retornar HTTP; regra de negócio e transação ficam no service. Dificulta reuso e testes.

---

### P15. O que é `@RestController` vs `@Controller`?

**R:** `@RestController` = `@Controller` + `@ResponseBody` em todos os métodos — retorna JSON/XML direto. `@Controller` tradicional retorna nome de view (HTML), a menos que use `@ResponseBody` no método.

---

### P16. Para que serve o `application.yml` / `application.properties`?

**R:** Configuração externa da aplicação: datasource, porta, profiles (`dev`, `prod`), logging. Permite mudar comportamento sem recompilar.

---

### P17. O que são Profiles no Spring?

**R:** Conjuntos de configuração por ambiente. Ex.: `application-dev.yml` com H2, `application-prod.yml` com SQL Server. Ativa com `spring.profiles.active=dev`.

---

## 3. JPA / Hibernate / Banco de dados

### P18. Diferença entre `@Entity` e `@Table`?

**R:** `@Entity` marca a classe como entidade JPA. `@Table(name = "tb_usuario")` define o nome da tabela no banco (opcional se o nome da classe coincidir).

---

### P19. O que é Lazy vs Eager loading?

**R:**
- **EAGER** — carrega relacionamento junto com a entidade principal
- **LAZY** — carrega só quando acessado

Padrão recomendado: **LAZY** em `@OneToMany` e `@ManyToMany` para evitar carregar dados desnecessários.

---

### P20. O que é o problema N+1?

**R:** Consulta 1 traz N registros principais; depois, para cada registro, outra query busca o relacionamento → 1 + N queries. Soluções: `JOIN FETCH`, `@EntityGraph`, DTO projection ou query JPQL com join.

---

### P21. Diferença entre `save()` e `saveAndFlush()`?

**R:** `save()` persiste na sessão JPA; o flush para o banco pode ser adiado. `saveAndFlush()` força sincronização imediata com o banco — útil quando você precisa do ID gerado ou validar constraint na hora.

---

### P22. O que é um DTO e por que usar?

**R:** Data Transfer Object — objeto para trafegar dados na API sem expor entidade JPA. Evita expor campos internos, lazy loading na serialização JSON, e desacopla contrato da API do modelo de persistência.

---

### P23. Diferença entre `@OneToMany` e `@ManyToOne`?

**R:** `@ManyToOne` — muitos registros filhos apontam para um pai (lado "many"). `@OneToMany` — um pai tem muitos filhos (lado "one"). `@ManyToOne` é o lado dono da FK na prática.

---

### P24. O que é uma transação ACID?

**R:**
- **A**tomicity — tudo ou nada
- **C**onsistency — regras do banco mantidas
- **I**solation — transações não interferem indevidamente
- **D**urability — após commit, dados persistem

---

### P25. Você usa Oracle. Como falaria de SQL Server na entrevista?

**R:** "Trabalho com Oracle SQL/PLSQL no dia a dia — joins, procedures, otimização de queries. SQL Server segue a mesma lógica relacional; diferenças práticas são tipos (`NVARCHAR`, `DATETIME2`), sintaxe de paginação (`OFFSET/FETCH`) e driver JDBC `mssql-jdbc` no Spring. Já estudei a configuração de datasource e migração de um CRUD para SQL Server."

---

### P26. Escreva mentalmente: query com JOIN e filtro.

**R:**
```sql
SELECT u.id, u.nome, d.nome AS departamento
FROM usuario u
INNER JOIN departamento d ON d.id = u.departamento_id
WHERE u.ativo = 1
ORDER BY u.nome;
```
No SQL Server, `ativo` pode ser `BIT` (0/1).

---

### P27. O que é um índice no banco?

**R:** Estrutura que acelera buscas (como índice de livro), com custo extra em INSERT/UPDATE. Criar em colunas usadas em `WHERE`, `JOIN` e `ORDER BY` frequentes.

---

## 4. APIs REST

### P28. Quando usar GET, POST, PUT, PATCH e DELETE?

**R:**
- **GET** — buscar (idempotente, sem body de alteração)
- **POST** — criar recurso
- **PUT** — substituir recurso inteiro (idempotente)
- **PATCH** — atualizar parcialmente
- **DELETE** — remover (idempotente)

---

### P29. Quando retornar 201, 204, 400, 404 e 409?

**R:**
- **201 Created** — recurso criado (POST)
- **204 No Content** — sucesso sem corpo (DELETE comum)
- **400 Bad Request** — payload inválido / validação falhou
- **404 Not Found** — recurso não existe
- **409 Conflict** — conflito (ex.: e-mail duplicado)

---

### P30. O que é idempotência?

**R:** Repetir a mesma requisição produz o mesmo efeito. GET, PUT e DELETE são idempotentes; POST geralmente não (cria outro recurso a cada chamada).

---

### P31. Como versionar uma API?

**R:** Prefixo na URL (`/api/v1/users`) ou header (`Accept: application/vnd.api.v1+json`). URL é mais comum e simples para júnior.

---

### P32. Como tratar erros de forma padronizada?

**R:** `@ControllerAdvice` com `@ExceptionHandler` retornando JSON consistente:
```json
{
  "timestamp": "2026-08-26T13:00:00",
  "status": 404,
  "error": "Not Found",
  "message": "Usuário 10 não encontrado",
  "path": "/api/users/10"
}
```

---

### P33. O que é OpenAPI/Swagger?

**R:** Especificação para documentar APIs REST (endpoints, parâmetros, responses). No Spring, usa-se SpringDoc para gerar documentação interativa em `/swagger-ui.html`.

---

## 5. Padrões Repository e Service

### P34. Qual a responsabilidade do Repository?

**R:** Abstrair acesso a dados: CRUD, queries. Não deve conter regra de negócio. No Spring Data JPA, estende `JpaRepository<Entity, Id>`.

---

### P35. Qual a responsabilidade do Service?

**R:** Orquestrar casos de uso e regras de negócio: validar regras, chamar um ou mais repositories, controlar transação, lançar exceções de domínio.

---

### P36. Dê um exemplo de regra que fica no Service, não no Repository.

**R:** "Não permitir cadastrar usuário com e-mail duplicado" ou "Calcular desconto conforme tipo de cliente". Repository só busca/salva; Service valida e decide.

---

## 6. Arquitetura hexagonal

### P37. O que é arquitetura hexagonal?

**R:** Também chamada Ports and Adapters. O **domínio** (regras de negócio) fica no centro, sem depender de Spring, HTTP ou banco. **Ports** são interfaces (entrada/saída). **Adapters** implementam: REST controller (entrada), JPA repository (saída), cliente HTTP, Redis.

---

### P38. Hexagonal vs camadas tradicionais (Controller → Service → Repository)?

**R:** Camadas tradicionais organizam por tipo técnico. Hexagonal organiza pelo **domínio** e isola infraestrutura. Service/Repository podem existir nos dois, mas na hexagonal o domínio não importa JPA ou Spring Web.

---

### P39. Por que usar hexagonal?

**R:** Testabilidade (testar regra sem subir banco), independência de framework, trocar banco ou API com menos impacto, código de negócio mais claro.

---

### P40. Onde ficam DTOs na hexagonal?

**R:** Geralmente nos adapters de entrada (web), para converter request/response. O domínio usa entidades/value objects próprios, não DTO de API.

---

## 7. Microserviços

### P41. Monólito vs microserviço — quando usar cada um?

**R:** **Monólito** — app única, mais simples de desenvolver/deployar; bom para times pequenos e domínio ainda instável. **Microserviços** — serviços independentes, deploy separado, escalam por partes; trazem complexidade (rede, observabilidade, consistência). Avanade trabalha com os dois; júnior precisa entender trade-offs.

---

### P42. Como microserviços se comunicam?

**R:** **Síncrona** — HTTP/REST, gRPC. **Assíncrona** — filas/eventos (Kafka, RabbitMQ, Azure Service Bus). Síncrona é mais simples; assíncrona desacopla melhor.

---

### P43. O que acontece se o serviço B cair quando A chama B?

**R:** A falha — timeout, erro 503. Mitigações: timeout configurado, retry com cuidado, circuit breaker, fallback, fila assíncrona. Sempre tratar erro de integração no Service.

---

### P44. O que é API Gateway?

**R:** Ponto único de entrada que roteia para microserviços, centraliza autenticação, rate limit, logging. Ex.: Azure API Management.

---

## 8. Redis (cache)

### P45. Para que serve Redis em uma API?

**R:** Cache em memória de alta performance — reduz carga no banco e melhora tempo de resposta em leituras frequentes (ex.: catálogo de produtos, configurações).

---

### P46. O que é cache-aside?

**R:**
1. App busca no cache
2. Se não achar (cache miss), busca no banco
3. Grava no cache com TTL
4. Retorna ao cliente

No update/delete, invalida ou atualiza o cache.

---

### P47. O que é TTL?

**R:** Time To Live — tempo de expiração da chave no cache. Evita dado obsoleto para sempre.

---

### P48. Quando NÃO usar cache?

**R:** Dados muito voláteis, dados sensíveis sem estratégia clara, operações que exigem consistência forte imediata, ou quando invalidação é complexa demais.

---

## 9. Testes e TDD

### P49. Diferença entre teste unitário e teste de integração?

**R:** **Unitário** — testa uma unidade isolada (service com mocks). **Integração** — testa várias partes juntas (controller + banco com `@SpringBootTest` ou Testcontainers).

---

### P50. O que é TDD?

**R:** Test-Driven Development:
1. **Red** — escreve teste que falha
2. **Green** — implementa o mínimo para passar
3. **Refactor** — melhora código mantendo testes verdes

Garante cobertura e design testável.

---

### P51. Exemplo de TDD (regra de negócio).

**R:** Regra: "Pedido não pode ter quantidade <= 0".

1. Teste: `assertThrows(IllegalArgumentException.class, () -> service.criarPedido(0))`
2. Implementação: `if (qtd <= 0) throw new IllegalArgumentException(...)`
3. Refactor: extrair validação se necessário

---

### P52. Para que serve Mockito?

**R:** Criar mocks de dependências em testes unitários. Ex.: mockar `UserRepository` para testar `UserService` sem banco real.

---

### P53. Diferença entre `@WebMvcTest`, `@DataJpaTest` e `@SpringBootTest`?

**R:**
- `@WebMvcTest` — só camada web (controller)
- `@DataJpaTest` — só persistência (repository)
- `@SpringBootTest` — contexto completo (mais lento, integração)

---

## 10. CI/CD, Git e DevOps

### P54. Diferença entre CI e CD?

**R:** **CI (Continuous Integration)** — integrar código frequentemente com build e testes automáticos. **CD (Continuous Delivery/Deployment)** — entregar/deployar automaticamente após CI passar.

---

### P55. O que colocar num pipeline mínimo Java/Spring?

**R:** Checkout → `./mvnw test` → `./mvnw package` → (opcional) build Docker → deploy. Falhou teste = pipeline vermelho = não mergeia.

---

### P56. O que é um Pull Request?

**R:** Proposta de merge de uma branch para outra. Permite code review, discussão e validação de CI antes de integrar à `main`.

---

### P57. Você usa Azure DevOps — o que falar?

**R:** "Uso Git/GitLab e Azure DevOps no fluxo da MV: branches, commits, acompanhamento de tasks no Jira, pipelines de build/deploy. Entendo a importância de testes no pipeline antes de ir para produção."

---

## 11. Azure e OpenShift (nível entrevista júnior)

### P58. O que é Azure App Service?

**R:** Serviço PaaS da Microsoft para hospedar APIs/web apps sem gerenciar servidor manualmente. Comum para Spring Boot containerizado ou JAR.

---

### P59. Cite 3 serviços Azure úteis para backend.

**R:**
1. **Azure SQL** — banco relacional gerenciado (SQL Server)
2. **Azure Cache for Redis** — cache gerenciado
3. **Azure Key Vault** — segredos e certificados
(Bônus: Application Insights para monitoramento)

---

### P60. O que é OpenShift?

**R:** Plataforma de containers baseada em **Kubernetes** (Red Hat). Orquestra deploy, scaling e rede de aplicações em containers. Avanade usa em projetos enterprise junto com Azure.

---

### P61. Docker vs Kubernetes/OpenShift?

**R:** **Docker** — empacota app + dependências em imagem/container (roda local ou servidor). **Kubernetes/OpenShift** — orquestra muitos containers: restart, scale, load balance, deploy rolling.

---

## 12. Performance (nível júnior)

### P62. Cite 3 causas comuns de API lenta.

**R:**
1. Problema N+1 no JPA
2. Query sem índice no banco
3. Lógica pesada síncrona ou chamada externa sem timeout

---

### P63. Como investigar performance?

**R:** Logs com tempo de resposta, Spring Actuator/metrics, analisar queries (SQL log), profiler (VisualVM), teste de carga básico (JMeter/k6), cache onde fizer sentido.

---

## 13. Spring Security (seus projetos)

### P64. Diferença entre autenticação e autorização?

**R:** **Autenticação** — quem é você (login, JWT). **Autorização** — o que você pode fazer (roles: ADMIN, USER).

---

### P65. O que é JWT?

**R:** JSON Web Token — token assinado com claims (usuário, expiração). Cliente envia no header `Authorization: Bearer <token>`. Stateless — servidor valida assinatura sem sessão.

---

### P66. Para que serve OAuth 2.0?

**R:** Protocolo de autorização delegada — "login com Google", fluxo password/client credentials em APIs. Seus projetos usam OAuth 2.0 com Spring Security.

---

## 14. Perguntas sobre sua experiência (MV e projetos)

### P67. "Conte um bug difícil que você resolveu."

**R (modelo STAR):**
- **S:** API retornava erro intermitente ao salvar usuário
- **T:** Identificar causa e corrigir sem impactar produção
- **A:** Analisei logs, reproduzi local, descobri constraint no banco + payload inválido; corrigi validação no service e mensagem no ExceptionHandler
- **R:** Erro parou, time passou a receber mensagem clara no front

*Substitua por um caso real seu.*

---

### P68. "Fale sobre um projeto seu no GitHub."

**R (modelo):**
"No `validacao_e_seguranca` implementei API REST com Spring Boot, Bean Validation, Spring Security, OAuth 2.0 e JWT. Separei controller, service e repository, tratei exceções globalmente e controlei acesso por perfil. Aprendi a não expor entidade JPA direto e a padronizar erros."

---

### P69. "Como você aprende uma tecnologia nova?"

**R:** "Documentação oficial + projeto prático pequeno. Ex.: para Redis, estudei cache-aside e implementei `@Cacheable` em endpoint de leitura. Anoto dúvidas e reviso em voz alta para fixar."

---

### P70. "Por que Avanade?"

**R:** "Avanade é referência em consultoria Microsoft, com foco em Java/Spring, cloud Azure e projetos enterprise. Busco evoluir tecnicamente com mentoria, certificações e exposição a arquiteturas como microserviços e hexagonal — alinhado ao que já estudo e ao que pratico com Spring Boot."

---

## 15. Perguntas técnicas ao vivo (simulado)

### P71. Implemente mentalmente: buscar usuário por ID ou lançar 404.

**R:**
```java
public UserDTO buscarPorId(Long id) {
    User user = repository.findById(id)
        .orElseThrow(() -> new ResourceNotFoundException("Usuário não encontrado"));
    return mapper.toDTO(user);
}
```

---

### P72. Como evitar e-mail duplicado no cadastro?

**R:** No service, antes de salvar: `if (repository.existsByEmail(email)) throw new BusinessException("E-mail já cadastrado")`. Retornar 409 no ExceptionHandler. Opcional: unique constraint no banco.

---

### P73. Como integrar com API externa no Spring?

**R:** Usar `RestClient` ou `WebClient`, configurar timeout, tratar exceções (`RestClientException`), mapear response para DTO. No service, não no controller.

---

## 16. Roteiro de estudo até quarta (26/08)

| Dia | Foco | Perguntas |
|---|---|---|
| **Dom 23** | Java + Spring | P1–P17 |
| **Seg 24** | JPA + REST + Repository/Service | P18–P36 |
| **Ter 25** | Hexagonal + Micro + Redis + Testes | P37–P53 |
| **Qua 26 manhã** | Azure/DevOps + Experiência + revisão | P54–P70 |

**Manhã de quarta:** releia P9, P13, P20, P37, P41, P45, P49, P67, P68 — são as mais prováveis.

---

## 17. Dicas finais na hora da entrevista

1. **Respire e structure:** "Na camada X eu faria Y porque Z."
2. **Não sabe?** "Ainda não apliquei em produção, mas entendo que..." + conceito
3. **Use seus projetos** como prova — Security, JPA, testes, camadas
4. **Tenha o GitHub aberto** — `validacao_e_seguranca`, `dscommerce_jacoco`, `webService`
5. **Pergunte ao final:** "Quais tecnologias o time usa no dia a dia?" ou "Como é o onboarding de dev júnior?"

Boa entrevista, Lucas!
