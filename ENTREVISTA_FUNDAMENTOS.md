# Flashcards de entrevista — fundamentos Spring / Java

> Treino: leia a pergunta, feche o arquivo, responda em voz alta em ~1–2 min.  
> Se travar, releia a resposta-modelo e tente de novo no dia seguinte.

---

## 1. Qual a diferença entre Spring e Spring Boot?

**Resposta-modelo (fale assim):**

> **Spring** é um **ecossistema / framework** grande: Injeção de Dependência (IoC), Spring MVC, Spring Data, Security, etc. Você monta a aplicação pedaço a pedaço: configura XML/Java Config, escolhe dependências, sobe um servidor (Tomcat) separado, etc.
>
> **Spring Boot** é uma **forma de usar o Spring com menos configuração**. Ele traz:
> - **starters** (ex.: `spring-boot-starter-web` já puxa MVC + Tomcat embutido)
> - **auto-configuration** (configura beans sozinho conforme o classpath)
> - **servidor embutido** (roda com `main` / `java -jar`)
> - **opinionated defaults** (convenções prontas)
>
> Em resumo: **Boot não substitui o Spring — ele facilita criar apps Spring**. Por baixo, ainda é Spring (IoC, beans, `@RestController`, etc.).

**Analogia curta:** Spring = peças de um carro; Boot = carro já montado pra você sair andando, mas ainda é o mesmo motor.

**No seu projeto:** o `pom.xml` usa `spring-boot-starter-parent` e `spring-boot-starter-web` / `data-jpa`. O `@SpringBootApplication` liga auto-config + component scan.

---

## 2. O que é Injeção de Dependência (DI / IoC)?

> Em vez da classe criar suas dependências com `new`, o **container Spring** cria e **injeta** (via construtor, de preferência). Isso desacopla o código e facilita testes.

Exemplo: `UserController` recebe `UserService` sem fazer `new UserService()`.

---

## 3. O que faz `@SpringBootApplication`?

É um atalho de 3 anotações:
- `@Configuration` — classe de configuração
- `@EnableAutoConfiguration` — liga a auto-configuração
- `@ComponentScan` — procura `@Component`, `@Service`, `@RestController`, etc. no pacote e subpacotes

---

## 4. Controller × Service × Repository

| Camada | Responsabilidade |
|--------|------------------|
| **Controller** | HTTP: recebe request, devolve response/status |
| **Service** | Regra de negócio + `@Transactional` |
| **Repository** | Acesso a dados (JPA / banco) |

Hoje no seu repo o Controller chama o Repository direto — em entrevista diga que o ideal é ter Service no meio.

---

## 5. Spring MVC vs Spring Data JPA (não misturar)

- **Spring MVC / Web:** HTTP, `@RestController`, `@GetMapping`, JSON
- **Spring Data JPA:** persistência, `JpaRepository`, entidades `@Entity`

Boot junta os dois via starters.

---

## 6. O que é um Bean?

> Objeto gerenciado pelo Spring (ciclo de vida, injeção). Classes com `@Component`, `@Service`, `@Repository`, `@Controller` (ou métodos `@Bean`) viram beans.

---

## 7. `application.properties` — pra quê?

> Configuração externa: URL do banco, usuário, `ddl-auto`, portas, etc. Sem recompilar lógica. No Boot, muitas configs têm default; você só sobrescreve o necessário.

---

## 8. JPA × Hibernate × Spring Data JPA

- **JPA:** especificação (API padrão) de persistência
- **Hibernate:** implementação mais comum da JPA
- **Spring Data JPA:** facilita ainda mais (interfaces `JpaRepository`, queries derivadas)

---

## 9. `@Transactional` em uma frase

> Marca um método como unidade atômica: se der erro (RuntimeException), o Spring faz **rollback**; se ok, **commit**. Coloca na **Service**, não no Controller.

---

## 10. REST em uma frase

> Estilo de API sobre HTTP: recursos (`/users`), verbos (`GET/POST/PUT/DELETE`), status codes e, em geral, JSON.

---

## Outras “básicas” que caem muito (pratique igual)

| Pergunta | Ideia da resposta |
|----------|-------------------|
| O que é um starter? | Dependência que agrupa libs + auto-config pra um uso (web, jpa, security) |
| Tomcat embutido? | Servidor vem dentro do jar do Boot; não precisa instalar Tomcat separado |
| `@Autowired` vs construtor? | Construtor é preferido (obrigatório, testável, imutável) |
| `@RestController` vs `@Controller`? | Rest = Controller + `@ResponseBody` (JSON direto) |
| PUT vs PATCH? | PUT costuma substituir o recurso; PATCH atualiza parcial |
| 401 vs 403? | 401 não autenticado; 403 autenticado sem permissão |
| checked vs unchecked? | checked obriga tratar/declarar; RuntimeException não |
| `==` vs `equals`? | `==` referência (objetos); `equals` igualdade de conteúdo |

---

## Como treinar esta semana

1. **Dia 1–2:** perguntas 1 a 5 em voz alta (2x por dia)
2. **Dia 3–4:** perguntas 6 a 10
3. **Dia 5:** peça pra alguém te perguntar aleatório (ou grave áudio)
4. Só depois aprofunde Service/DTO no código

**Regra:** se não explicar Spring × Spring Boot sem olhar, não avance para Security/JWT.
