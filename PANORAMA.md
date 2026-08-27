# Panorama — Docker, microsserviços, AWS (e afins)

> Material do **Bloco C** (1 semana por tema).  
> Objetivo: **mapa + lab mínimo**, não especialização.

Marque só o tema da semana ativa.

---

## Tema 1 — Docker

### Conceitos
- Container × máquina virtual  
- Imagem × container  
- Dockerfile, registry  
- Volumes e redes (ideia)  
- Docker Compose (vários containers)

### Lab mínimo
- [ ] Instalar Docker  
- [ ] `docker run` de uma imagem simples  
- [ ] Escrever Dockerfile **ou** `docker-compose` com Postgres  
- [ ] Anotar 10 linhas: como rodaria a `api_rest` containerizada  

### Critério de saída
Explica imagem/container/compose e sobe um banco com Compose.

---

## Tema 2 — Microsserviços

### Conceitos
- Monólito × microsserviços  
- Fronteira de serviço (domínio)  
- API Gateway  
- Sync (HTTP) × async (fila/evento)  
- Consistência eventual  
- Observabilidade (log, métrica, trace — ideia)  
- Quando **não** vale a pena

### Lab mínimo
- [ ] Desenhar no papel o monólito `api_rest` vs 2 serviços imaginários  
- [ ] Listar 3 prós e 3 contras pro **seu** contexto de trabalho  
- [ ] (Opcional) Ler 1 artigo curto e resumir em 8 linhas  

### Critério de saída
Explica trade-offs sem discurso de hype.

---

## Tema 3 — AWS (mapa)

### Conceitos (o que é / pra que serve)
- Região × Availability Zone  
- IAM (usuário, role, policy — ideia)  
- EC2 (VM)  
- S3 (objeto/arquivo)  
- RDS (banco gerenciado)  
- VPC (rede isolada — ideia)  
- Security Group (firewall básico)

### Lab mínimo
- [ ] Criar conta free tier **ou** só tour documentado no console  
- [ ] Criar bucket S3 de teste **ou** descrever arquitetura: app + RDS + S3  
- [ ] Anotar custos/cuidados básicos (não deixar recurso ligado à toa)  

### Critério de saída
Monta um desenho: usuário → app → banco/storage na AWS com 1 frase por caixa.

---

## Próximos panoramas (fila)

- CI/CD (GitHub Actions: build + test)  
- Mensageria (fila × tópico)  
- Kubernetes (só o problema que resolve)  
- Observabilidade (Prometheus/Grafana — ideia)  

Um por semana de Bloco C, quando chegar a vez.
