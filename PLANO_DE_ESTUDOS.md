# Plano de estudos — ajustado à sua rotina real

> Para: Lucas Williams  
> Stack no trabalho: **Angular + Java + Spring + SQL/PLSQL**  
> Objetivo: fechar lacunas de entrevista (ex.: Spring × Spring Boot) sem quebrar sono, academia e futebol

---

## Sua rotina (base do plano)

| Horário | Seg–Sex |
|---------|---------|
| 04:30 | Acorda |
| ~05:40 | Deixa a esposa |
| 06:10 | Chega no trabalho |
| **06:15–07:50** | **Janela principal de estudo** (~1h15–1h30) |
| 08:00–18:00 | Expediente |
| ~19:00 | Chega em casa |
| 19:30 | Academia (exceto **quarta** → futebol) |
| após academia | Higiene + dormir cedo (acordar 04:30) |

| Fim de semana | |
|---------------|--|
| **Sábado** | Futebol 06:00–09:00 → em casa ~10:00 → estudo **10:30–12:00** |
| **Domingo** | Simulação de entrevista + revisão leve **09:00–10:00** (ou outro horário fixo) |

### Regras de ouro (pra não abandonar)

1. **Estudo pesado = manhã no trabalho (06:15–07:50).** Cabeça fresca, sem academia no meio.
2. **Noite depois da academia = no máximo 15 min** de flashcard no celular, ou **zero**. Sono > mais uma hora forçada.
3. **Quarta à noite e sábado de manhã** são futebol → não planejar código nesses horários.
4. Meta realista: **~7–8 h/semana**, não 12. Constância ganha de maratona.
5. No expediente, quando aparecer algo (Spring, SQL, Angular), anote 1 linha em `GAPS.md` — vira material de estudo no dia seguinte.

---

## Grade semanal fixa — o que estudar cada dia

### Segunda — fundamentos Spring (entrevista)

**06:15–07:50 · ~60–75 min**

| Bloco | Tempo | O que fazer |
|-------|-------|-------------|
| Leitura | 25 min | 1 tema de `ENTREVISTA_FUNDAMENTOS.md` |
| Falar | 15 min | Explicar em voz baixa / gravar áudio de 2 min |
| Escrever | 15 min | 5–8 linhas com **suas** palavras |
| Fechamento | 5 min | Marcar no `GAPS.md` se ainda trava |

**Semana 1 (segunda):** Spring × Spring Boot (pergunta 1)  
**Semanas seguintes:** DI/IoC → `@SpringBootApplication` → Bean → starters → Tomcat embutido

**Noite:** off ou 10 flashcards no celular.

---

### Terça — Java que entrevista cobra

**06:15–07:50**

| Foco rotativo (1 por terça) |
|-----------------------------|
| OOP (encapsulamento, interface × classe abstrata) |
| `==` vs `equals` / `hashCode` |
| `List` × `Set` × `Map` |
| `Optional` e por que evitar `.get()` cego |
| Exceções checked × unchecked |
| Streams (map/filter/collect) — nível básico |

**Formato:** 30 min teoria/exemplo → 30 min exercício pequeno (pode ser no papel ou no IntelliJ) → 10 min explicar em voz alta.

**Noite:** off (academia).

---

### Quarta — SQL / PLSQL (aproveita o que você já usa)

**06:15–07:50** · à noite é futebol → **só manhã**

| Bloco | O que fazer |
|-------|-------------|
| 20 min | Pegar **1 query ou procedure do trabalho** (sem dado sensível) e reescrever o raciocínio |
| 25 min | Conceito de entrevista: JOIN, índice, PK/FK, transação ACID, ou diferença SQL × PLSQL |
| 20 min | Ligar com JPA: “isso no banco vira o quê na Entity / Repository?” |
| 10 min | Explicar em 2 min como se fosse entrevista |

**Ideia:** você já pratica SQL no dia a dia — o gap costuma ser **explicar**, não só executar.

---

### Quinta — código no `api_rest` (projeto)

**06:15–07:50** · sessão de implementação

Checklist da Etapa 1 (`PROJETOS.md`), um pedaço por quinta:

1. Criar `UserService` e mover lógica do controller  
2. Injeção por construtor  
3. `orElseThrow` + 404  
4. PUT / DELETE  
5. DTOs  
6. `@Transactional` no service  

**Regra:** 1 objetivo pequeno por quinta + commit no fim (mesmo que incompleto: `wip:`).

**Noite:** off (academia).

---

### Sexta — Angular no trabalho + revisão da semana

**06:15–07:50**

| Semana ímpar | Semana par |
|--------------|------------|
| Angular: 1 conceito (componentes, services, RxJS básico, HTTP client, rotas) | Revisão: reler áudios/anotações Seg–Qui + refazer 5 perguntas que falhou |

**Por quê Angular na sexta:** você usa no trabalho; 1 conceito/semana vira resposta de entrevista full-stack sem comer o foco do backend.

**Noite:** off. Se sobrar energia, **só** listar no `GAPS.md` dúvidas da semana.

---

### Sábado — bloco longo de projeto

**10:30–12:00** (depois do futebol e de comer / tomar banho)

- Continuar o que começou na quinta no `api_rest`
- Ou README / teste / Docker quando chegar nessa etapa
- Fechar com: commit + 5 linhas “o que aprendi hoje”

**Tarde/noite:** livre (descanso de verdade).

---

### Domingo — modo entrevista

**45–60 min** (ex.: 09:00–10:00)

1. 6–8 perguntas aleatórias (fundamentos + o que errou na entrevista)
2. Responder em voz alta com cronômetro (2 min cada)
3. Anotar o que travou → vira tema da **segunda**
4. **Não** abrir IDE (exceto se for mostrar um trecho de 5 min)

