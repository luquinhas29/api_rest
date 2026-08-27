# Fundamentos — Spring / Java

> Material de estudo do **Bloco A**.  
> Método: ler → explicar com suas palavras → aplicar no `api_rest`.

---

## 1. Diferença entre Spring e Spring Boot

**Spring** = ecossistema/framework (IoC, MVC, Data, Security…). Você monta muita configuração na mão.

**Spring Boot** = jeito de usar o Spring com menos configuração: starters, auto-configuration, servidor embutido, defaults opinativos.

Boot **não substitui** o Spring — facilita. Por baixo, sua API ainda é Spring.

No projeto: `spring-boot-starter-web`, `spring-boot-starter-data-jpa`, `@SpringBootApplication`.

---

## 2. Injeção de Dependência (DI / IoC)

Em vez de `new`, o container Spring cria e injeta dependências (prefira **construtor**). Desacopla e facilita testes.

---

## 3. `@SpringBootApplication`

Atalho de:
- `@Configuration`
- `@EnableAutoConfiguration`
- `@ComponentScan`

---

## 4. Controller × Service × Repository

| Camada | Papel |
|--------|-------|
| Controller | HTTP |
| Service | Regra de negócio + transação |
| Repository | Acesso a dados |

---

## 5. Spring Web × Spring Data JPA

- **Web:** `@RestController`, mappings, JSON  
- **Data JPA:** `JpaRepository`, `@Entity`

Boot junta via starters.

---

## 6. Bean

Objeto gerenciado pelo Spring (`@Component`, `@Service`, `@Repository`, `@RestController`, `@Bean`).

---

## 7. `application.properties`

Config externa: banco, porta, `ddl-auto`, etc.

---

## 8. JPA × Hibernate × Spring Data JPA

- **JPA:** especificação  
- **Hibernate:** implementação comum  
- **Spring Data JPA:** repositórios prontos / queries derivadas  

---

## 9. `@Transactional`

Unidade atômica: commit se ok, rollback se RuntimeException (padrão). Preferir na **Service**.

---

## 10. REST (visão prática)

Recursos + verbos HTTP + status + JSON.  
Códigos úteis: 200, 201, 204, 400, 404, 500.

---

## Extra (quando for avançando o Bloco A)

- `@Valid` / Bean Validation  
- `@ControllerAdvice`  
- DTO vs Entity  
- Lazy × Eager / N+1  
- Testes (`@WebMvcTest`, teste de Service)  
