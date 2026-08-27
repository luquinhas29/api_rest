# Plano de evolução técnica

> Para: Lucas Williams  
> Stack no trabalho: **Angular · Java · Spring · SQL/PLSQL**  
> Objetivo: **evoluir conhecimento de verdade** (profundidade + panorama), no ritmo da sua rotina — sem orientar o plano por entrevista

---

## Sua rotina (não muda)

| Horário | Seg–Sex |
|---------|---------|
| 04:30 | Acorda |
| ~05:40 | Deixa a esposa |
| 06:10 | Chega no trabalho |
| **06:15–07:50** | **Janela principal** (~1h15–1h30) |
| 08:00–18:00 | Expediente |
| ~19:00 | Em casa |
| 19:30 | Academia (exceto **quarta** → futebol) |
| após academia | Dormir cedo |

| Fim de semana | |
|---------------|--|
| **Sábado** | Futebol 06:00–09:00 → casa ~10:00 → estudo **10:30–12:00** |
| **Domingo** | Revisão / consolidar anotações **45–60 min** |

### Regras de ouro

1. Estudo pesado = **manhã 06:15–07:50**
2. Noite pós-academia = no máximo 15 min de revisão leve, ou zero
3. Quarta noite e sábado de manhã = futebol → sem estudo
4. Meta: **~7–8 h/semana**
5. Trabalho alimenta o caderno (`CADERNO.md`): 1 dúvida/linha → entra no bloco certo depois

---

## Duas velocidades de estudo

Você pediu profundidade **e** assuntos mais amplos. Isso pede dois modos:

| Modo | Para quê | Como estudar | Duração típica |
|------|----------|--------------|----------------|
| **Profundo** | Java/Spring, PLSQL | Ler → anotar → **aplicar** (código/script) → revisar | 2 semanas por bloco |
| **Panorama** | Microsserviços, Docker, AWS, etc. | Conceito + desenho + lab mínimo (subir algo / console) | **1 semana** por tema |

Regra: panorama **não** compete com profundo no mesmo dia. É um bloco separado no ciclo.

---

## Estratégia: blocos de foco

Continua valendo: **vários dias na mesma linha**, não “um dia cada tecnologia”.

Ordem sugerida do **ciclo** (repete e aprofunda):

| Ordem | Bloco | Modo | Semanas |
|-------|-------|------|---------|
| 1 | **Java + Spring** (+ projeto `api_rest`) | Profundo | 2 |
| 2 | **SQL / PLSQL** | Profundo | 2 |
| 3 | **Panorama** (Docker **ou** AWS **ou** microsserviços — um por vez) | Panorama | 1 |
| — | Volta ao 1 ou 2 com tema mais avançado | — | — |

Angular: você já pratica no trabalho. Só vira bloco próprio se quiser (depois de 1–2 ciclos), ou 1 domingo de consolidação do que usou na semana.

**Critério pra trocar de bloco:** consegue explicar o checklist do bloco com suas palavras **e** tem um artefato (commit, script `.sql`, nota + lab). Não precisa “terminar a tecnologia”.

---

## Como é uma semana (qualquer bloco)

Horários fixos; o **conteúdo** vem do bloco ativo.

| Dia | Horário | Atividade |
|-----|---------|-----------|
| Seg | 06:15–07:50 | Conceito 1 do bloco |
| Ter | 06:15–07:50 | Conceito 2 (mesmo bloco) |
| Qua | 06:15–07:50 | Conceito 3 ou exercício curto |
| Qui | 06:15–07:50 | **Aplicar** (código Java **ou** script PLSQL **ou** lab Docker/AWS) |
| Sex | 06:15–07:50 | Revisar a semana (só o bloco atual) |
| Sáb | 10:30–12:00 | Bloco longo de prática / projeto |
| Dom | 45–60 min | Consolidar: reler notas, completar `CADERNO.md`, escolher próximo tema do bloco |

```
SEG–QUA  conceito (mesmo bloco)
QUI      prática
SEX      revisão
SÁB      prática longa
DOM      consolidar
```

---

## Bloco A — Java / Spring (profundo · 2 semanas)

Materiais: `FUNDAMENTOS_SPRING.md` · projeto: `PROJETOS.md`

### Semana A1 — bases que sustentam o dia a dia

| Dia | Tema |
|-----|------|
| Seg | Spring × Spring Boot (o que cada um é) |
| Ter | DI / IoC / Bean |
| Qua | Camadas: Controller × Service × Repository |
| Qui | Código: criar `UserService` e tirar Repository do Controller |
| Sex | Revisar Seg–Qui |
| Sáb | `orElseThrow`, PUT, DELETE |
| Dom | Consolidar notas |