---

## Resumo visual da semana

```
SEG  06:15  Spring / entrevista (teoria + falar)
TER  06:15  Java (teoria + exercício curto)
QUA  06:15  SQL/PLSQL → conceito + ligação com JPA
     noite  futebol ❌ sem estudo
QUI  06:15  Código api_rest (1 tarefa)
SEX  06:15  Angular OU revisão da semana
SÁB  10:30  Projeto 90 min
DOM  09:00  Simulado de entrevista 45–60 min

Noites com academia (seg/ter/qui/sex): no máximo flashcard 15 min ou dormir.
```

**Total estimado:** ~7,5 h/semana.

---

## Método de fixação (em todo tema)

1. Explicar em voz alta em ~2 min  
2. Escrever 5–8 linhas com suas palavras  
3. Aplicar no código (quinta/sábado) quando for tema de Spring/Java  
4. Commit quando houver mudança no repo  

Se não explica sem olhar → ainda não fixou → repete na segunda.

---

## Diagnóstico (preencher e atualizar)

| Pergunta | Consegui? | Prioridade |
|----------|-----------|------------|
| **Spring × Spring Boot** | **não (entrevista)** | **P0** |
| DI / IoC / Bean | | P0 |
| `@SpringBootApplication` | | P0 |
| Controller × Service × Repository | | P0 |
| API REST + status HTTP | | P1 |
| `@Transactional` / ACID | | P1 |
| JPA × Hibernate × Spring Data | | P1 |
| SQL JOIN / índice / transação | | P1 (você usa — foque em explicar) |
| Angular: module/component/service | | P2 |
| DTO, validação, 404 | | P2 |

Detalhes: `GAPS.md` · respostas-modelo: `ENTREVISTA_FUNDAMENTOS.md` · tarefas de código: `PROJETOS.md`

---

## Mapa de fases (continua valendo)

### Fase A — falar o básico sem travar (~2–3 semanas nesta rotina)

Spring × Boot, DI, camadas, REST, Java OOP básico, SQL que você já usa mas explica mal.

### Fase B — Spring “de verdade” no `api_rest` (~3–4 semanas)

Service, DTO, CRUD completo, `@Transactional`, validação, exception handler, testes.

### Fase C — portfólio / júnior+ (~3–4 semanas)

Docker, Flyway, Swagger, Security básico, CI.

Não pule a Fase A: a entrevista mostrou que o buraco está no **conceito**, não só no código.

---

## Primeira semana (calendário concreto)

Assuma que “semana 1” começa na **próxima segunda**. Ajuste as datas se começar no meio da semana (pule o que já passou e continue a ordem).

| Dia | Horário | Conteúdo exato |
|-----|---------|----------------|
| **Seg** | 06:15–07:50 | Spring × Spring Boot — ler, gravar áudio, escrever 8 linhas |
| **Ter** | 06:15–07:50 | Java: `==` vs `equals` + `Optional` (ligar ao `.get()` do seu `UserController`) |
| **Qua** | 06:15–07:50 | SQL: o que é JOIN + PK/FK; relacionar com `User`/`Department` do projeto |
| **Qui** | 06:15–07:50 | Código: criar `UserService` e mover `findAll` / `findById` / `save` do controller |
| **Sex** | 06:15–07:50 | Revisar áudios Seg–Qui + 5 perguntas de `ENTREVISTA_FUNDAMENTOS.md` |
| **Sáb** | 10:30–12:00 | Código: PUT + DELETE + `orElseThrow` no service |
| **Dom** | 45–60 min | Simulado: Spring×Boot, DI, camadas, equals, JOIN, REST |

No fim do domingo: atualizar `GAPS.md` com o que ainda falhou.

---

## Segunda semana (próximo ciclo)

| Dia | Conteúdo |
|-----|----------|
| Seg | DI / IoC / Bean + `@Autowired` vs construtor |
| Ter | Collections: `List` × `Map` + 1 exercício |
| Qua | Transação no banco (ACID) + SQL × PLSQL (1 diferença clara) |
| Qui | Código: DTOs `UserRequest` / `UserResponse` |
| Sex | Angular: o que é Service no Angular × Service no Spring (comparar) |
| Sáb | `@Transactional` no `UserService` + README mínimo |
| Dom | Simulado 8 perguntas (incluir Angular 1 pergunta) |

---

## Como usar o trabalho a favor (08:00–18:00)

Sem estudar “escondido” o dia todo. Só:

- Quando mexer em Spring/SQL/Angular, pergunte: *“Se me perguntassem isso na entrevista, eu explicaria?”*
- Se não → 1 linha no `GAPS.md` no celular
- No dia certo da grade (seg/ter/qua/sex), isso vira o tema

---

## Medir progresso (a cada 2 semanas)

- [ ] Explico Spring × Boot sem olhar  
- [ ] Explico DI + camadas Controller/Service/Repository  
- [ ] `UserService` existe no repo  
- [ ] Fiz 2 simulados de domingo  
- [ ] Academia + futebol mantidos (plano sustentável)  
- [ ] Sono ok na maioria dos dias  

Se o plano competir com sono ou academia, **corte a noite**, nunca a manhã.

---

## Mentalidade

Você não tem “falta de tempo” — tem **uma janela boa** (06:15–07:50) e um bloco de sábado.  
Com 7h/semana bem usadas, em 1–2 meses a entrevista básica para de te derrubar.

Quando quiser, me passa as **outras perguntas** que caíram na entrevista que eu encaixo na grade do dia certo.
