# GRC Skills para IA: Resultados do Benchmark
### Apresentacao Executiva — Abril 2026

---

## O que sao GRC Skills?

Skills sao **modulos de conhecimento especializado** que podem ser carregados em assistentes de IA para melhorar suas respostas em dominios especificos. Neste caso, testamos 3 skills focadas em Governance, Risk & Compliance:

- **ISO 27001** — Gestao de seguranca da informacao
- **GDPR** — Protecao de dados pessoais (regulamento europeu)
- **NIST CSF 2.0** — Framework de cyberseguranca

**Pergunta central:** A IA responde melhor sobre compliance quando tem uma skill carregada, comparado com seu conhecimento geral?

---

## Como testamos

```
9 cenarios reais de compliance
x 2 condicoes (com e sem skill)
x 3 repeticoes cada
= 54 avaliacoes independentes
```

Cada resposta foi pontuada em 5 criterios de qualidade (escala 1-5):
- **Precisao** — as informacoes estao corretas?
- **Especificidade** — cita controles, artigos, numeros exatos?
- **Estrutura** — formato profissional, pronto para auditoria?
- **Aplicabilidade** — recomendacoes praticas e implementaveis?
- **Completude** — cobre todos os aspectos relevantes?

---

## Resultado Principal

```
                    SEM skill    COM skill    Melhoria
                    ---------    ---------    --------
Score total (/25)     14.6         24.6       +68%
```

### A IA com skill especializada alcanca 98% da pontuacao maxima, contra 58% sem skill.

---

## Melhoria por Criterio

```
Especificidade  ██████████████████████████████ +153%
                A maior melhoria. Sem skill, a IA diz
                "controles de acesso". Com skill, cita
                "A.5.17 (Authentication information),
                Art. 17(3)(a-e), GV.SC-01".

Completude      ████████████████████           +69%
                Sem skill, a IA esquece DPIA, supply
                chain, controles novos de 2022.
                Com skill, nada e omitido.

Estrutura       ████████████████████           +70%
                Sem skill: paragrafos genericos.
                Com skill: tabelas de gap analysis,
                risk registers, audit findings.

Aplicabilidade  ████████████████               +48%
                Com skill: owners, prazos, fases
                30/60/90 dias, evidencias para auditoria.

Precisao        █████████████                  +38%
                Baseline ja razoavel (3.6/5).
                Skill refina e aprofunda.
```

---

## Exemplo Concreto: Incidente de Credenciais

**Cenario:** Desenvolvedor compartilhou credenciais de banco de dados via Slack.

### Resposta SEM skill (resumo):
> "Revogue as credenciais, rotacione senhas, e treine a equipe sobre boas praticas de seguranca da informacao. Isso se relaciona com controles de acesso do ISO 27001."

- Correta, mas vaga
- Nenhum controle especifico citado
- Sem formato de auditoria
- **Score: 13/25**

### Resposta COM skill (resumo):
> **Controles ISO 27001:2022 aplicaveis:**
> - A.5.10 — Uso aceitavel de informacao
> - A.5.14 — Transferencia de informacao
> - A.5.17 — Informacao de autenticacao
> - A.8.12 — Prevencao de vazamento de dados (novo em 2022)
> - A.8.16 — Atividades de monitoramento
> - A.5.24 — Planejamento de gestao de incidentes
>
> **Acoes imediatas (0-24h):** Revogar credenciais, auditar historico Slack, registrar incidente formalmente
> **Curto prazo (1-2 sem):** Implementar secrets manager, configurar DLP
> **Evidencias para auditoria:** Logs do Slack Admin, registro de incidente, checklist de rotacao

- 6 controles especificos com IDs
- Timeline de acoes priorizadas
- Pronto para auditoria
- **Score: 25/25**

---

## Resultados por Framework

| Framework | Sem Skill | Com Skill | Melhoria |
|-----------|-----------|-----------|----------|
| **ISO 27001** | 13.6/25 (54%) | 24.7/25 (99%) | **+82%** |
| **GDPR** | 15.2/25 (61%) | 24.6/25 (98%) | **+61%** |
| **NIST CSF** | 15.1/25 (60%) | 24.6/25 (98%) | **+62%** |

ISO 27001 tem o maior ganho porque seu sistema de numeracao (93 controles, 4 temas, 11 novos em 2022) e o mais complexo — a skill embarca toda essa referencia.

---

## Confiabilidade dos Resultados

| Indicador | Valor | Significado |
|-----------|-------|-------------|
| **Repeticoes** | 3x cada teste | Media e desvio padrao calculados |
| **IC 95%** | Nenhum overlap | Diferenca estatisticamente significativa |
| **Variancia** | SD = 0.50 (com skill) | Respostas altamente consistentes |
| **Amostra** | 54 avaliacoes | 27 baseline + 27 com skill |

**A variancia cai 46% quando a skill esta ativa** — alem de melhores, as respostas se tornam mais previsiveis.

---

## Implicacoes para o Negocio

### 1. Produtividade em Compliance
Uma tarefa que exigiria um consultor senior para formatar corretamente (controles, artigos, tabelas de gap analysis) pode ser feita em minutos com a skill carregada. O output ja sai no formato auditavel.

### 2. Reducao de Risco de Omissao
Sem skill, a IA consistentemente omite elementos criticos:
- Controles novos do ISO 27001:2022 (data masking, DLP, cloud security)
- Requisitos de DPIA do GDPR para dados de saude
- Funcao Govern do NIST CSF 2.0 (ausente no HIPAA)

Com skill, a taxa de completude e **100%** (5.0/5.0, sem variacao).

### 3. Escalabilidade
As skills sao modulares e reutilizaveis. Uma vez configuradas, qualquer membro da equipe obtem o mesmo nivel de qualidade nas respostas, independente do seu nivel de experiencia em GRC.

### 4. Custo-Beneficio
As skills sao open source (GitHub) e custam zero para integrar. O ganho de +68% na qualidade e imediato e sem investimento adicional em infraestrutura.

---

## Proximos Passos Recomendados

1. **Integrar as 3 skills** no workflow de compliance da equipe
2. **Adicionar skills para SOC 2 e HIPAA** (ja disponiveis no mesmo repositorio, nao testadas ainda)
3. **Customizar skills** para incluir politicas internas e controles especificos da organizacao
4. **Reavaliar trimestralmente** conforme frameworks sao atualizados (ex: novas guidelines CNIL, atualizacoes NIST)

---

## Resumo em Uma Frase

> **Skills de GRC melhoram a qualidade das respostas de IA em compliance em 68%, com o maior impacto em especificidade (+153%) e completude (+69%), transformando outputs genericos em entregas prontas para auditoria.**

---

*Benchmark conduzido em 14/04/2026 | Modelo: Claude Opus 4.6 | 54 avaliacoes | 3 frameworks | IC 95% significativo em todos os criterios*
*Relatorio tecnico completo disponivel em: technical-report.md*
