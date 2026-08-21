#!/usr/bin/env python3
"""Gera PDF de perguntas e respostas para entrevista técnica Avanade."""

from pathlib import Path

from fpdf import FPDF

OUT = Path("/workspace/RELATORIO_QA_ENTREVISTA_AVANADE.pdf")
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_I = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"


class PDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("DejaVu", "I", 8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 6, "Q&A Entrevista Técnica — Avanade Back-End Júnior | Lucas Williams", align="L")
        self.ln(8)

    def footer(self):
        self.set_y(-12)
        self.set_font("DejaVu", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, f"Página {self.page_no()}/{{nb}}", align="C")

    def cover(self):
        self.add_page()
        self.ln(40)
        self.set_font("DejaVu", "B", 22)
        self.set_text_color(20, 40, 70)
        self.multi_cell(0, 10, "Relatório de Preparação", align="C")
        self.ln(4)
        self.set_font("DejaVu", "B", 16)
        self.multi_cell(0, 8, "Perguntas e Respostas — Entrevista Técnica", align="C")
        self.ln(8)
        self.set_font("DejaVu", "", 12)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 7, "Avanade — Desenvolvedor(a) Back-End Júnior (R00348516)", align="C")
        self.ln(2)
        self.multi_cell(0, 7, "Candidato: Lucas Williams César Pires", align="C")
        self.ln(2)
        self.multi_cell(0, 7, "Entrevista: quarta-feira 26/08 às 13:00 (com desenvolvedor)", align="C")
        self.ln(16)
        self.set_font("DejaVu", "I", 10)
        self.set_text_color(80, 80, 80)
        self.multi_cell(
            0,
            6,
            "Estude em voz alta. As respostas são modelos — adapte com exemplos reais da MV e dos seus repositórios GitHub.",
            align="C",
        )

    def h1(self, text: str):
        self.ln(4)
        self.set_x(self.l_margin)
        self.set_font("DejaVu", "B", 14)
        self.set_text_color(20, 40, 70)
        self.multi_cell(0, 8, text)
        self.set_draw_color(20, 40, 70)
        self.set_line_width(0.4)
        y = self.get_y()
        self.line(self.l_margin, y, self.w - self.r_margin, y)
        self.set_xy(self.l_margin, y + 4)

    def h2(self, text: str):
        self.ln(2)
        self.set_x(self.l_margin)
        self.set_font("DejaVu", "B", 11)
        self.set_text_color(30, 60, 100)
        self.multi_cell(0, 7, text)
        self.ln(1)

    def body(self, text: str):
        self.set_x(self.l_margin)
        self.set_font("DejaVu", "", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def italic(self, text: str):
        self.set_x(self.l_margin)
        self.set_font("DejaVu", "I", 10)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def bullet(self, text: str):
        self.set_x(self.l_margin)
        self.set_font("DejaVu", "", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5.5, f"-  {text}")

    def qa(self, n: int, pergunta: str, resposta: str, dica: str | None = None):
        if self.get_y() > 250:
            self.add_page()
        self.set_x(self.l_margin)
        self.set_fill_color(232, 240, 250)
        self.set_font("DejaVu", "B", 10)
        self.set_text_color(15, 35, 65)
        self.multi_cell(0, 6, f"P{n}. {pergunta}", fill=True)
        self.ln(2)
        self.set_x(self.l_margin)
        self.set_font("DejaVu", "B", 9)
        self.set_text_color(0, 100, 70)
        self.cell(0, 5, "Resposta modelo:")
        self.ln(5)
        self.body(resposta)
        if dica:
            self.set_x(self.l_margin)
            self.set_font("DejaVu", "I", 9)
            self.set_text_color(90, 70, 20)
            self.multi_cell(0, 5, f"Dica: {dica}")
            self.ln(1)
        self.ln(3)


def build() -> None:
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=16)
    pdf.add_font("DejaVu", "", FONT)
    pdf.add_font("DejaVu", "B", FONT_B)
    pdf.add_font("DejaVu", "I", FONT_I)
    pdf.set_margins(16, 16, 16)

    pdf.cover()

    # ========== SUMÁRIO ==========
    pdf.add_page()
    pdf.h1("Sumário")
    for item in [
        "1. Como usar este material",
        "2. Pitch de 60 segundos",
        "3. Java, Spring Boot e APIs REST",
        "4. JPA, Hibernate e banco de dados",
        "5. Arquitetura (camadas, hexagonal, microserviços)",
        "6. SQL Server, Redis e performance",
        "7. Testes, TDD e qualidade",
        "8. CI/CD, Git e DevOps",
        "9. Azure, OpenShift e cloud (glossário + respostas)",
        "10. Experiência na MV e projetos GitHub",
        "11. Comportamentais (STAR)",
        "12. Como falar das lacunas",
        "13. Perguntas para você fazer ao entrevistador",
        "14. Checklist do dia da entrevista",
    ]:
        pdf.bullet(item)

    # ========== 1 ==========
    pdf.add_page()
    pdf.h1("1. Como usar este material")
    pdf.body(
        "Leia cada pergunta, tape a resposta e responda em voz alta. Depois compare. "
        "Não decore palavra por palavra — memorize a estrutura e use exemplos seus."
    )
    pdf.bullet("Prioridade alta: seções 3, 4, 5, 10 e 11 (o que o dev mais cobra).")
    pdf.bullet("Prioridade média: seções 6, 7 e 8.")
    pdf.bullet("Prioridade glossário: seção 9 (honestidade > inventar experiência).")
    pdf.ln(2)
    pdf.italic(
        "Regra de ouro: se não souber, diga o que sabe, o que faria e como validaria. Nunca invente."
    )

    # ========== 2 ==========
    pdf.h1("2. Pitch de 60 segundos")
    pdf.h2("Pergunta típica: “Me conta um pouco sobre você / sua experiência.”")
    pdf.body(
        "Sou desenvolvedor Java júnior na MV, atuando com Spring Boot, APIs REST, Oracle e Angular. "
        "No dia a dia investigo bugs em produção, integro front, back e banco, e trabalho com Git, Jira, "
        "Azure DevOps e Docker. Tenho projetos públicos no GitHub com JPA, Security, validação e testes. "
        "Estou aprofundando SQL Server, Redis, arquitetura hexagonal, microserviços e CI/CD — stack alinhada "
        "à vaga — e busco evoluir em um ambiente Microsoft/Azure como o da Avanade."
    )
    pdf.italic("Ensaie até caber em ~60 segundos, sem correr.")

    # ========== 3 ==========
    pdf.add_page()
    pdf.h1("3. Java, Spring Boot e APIs REST")

    pdf.qa(
        1,
        "Explique o fluxo de uma requisição no Spring Boot.",
        "A requisição HTTP chega no DispatcherServlet, que roteia para o Controller anotado "
        "(@RestController + @GetMapping/@PostMapping). O Controller recebe PathVariable/RequestBody, "
        "chama o Service (regra de negócio) e o Service usa o Repository (Spring Data JPA) para acessar "
        "o banco. O retorno vira JSON via Jackson e sai com o status HTTP adequado (200, 201, 404…).",
        "Cite um endpoint seu, ex.: GET /users/{id} do api_rest.",
    )

    pdf.qa(
        2,
        "Qual a diferença entre @Controller e @RestController?",
        "@Controller é para MVC com views. @RestController = @Controller + @ResponseBody: "
        "o retorno do método já é o corpo da resposta HTTP (geralmente JSON), típico de API REST.",
    )

    pdf.qa(
        3,
        "O que são status HTTP e quando usar cada um?",
        "200 OK (sucesso GET/PUT), 201 Created (POST criou recurso), 204 No Content (DELETE ok sem corpo), "
        "400 Bad Request (validação/entrada inválida), 401 Unauthorized (não autenticado), "
        "403 Forbidden (sem permissão), 404 Not Found, 409 Conflict (regra de negócio), "
        "500 Internal Server Error (erro inesperado no servidor).",
    )

    pdf.qa(
        4,
        "O que é DTO e por que usar?",
        "DTO (Data Transfer Object) é um objeto só para transporte de dados na API. "
        "Evita expor a entidade JPA diretamente (segurança, acoplamento, lazy loading estourando JSON) "
        "e permite formatar exatamente o contrato do endpoint.",
        "Se no seu projeto ainda devolve entidade, diga que hoje usaria DTO + mapper.",
    )

    pdf.qa(
        5,
        "Como você trata exceções numa API Spring?",
        "Com @ControllerAdvice + @ExceptionHandler centralizo o tratamento: "
        "ResourceNotFound → 404, MethodArgumentNotValidException → 400 com detalhes de validação, "
        "e um handler genérico → 500 sem vazar stack trace sensível para o cliente.",
    )

    pdf.qa(
        6,
        "O que é injeção de dependência e @Autowired?",
        "O Spring cria e injeta as dependências (beans) em vez de você dar new. "
        "Isso facilita teste (mocks) e desacoplamento. Prefiro injeção por construtor "
        "(immutável e obrigatória) em vez de @Autowired em campo.",
    )

    pdf.qa(
        7,
        "Diferença entre PUT e PATCH.",
        "PUT atualiza o recurso de forma completa (substitui). PATCH atualiza parcialmente. "
        "POST cria; GET lê; DELETE remove. APIs devem ser semânticas e, no GET, idempotentes.",
    )

    pdf.qa(
        8,
        "O que você sabe de Spring Security / JWT?",
        "Já pratiquei em projetos com autenticação JWT e OAuth2: o cliente envia token no header Authorization, "
        "um filtro valida o token e o contexto de segurança define o usuário e as roles. "
        "Bean Validation (@Valid, @NotBlank) complementa na entrada da API.",
        "Cite validacao_e_seguranca ou dscommerce se perguntarem evidência.",
    )

    # ========== 4 ==========
    pdf.add_page()
    pdf.h1("4. JPA, Hibernate e banco de dados")

    pdf.qa(
        9,
        "O que é JPA / Hibernate?",
        "JPA é a especificação de ORM em Java; Hibernate é a implementação mais comum. "
        "Mapeio classes (@Entity) para tabelas e uso Spring Data JPA (interfaces Repository) "
        "para CRUD sem escrever SQL repetitivo — ainda posso usar JPQL ou native query quando preciso.",
    )

    pdf.qa(
        10,
        "Explique @Entity, @Id, @GeneratedValue, relacionamentos.",
        "@Entity marca a classe persistente; @Id a chave; @GeneratedValue(IDENTITY) deixa o banco gerar o id. "
        "@ManyToOne / @OneToMany / @ManyToMany modelam relacionamentos. "
        "No api_rest, User tem @ManyToOne com Department via department_id.",
    )

    pdf.qa(
        11,
        "Lazy vs Eager — qual a diferença?",
        "LAZY carrega o relacionamento só quando acessado; EAGER carrega junto com a entidade. "
        "O padrão em @ManyToOne costuma ser EAGER (no JPA clássico) e em coleções LAZY. "
        "Lazy mal usado fora de transação causa LazyInitializationException; Eager demais causa over-fetch.",
    )

    pdf.qa(
        12,
        "O que é o problema N+1 e como evitar?",
        "N+1: 1 query busca a lista e depois N queries buscam o relacionamento de cada item. "
        "Evito com JOIN FETCH na JPQL, @EntityGraph, ou DTO/projeção. "
        "Também reviso logs com spring.jpa.show-sql para detectar.",
    )

    pdf.qa(
        13,
        "Para que serve @Transactional?",
        "Define o limite de uma transação: tudo commit ou rollback. "
        "Uso no Service para operações que alteram mais de uma tabela ou precisam de consistência. "
        "Leitura pode usar readOnly=true. Cuidado com self-invocation e exceções checked.",
    )

    pdf.qa(
        14,
        "Por que findById().get() é perigoso?",
        "Optional.get() sem checagem estoura NoSuchElementException se o id não existir. "
        "O correto é orElseThrow(() -> new ResourceNotFoundException(...)) e devolver 404.",
        "Isso mostra maturidade — mencione melhoria no seu código atual.",
    )

    pdf.qa(
        15,
        "Diferença entre SQL e JPQL.",
        "SQL fala com tabelas/colunas do banco. JPQL fala com entidades/atributos Java. "
        "JPQL é mais portável entre bancos; native query uso quando preciso de dialeto específico ou performance.",
    )

    pdf.qa(
        16,
        "O que é ddl-auto (update, validate, none)?",
        "Controla se o Hibernate altera o schema. update é ok em lab/dev; em produção prefiro "
        "validate/none + migrations (Flyway/Liquibase) para mudanças versionadas e seguras.",
    )

    # ========== 5 ==========
    pdf.add_page()
    pdf.h1("5. Arquitetura")

    pdf.qa(
        17,
        "Repository vs Service — responsabilidades?",
        "Repository: acesso a dados (CRUD, queries). Service: regra de negócio, orquestração, transações. "
        "Controller: HTTP — recebe request, chama service, devolve response. "
        "Não coloco regra de negócio no Controller nem SQL no Controller.",
    )

    pdf.qa(
        18,
        "O que é arquitetura hexagonal (ports & adapters)?",
        "O domínio/caso de uso fica no centro. Ports são contratos (interfaces). "
        "Adapters são implementações: HTTP (entrada), JPA/Redis (saída). "
        "Benefício: testar regra sem subir Spring/banco, e trocar tecnologia sem reescrever o domínio.",
    )
    pdf.italic(
        "Desenho rápido: HTTP Adapter → Port In → Domínio → Port Out → JPA/Redis Adapters"
    )

    pdf.qa(
        19,
        "Monólito vs microserviço — quando usar cada um?",
        "Monólito: um deploy, mais simples no início, bom para time pequeno e domínio ainda nebuloso. "
        "Microserviço: serviços independentes por bounded context — escala e deploy isolados, "
        "mas traz rede, consistência eventual, observabilidade e complexidade operacional. "
        "Para júnior: começo modular no monólito e extraio serviço quando o contexto estiver claro.",
    )

    pdf.qa(
        20,
        "O que é API RESTful de verdade para você?",
        "Recursos nomeados por substantivos (/users), verbos HTTP corretos, status adequados, "
        "payload previsível (DTO), versionamento se necessário, documentação (OpenAPI) e "
        "tratamento de erro consistente. Não é só “ter JSON num @RestController”.",
    )

    pdf.qa(
        21,
        "Como trataria falha ao chamar um serviço externo?",
        "Timeout configurado, tratamento de erro (4xx/5xx), log com correlação, "
        "retry com cuidado (só em erros transitórios), fallback quando fizer sentido, "
        "e não engolir exceção em silêncio. Em cenário avançado: circuit breaker (Resilience4j).",
    )

    # ========== 6 ==========
    pdf.add_page()
    pdf.h1("6. SQL Server, Redis e performance")

    pdf.qa(
        22,
        "Você tem experiência com SQL Server?",
        "Minha base forte é Oracle e PostgreSQL na MV e nos projetos. SQL Server é relacional — "
        "a modelagem, joins, índices e JPA continuam iguais; mudam dialeto, tipos e o driver JDBC. "
        "Já estudei a configuração de datasource SQL Server no Spring e consigo transferir rápido.",
    )

    pdf.qa(
        23,
        "O que é Redis e como usaria numa API?",
        "Redis é um banco em memória, ótimo para cache. Padrão cache-aside: no GET, olho a key no Redis; "
        "se miss, busco no SQL Server/Oracle, gravo no Redis com TTL e retorno; no update, invalido a key. "
        "Reduz carga no banco em leituras quentes (ex.: catálogo de produto).",
    )

    pdf.qa(
        24,
        "Quando NÃO usar cache?",
        "Dado muito volátil, dado sensível sem política clara, ou quando a complexidade de invalidação "
        "é maior que o ganho. Cache errado é bug difícil (dado stale).",
    )

    pdf.qa(
        25,
        "Como você analisa performance num endpoint lento?",
        "1) Reproduzir e medir tempo. 2) Ver SQL gerado (N+1, full scan). 3) Checar índices. "
        "4) Avaliar se cabe cache. 5) Paginação em listas grandes. "
        "Na MV já investigo bugs e lentidão olhando integração e banco — o método é o mesmo.",
    )

    pdf.qa(
        26,
        "O que é índice e por que importa?",
        "Estrutura que acelera busca por colunas de filtro/join. Sem índice certo, o banco faz scan. "
        "Índice demais atrasa escrita. Em entrevista júnior, mostrar que você pensa nisso já diferencia.",
    )

    # ========== 7 ==========
    pdf.add_page()
    pdf.h1("7. Testes, TDD e qualidade")

    pdf.qa(
        27,
        "O que é TDD?",
        "Test-Driven Development: Red → Green → Refactor. "
        "Escrevo o teste que falha, implemento o mínimo para passar, depois limpo o código. "
        "Ajuda a desenhar a API do Service/domínio e evita regressão.",
    )

    pdf.qa(
        28,
        "Diferença entre teste unitário e de integração.",
        "Unitário: isola uma classe (mocks com Mockito), rápido, testa regra. "
        "Integração: sobe contexto Spring / banco (ou Testcontainers) e valida o fio Controller–JPA. "
        "Os dois se complementam; unitário em volume, integração nos fluxos críticos.",
    )

    pdf.qa(
        29,
        "O que você testaria num Service de criar usuário?",
        "Caminho feliz (salva e retorna), e-mail duplicado (regra), validação de entrada, "
        "e se o repository foi chamado corretamente. Com JaCoCo acompanho cobertura, "
        "mas priorizo comportamento importante, não % cega.",
        "Cite dscommerce_jacoco se pedirem evidência.",
    )

    pdf.qa(
        30,
        "O que é mock?",
        "Objeto falso que simula dependência. No unitário do Service, mocko o Repository "
        "para não precisar de banco e controlar o retorno (quando id existe, quando não existe…).",
    )

    # ========== 8 ==========
    pdf.add_page()
    pdf.h1("8. CI/CD, Git e DevOps")

    pdf.qa(
        31,
        "O que é CI e o que é CD?",
        "CI (Continuous Integration): a cada push/PR, build + testes automáticos para pegar quebra cedo. "
        "CD (Continuous Delivery/Deployment): caminho automatizado até homolog/produção com mais controles. "
        "Na MV uso Azure DevOps; nos labs estudo GitHub Actions (checkout → JDK → mvn test).",
    )

    pdf.qa(
        32,
        "Como montaria um pipeline CI simples para Java?",
        "Trigger no push/PR → checkout → setup Java 17 → cache Maven → mvn -B test "
        "(e opcionalmente package). Se falhar teste, o merge não segue. "
        "Depois posso acrescentar build de imagem Docker e deploy.",
    )

    pdf.qa(
        33,
        "Como é seu fluxo com Git?",
        "Branch por feature, commits claros, PR/MR com review, merge na main. "
        "Uso GitLab/Azure DevOps no trabalho e GitHub nos projetos pessoais. "
        "Evito commit grande sem contexto; prefiro histórico legível.",
    )

    pdf.qa(
        34,
        "Para que serve Docker no seu dia a dia?",
        "Padronizar ambiente: subir app/dependências (banco, Redis) sem “na minha máquina funciona”. "
        "Docker Compose orquestra vários containers juntos no lab local.",
    )

    # ========== 9 ==========
    pdf.add_page()
    pdf.h1("9. Azure, OpenShift e cloud")

    pdf.body(
        "Avanade é parceira Microsoft — vão valorizar interesse e vocabulário correto, "
        "não experiência inventada. Seja honesto."
    )

    pdf.qa(
        35,
        "O que você sabe de Azure?",
        "Tenho Azure DevOps na prática (pipelines/boards no trabalho). Estudei os serviços que fazem "
        "sentido para API Java: App Service ou Container Apps (hospedar), Azure SQL (SQL Server gerenciado), "
        "Azure Cache for Redis, Key Vault (segredos) e Application Insights (monitoramento). "
        "Ainda não tenho deploy produtivo meu na Azure, mas entendo o papel de cada um.",
    )

    pdf.qa(
        36,
        "O que é OpenShift?",
        "Plataforma Kubernetes enterprise da Red Hat: orquestra containers (Pod, Deployment, Service) "
        "e expõe aplicação (Route). Conceito base é o mesmo do Kubernetes, com ferramentas e "
        "segurança corporativas por cima.",
    )

    pdf.h2("Glossário rápido (decore)")
    for line in [
        "App Service / Container Apps — hospeda API web ou containers.",
        "Azure SQL — SQL Server gerenciado na nuvem.",
        "Azure Cache for Redis — Redis gerenciado.",
        "Key Vault — senhas e connection strings.",
        "Application Insights — telemetria e diagnóstico.",
        "OpenShift — Kubernetes enterprise (Pod, Deployment, Service, Route).",
    ]:
        pdf.bullet(line)

    # ========== 10 ==========
    pdf.add_page()
    pdf.h1("10. Experiência na MV e projetos")

    pdf.qa(
        37,
        "O que você faz na MV no dia a dia?",
        "Desenvolvimento Java/Spring: APIs REST, manutenção, correção de bugs em produção, "
        "integração com Angular no front e Oracle no banco (SQL/PLSQL). "
        "Trabalho com Git/GitLab, Jira, Azure DevOps e Docker, sempre buscando entender o fluxo ponta a ponta "
        "antes de mudar código em produção.",
        "Prepare 1 exemplo concreto de bug ou feature (sem dados sensíveis).",
    )

    pdf.qa(
        38,
        "Me explica um projeto do seu GitHub.",
        "Exemplo api_rest: API Spring Boot 3 / Java 17 com JPA, PostgreSQL, entidades User e Department "
        "(@ManyToOne), endpoints GET lista, GET por id e POST. "
        "Hoje eu evoluiria com camada Service, DTO, Exception Handler e testes — "
        "e é exatamente esse tipo de evolução que me interessa na Avanade.",
    )

    pdf.qa(
        39,
        "Por que quer sair / por que a Avanade?",
        "Quero crescer em backend com boas práticas, arquitetura, cloud Microsoft e times maduros de engenharia. "
        "A vaga pede Spring, SQL Server, Redis, hexagonal e CI/CD — é o caminho que já estou estudando. "
        "Avanade combina minha base Java com o ecossistema Azure.",
    )

    pdf.qa(
        40,
        "Qual sua maior fraqueza técnica?",
        "Ainda estou aprofundando microserviços, Redis em produção e cloud Azure além do DevOps. "
        "Compenso com estudo dirigido, labs no GitHub e honestidade sobre o que já pratiquei vs o que estudei. "
        "Na MV minha força é entregar e depurar no stack Java/Spring/Oracle.",
    )

    pdf.qa(
        41,
        "Onde se vê em 2 anos?",
        "Como backend sólido: APIs bem desenhadas, testes, CI, noção forte de dados e cache, "
        "contribuindo em code review e evoluindo para arquitetura (hexagonal/microsserviços) "
        "com mais autonomia.",
    )

    # ========== 11 ==========
    pdf.add_page()
    pdf.h1("11. Comportamentais (STAR)")
    pdf.body(
        "Método STAR: Situação → Tarefa → Ação → Resultado. "
        "Preencha com casos REAIS seus antes da entrevista."
    )

    pdf.h2("P42. Conte um bug difícil que você resolveu.")
    pdf.italic(
        "Estrutura: situação em produção/homolog → o que era sua responsabilidade → "
        "como investigou (log, SQL, integração front/back) → o que corrigiu e o impacto."
    )
    pdf.body(
        "Resposta-guia: “Tivemos [sintoma]. Eu precisei [tarefa]. Investiguei [passos]. "
        "A causa era [raiz]. Corrigi [ação] e o resultado foi [usuário/sistema estável / tempo].”"
    )

    pdf.h2("P43. Como você aprende uma tecnologia nova sob prazo?")
    pdf.body(
        "Defino o mínimo necessário para a tarefa, estudo doc oficial + 1 exemplo, "
        "faço um spike pequeno, valido com teste ou prova manual, e só então integro na feature. "
        "Documento o essencial para o time. Evito tutorial infinito sem entregar."
    )

    pdf.h2("P44. Situação em que pediu ajuda / colaborou.")
    pdf.body(
        "Mostre humildade + ownership: “bloqueei X tempo, juntei evidências (erro, o que já tentei), "
        "pedi ajuda ao colega/sênior com pergunta objetiva, implementei a solução e compartilhei o aprendizado.”"
    )

    pdf.h2("P45. Como prioriza correção vs feature?")
    pdf.body(
        "Impacto no usuário e risco em produção primeiro. Bug crítico > feature. "
        "Alinho com o time/PO no Jira. Se feature e bug competem, explico trade-off com dados."
    )

    pdf.h2("P46. Conte um conflito / feedback difícil.")
    pdf.body(
        "Foque em profissionalismo: ouviu, esclareceu expectativa, ajustou comunicação ou código, "
        "e manteve o objetivo do time. Evite falar mal de colega ou empresa."
    )

    # ========== 12 ==========
    pdf.add_page()
    pdf.h1("12. Como falar das lacunas")

    pdf.h2("SQL Server")
    pdf.body(
        "“Venho de Oracle/PostgreSQL; a lógica SQL é a mesma. Já estudei o driver e o datasource "
        "do SQL Server no Spring e consigo produzir rápido.”"
    )

    pdf.h2("Redis")
    pdf.body(
        "“Usaria cache-aside no GET com TTL e invalidação no update. Ainda não operei Redis em produção "
        "na MV, mas o padrão está claro e pratiquei o conceito no estudo.”"
    )

    pdf.h2("Hexagonal")
    pdf.body(
        "“Domínio no centro, ports como contratos, adapters para HTTP e banco — facilita teste isolado. "
        "Hoje trabalho em camadas; sei como migrar um caso de uso para esse estilo.”"
    )

    pdf.h2("Azure / OpenShift")
    pdf.body(
        "“Tenho Docker e Azure DevOps na prática. Estudei App Service, Azure SQL, Redis Cache, "
        "Key Vault, Insights e OpenShift como Kubernetes enterprise. Não vou inventar deploy que não fiz.”"
    )

    pdf.h2("Inglês")
    pdf.body(
        "Se perguntarem: seja honesto sobre o nível e diga que lê documentação técnica e está evoluindo "
        "comunicação. Avanade valoriza times globais — mostre disposição."
    )

    # ========== 13 ==========
    pdf.h1("13. Perguntas para o entrevistador")
    pdf.body("Faça 1 ou 2 no final — demonstra interesse real:")
    pdf.bullet("Quais são os principais desafios técnicos do time hoje?")
    pdf.bullet("Como é o fluxo de code review e CI/CD no projeto?")
    pdf.bullet("No dia a dia do júnior, o quanto é API nova vs manutenção/bug?")
    pdf.bullet("Quais tecnologias o time mais usa no backend atualmente (SQL Server, Redis, mensageria)?")
    pdf.bullet("Como é o onboarding técnico nas primeiras semanas?")

    # ========== 14 ==========
    pdf.h1("14. Checklist do dia da entrevista")
    for item in [
        "Entrar 10 minutos antes (link, câmera, microfone, fone testados).",
        "Repo favorito aberto no navegador.",
        "Este PDF / anotações de 1 página ao lado (não ler na tela).",
        "Pitch ensaiado 1–2 vezes na manhã — sem estudar assunto novo.",
        "Água, ambiente silencioso, celular no silencioso.",
        "Se travar: o que sei → o que faria → como validaria.",
        "Terminar com uma pergunta boa.",
        "Agradecer o tempo do entrevistador.",
    ]:
        pdf.bullet(item)

    pdf.ln(8)
    pdf.set_font("DejaVu", "B", 11)
    pdf.set_text_color(20, 40, 70)
    pdf.multi_cell(0, 7, "Você já tem base de júnior em produção. O diferencial é clareza.", align="C")
    pdf.ln(2)
    pdf.set_font("DejaVu", "I", 10)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(0, 6, "Boa entrevista, Lucas.", align="C")

    pdf.output(OUT)
    print(f"PDF gerado: {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    build()
