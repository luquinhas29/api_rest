# Fundamentos — SQL / PLSQL

> Material do **Bloco C**.  
> Pratique em scripts seus (Oracle ou ambiente de estudo). **Não** versionar dado sensível do trabalho.

Sugestão: criar pasta `estudo-plsql/` neste repo ou repo separado só de scripts.

---

## SQL — checklist profundo

### 1. SELECT com intenção
- `WHERE`, `ORDER BY`, aliases
- Funções comuns (`NVL`/`COALESCE`, `TRUNC`, `TO_CHAR` — conforme dialeto)

### 2. JOINs
- `INNER JOIN` vs `LEFT JOIN`
- Quando o LEFT “explode” linhas
- Relacionar com suas entities `User` / `Department` (FK)

### 3. Agregação
- `GROUP BY`, `HAVING`, `COUNT/SUM/AVG`
- Diferença WHERE × HAVING

### 4. Integridade
- PK, FK, UNIQUE, CHECK
- O que o banco garante vs o que a aplicação garante

### 5. Índice (visão prática)
- Pra que serve
- Quando ajuda / quando atrapalha escrita
- Índice ≠ magia: precisa bater com o filtro da query

### 6. Transação no banco
- BEGIN / COMMIT / ROLLBACK (conceito)
- ACID em uma frase cada letra
- Ligação com `@Transactional` no Spring

---

## PLSQL — checklist profundo

### 1. Bloco anônimo
```text
DECLARE
  -- variáveis
BEGIN
  -- lógica
EXCEPTION
  WHEN OTHERS THEN
    -- tratamento
END;
/
```

### 2. Procedure × Function
- Procedure: faz algo (pode não retornar valor)
- Function: retorna valor; restrições de uso em SQL

### 3. Cursor
- Implícito vs explícito
- `OPEN` / `FETCH` / `CLOSE` ou `FOR r IN (...)`

### 4. Package
- Spec (contrato) + Body (implementação)
- Por que organizar em package no dia a dia

### 5. Trigger (conceito)
- BEFORE/AFTER, row × statement
- Quando faz sentido / quando vira lógica escondida demais

### 6. Exception handling
- Exceções pré-definidas vs próprias
- Não engolir erro sem log/raise

---

## Exercícios mínimos (por ciclo B)

1. 3 queries com JOIN + agregação comentadas  
2. 1 procedure de insert/update com `EXCEPTION`  
3. 1 function simples usada num `SELECT`  
4. 1 package com 2 rotinas  
5. Parágrafo: “quando eu faria isso no PLSQL vs na Service Java”

---

## Ligação com seu trabalho

No expediente, quando mexer em procedure/package:

1. Anote o **padrão** (não o dado) no `CADERNO.md`
2. No Bloco B, reproduza uma versão **simplificada** e sua
3. Explique o fluxo: app Java → chama SQL/PLSQL → commit/rollback
