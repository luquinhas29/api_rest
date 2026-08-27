# Fundamentos — Angular

> Material do **Bloco B**.  
> Método: ler → anotar com suas palavras → aplicar num app de estudo (ou reproduzir padrão do trabalho **sem** código proprietário).

Ajuste detalhes à **versão do Angular** que você usa no trabalho (modules clássicos vs standalone).

---

## 1. O que é Angular

Framework para **SPA** (Single Page Application): a UI atualiza no browser sem recarregar a página inteira a cada clique. Usa **TypeScript**.

Papel no seu stack: Angular (front) ↔ HTTP ↔ Spring Boot (API) ↔ SQL/PLSQL (banco).

---

## 2. Component

Unidade de UI: **template** (HTML) + **classe** (TS) + estilo.

Ideias-chave:
- Seletor
- Data binding: interpolação `{{ }}`, property binding `[ ]`, event `( )`, two-way `[(ngModel)]` (se usar FormsModule)

---

## 3. Module × standalone

- **NgModule:** agrupa components, imports, providers (estilo clássico)
- **Standalone:** component declara seus próprios `imports` (estilo mais novo)

No estudo: siga o padrão do seu projeto de trabalho para não estudar um e trabalhar outro.

---

## 4. Service + DI no Angular

Classe com `@Injectable` para lógica compartilhada (chamar API, estado simples).  
O Angular também tem **injeção de dependência** (parecido na ideia com o Spring, diferente na implementação).

---

## 5. HttpClient

Faz GET/POST/PUT/DELETE para a API.  
Retorna **Observable** (RxJS) — não é `Promise` “puro” (embora possa converter).

Fluxo típico: Component chama Service → Service usa `HttpClient` → API Spring.

---

## 6. RxJS (nível prático)

No começo, domine:
- `subscribe` (e lembrar de evitar leak — ou usar `async` pipe)
- `map`, `tap`, `catchError` (ideia)
- Diferença Observable × valor “já resolvido”

Não tente decorar todo o RxJS de uma vez.

---

## 7. Router

Navegar entre telas sem reload: rotas, `routerLink`, parâmetros (`:id`).

---

## 8. Forms

Escolha **um** para o primeiro ciclo:
- Template-driven, ou
- Reactive forms (`FormGroup` / `FormControl` + validators)

Validar campo obrigatório e mostrar erro na tela já é ganho grande.

---

## Checklist de saída do Bloco B (primeiro ciclo)

- [ ] Explico component × service × module/standalone  
- [ ] Faço um GET numa API e mostro na tela  
- [ ] Sei desenhar: tela → service → HTTP → backend  
- [ ] Montei 1 form simples com validação  

---

## Próximos ciclos

Interceptors (token), route guards, `OnPush`, signals, lazy loading de rotas, testes (`TestBed`), acessibilidade básica.