### Semana A2 — qualidade no projeto

| Dia | Tema |
|-----|------|
| Seg | `@SpringBootApplication` + starters |
| Ter | REST + status HTTP (visão prática) |
| Qua | `@Transactional` + ideia de ACID |
| Qui | DTOs request/response |
| Sex | Revisão A1+A2 |
| Sáb | `@Transactional` no service + README |
| Dom | Checklist A e anotar dúvidas no `CADERNO.md` |

**Próximos ciclos A (exemplos):** validação, exception handler, testes, JPA lazy/N+1, paginação, Security básico.

---

## Bloco B — SQL / PLSQL (profundo · 2 semanas)

Material: `FUNDAMENTOS_PLSQL.md`  
Prática: pasta sugerida `estudo-plsql/` (scripts seus, **sem dado sensível do trabalho**)

### Semana B1 — SQL sólido

| Dia | Tema |
|-----|------|
| Seg | SELECT avançado: WHERE, ORDER, funções |
| Ter | JOINs (INNER/LEFT) com exemplo próprio |
| Qua | GROUP BY / HAVING + agregações |
| Qui | Escrever 3 queries e explicar o plano mental |
| Sex | Revisar |
| Sáb | Índices + PK/FK (conceito + quando ajuda) |
| Dom | Consolidar |

### Semana B2 — PLSQL de verdade

| Dia | Tema |
|-----|------|
| Seg | Bloco anônimo: `DECLARE` / `BEGIN` / `EXCEPTION` |
| Ter | Procedures × Functions |
| Qua | Cursors (explícito) — ideia e 1 exemplo |
| Qui | Escrever procedure simples (insert/update + tratamento) |
| Sex | Revisar B2 |
| Sáb | Package (spec + body) mínimo **ou** trigger simples |
| Dom | Consolidar + ligar: “quando eu usaria isso no Java/Spring?” |

**Próximos ciclos B:** bulk collect, collections PLSQL, performance básica, dynamic SQL (com cuidado), padrões do seu time.

---

## Bloco C — Panorama (superficial mas útil · 1 semana cada)

Material: `PANORAMA.md`  
Meta: **mapa mental + 1 lab mínimo**, não virar especialista na semana.

Rodízio sugerido (um tema por vez no slot C):

1. **Docker**  
2. **Microsserviços** (conceitos)  
3. **AWS** (visão: o que é VPC, EC2, S3, RDS, IAM — nível mapa)  
4. Depois: Kubernetes (só ideia), mensageria (fila), CI/CD, etc.

### Exemplo — semana Docker

| Dia | Tema |
|-----|------|
| Seg | O que é container × VM |
| Ter | Imagem × container × Dockerfile |
| Qua | `docker run` / `ps` / `logs` (prática) |
| Qui | Dockerfile simples (ou compose app+Postgres) |
| Sex | Revisar |
| Sáb | Subir Postgres (ou a API) com Compose e anotar passos |
| Dom | Desenhar no papel: app → container → banco |

### Exemplo — semana microsserviços

Foco em ideias: monólito × serviços, API gateway, comunicação síncrona × assíncrona, consistência, quando **não** usar. Sem implementar frota de serviços.

### Exemplo — semana AWS

Conta/região, IAM (usuário × role), S3, EC2, RDS — “pra que serve” + um lab gratuito leve (ex.: bucket S3 ou só console tour documentado).

---

## Caderno e progresso

Use `CADERNO.md` (não é lista de entrevista):

- O que estudei
- O que ainda não explica bem
- Ideias do trabalho pra estudar no bloco certo

A cada 2 ciclos (~2 meses):

- [ ] `api_rest` ganhou camadas Service/DTO
- [ ] Tenho scripts PLSQL meus versionados
- [ ] Já fiz pelo menos 1 lab Docker e 1 panorama AWS ou microsserviços
- [ ] Consigo ensinar o último bloco a alguém em 10 min

---

## Trabalho (08:00–18:00) a favor

- Angular/SQL/Java no expediente = prática diária
- Se aparecer algo do **bloco ativo** e você não dominar → 1 linha no caderno → estuda na manhã
- Se for de outro bloco → anota e espera o bloco daquela tech (evita pular de galho)

---

## Mentalidade

Evoluir ≠ estudar tudo todo dia.  
É **profundidade em rodízio** + **panorama curto** pra não ficar só no CRUD eterno.

Horários e futebol/academia ficam; o que muda é o bloco ativo.  
Quando terminar um bloco, diga qual quer puxar (A, B ou C) que montamos a semana seguinte no detalhe.
