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
5. No expediente, quando aparecer algo (Spring, SQL, Angular), anote 1 linha em `GAPS.md` — vira material do **bloco atual** (não muda a tecnologia da semana).

---

## Estratégia: bloco de foco (não rodízio de tecnologias)

### A resposta curta

**Melhor agora: vários dias seguidos na mesma stack** (Java + Spring + o projeto),  
**não** “segunda Spring, terça Java, quarta SQL, sexta Angular”.

### Por quê

| Rodízio 1 tech/dia | Bloco de foco (recomendado) |
|--------------------|-----------------------------|
| Todo dia troca de contexto | Mesma linha por 1–2 semanas |
| Parece produtivo, gruda pouco | Repete, fala, aplica → fixa |
| Angular/SQL “roubam” a manhã do gap da entrevista | Trabalho já te expõe a Angular/SQL |
| Com 75 min/dia, mal aprofunda | 75 min × 4–5 dias no mesmo tema = progresso real |

Você **já pratica** Angular e SQL/PLSQL no expediente. O buraco da entrevista foi **conceito Spring/Java**. Então o estudo formal concentra nisso.

### O que muda na prática

- **Dentro da semana:** muda a *atividade* (ler → falar → codar → revisar), não a *tecnologia*.
- **Entre semanas:** quando o bloco atual estiver “explicável em voz alta”, aí sim troca (ex.: 2 semanas Spring/Java → depois 1 semana SQL entrevista → depois Angular).
- **Domingo:** único dia que mistura perguntas (simulado), de propósito.

### Ordem dos blocos (próximos meses)

| Bloco | Duração | Foco |
|-------|---------|------|
| **1 — Spring + Java + `api_rest`** | **2–3 semanas** (agora) | Spring×Boot, DI, camadas, Optional, Service, CRUD |
| **2 — SQL/PLSQL “de entrevista”** | 1 semana | Explicar JOIN, índice, ACID, SQL×PLSQL (ligar no JPA) |
| **3 — Angular de entrevista** | 1 semana | Component, Service, HTTP, o que você já usa no trabalho |
| Volta ao bloco 1 ou avança Fase B/C | … | Profundidade / portfólio |

Não “termina Java 100%” pra só depois ir pro Angular — **Java nunca termina**. O critério de saída do bloco é: *consigo explicar o checklist do bloco sem olhar*.

---

## Grade na semana (Bloco 1 — Spring / Java / projeto)

Horários iguais; **tema da semana = backend**.

### Segunda a quarta — teoria + falar (mesmo eixo)

**06:15–07:50**

| Bloco | Tempo | O que fazer |
|-------|-------|-------------|
| Ler | 25 min | 1 assunto do eixo Spring/Java (`ENTREVISTA_FUNDAMENTOS.md` ou tema da semana) |
| Falar | 15 min | Explicar / gravar áudio ~2 min |
| Escrever | 15 min | 5–8 linhas com suas palavras |
| Fechar | 5–10 min | Atualizar `GAPS.md` |

**Quarta à noite = futebol** → só manhã.

Progressão típica no Bloco 1 (um tema por dia, mas todos Spring/Java):

1. Spring × Spring Boot  
2. DI / IoC / Bean  
3. `@SpringBootApplication` + starters  
4. Camadas Controller × Service × Repository  
5. `Optional` / `equals` (Java ligado ao seu código)  
6. `@Transactional` (conceito)  
7. REST + status HTTP  

### Quinta — código (`api_rest`)

**06:15–07:50** · aplica o que estudou na semana (Etapa 1 em `PROJETOS.md`).

1 objetivo pequeno + commit (`wip:` ok).

### Sexta — revisão do bloco (não Angular por enquanto)

**06:15–07:50**

- Refazer 5–8 perguntas **só do Bloco 1**
- Ouvir/ler suas anotações da semana
- Anotar o que ainda trava → entra na segunda

Angular fica para o **Bloco 3**, não toda sexta.

### Sábado — projeto (mesmo eixo)

**10:30–12:00** · continua o `api_rest` (PUT/DELETE, DTO, etc.).

### Domingo — simulado

**45–60 min** · 6–8 perguntas em voz alta (maioria do bloco atual + 1–2 surpresa).  
O que falhar vira tema da segunda — **ainda no mesmo bloco**, até fechar.

---

## Resumo visual (Bloco 1)

```
SEG  06:15  Spring/Java — ler + falar
TER  06:15  Spring/Java — próximo conceito (mesmo eixo)
QUA  06:15  Spring/Java — próximo conceito
     noite  futebol ❌
QUI  06:15  Código api_rest (aplica o bloco)
SEX  06:15  Revisão do bloco (sem trocar pra Angular)
SÁB  10:30  Projeto 90 min (mesmo eixo)
DOM  09:00  Simulado 45–60 min

Noites academia: flashcard do BLOCO ATUAL (15 min) ou dormir.
```

**Total:** ~7,5 h/semana · tudo puxando a mesma corda.

---

## Método de fixação (em todo tema)

1. Explicar em voz alta em ~2 min  
2. Escrever 5–8 linhas com suas palavras  
3. Aplicar no código (quinta/sábado)  
4. Commit quando houver mudança no repo  

Se não explica sem olhar → **repete no dia seguinte** (não pula pra outra tecnologia).

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

## Primeira semana (Bloco 1 — só Spring/Java)

Assuma início na **próxima segunda**. Se começar no meio da semana, continue a ordem sem pular pra outra tech.

| Dia | Horário | Conteúdo |
|-----|---------|----------|
| **Seg** | 06:15–07:50 | Spring × Spring Boot — ler, áudio, 8 linhas |
| **Ter** | 06:15–07:50 | DI / IoC / Bean — mesmo eixo |
| **Qua** | 06:15–07:50 | Camadas Controller × Service × Repository |
| **Qui** | 06:15–07:50 | Código: criar `UserService` e mover findAll/findById/save |
| **Sex** | 06:15–07:50 | Revisão: só perguntas Seg–Qua (+ Spring×Boot de novo) |
| **Sáb** | 10:30–12:00 | Código: `orElseThrow` + PUT + DELETE |
| **Dom** | 45–60 min | Simulado: Spring×Boot, DI, camadas, Optional, REST |

Fim do domingo → `GAPS.md`. Se Spring×Boot ainda travar, **segunda repete** (não vai pra SQL/Angular).

---

## Segunda semana (ainda Bloco 1)

| Dia | Conteúdo |
|-----|----------|
| Seg | `@SpringBootApplication` + o que é starter |
| Ter | Java: `==` vs `equals` + `Optional` (seu `.get()` no controller) |
| Qua | `@Transactional` + ACID (conceito; liga no service) |
| Qui | Código: DTOs `UserRequest` / `UserResponse` |
| Sex | Revisão do Bloco 1 (8 perguntas) |
| Sáb | `@Transactional` no `UserService` + commit |
| Dom | Simulado Bloco 1; se ≥80% fluente → na **semana 3** pode abrir Bloco 2 (SQL) |

Angular **não** entra ainda.

---

## Como usar o trabalho a favor (08:00–18:00)

- Angular/SQL no expediente = prática. **Não precisa** estudar os dois toda semana de manhã.
- Se algo do trabalho for do **bloco atual** (ex.: Spring) e você não explicaria → anota no `GAPS.md` e estuda na manhã seguinte.
- Se for de outro bloco (ex.: Angular na semana de Spring) → só anota; estuda quando o bloco daquela tech começar.

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

Quando quiser, me passa as **outras perguntas** da entrevista — encaixo no bloco certo (não espalho na semana toda).
