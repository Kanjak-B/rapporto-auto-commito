# rapporto-auto-commito
# CommitAutoRapporti — Automatisation intelligente des rapports journaliers à partir des commits Git

CommitAutoRapporti collecte automatiquement les commits de plusieurs dépôts Git d’une organisation, organise et enrichit ces informations, puis génère un rapport clair et professionnel à l’aide d’une IA (OpenAI / Gemini). Le rapport peut ensuite être exporté en PDF, Word ou TXT et distribué via Email, Slack, WhatsApp, Telegram ou Discord.

## Fonctionnalités principales

- Collecte des commits depuis plusieurs dépôts (organisation, liste de dépôts ou monorepo).
- Agrégation et regroupement par date, auteur, composant/dossier, type de travail (fix, feat, docs, etc.).
- Résumé et reformulation intelligente des commits via un modèle IA (OpenAI / Gemini).
- Génération de rapports exportables : PDF, DOCX (Word), TXT.
- Distribution automatique : Email, Slack, Telegram, WhatsApp, Discord.
- Configuration flexible (filtrage de commits, templates, fréquence d’exécution).
- Mode dry-run pour validation avant envoi.

## Cas d'utilisation

- Rapports journaliers/hebdomadaires pour les managers et équipes.
- Rétrospectives automatiques basées sur l’activité Git.
- Synthèse pour reporting externe (clients, stakeholders).
- Archivage automatique des journaux de développement.

## Architecture (vue d'ensemble)

1. Collecteur Git — interroge les API Git (GitHub/GitLab) ou clones locaux pour récupérer les commits.
2. Normalisateur — nettoie et structure les messages de commit, extrait les métadonnées.
3. Agrégateur — groupe et catégorise les changements (par auteur, dossier, type).
4. IA — appelle l’API (OpenAI/Gemini) pour générer des résumés lisibles et des sections narratives.
5. Générateur de rapport — rend en Markdown puis convertit en PDF/DOCX/TXT.
6. Transporteur — envoie les rapports via Email / Slack / Telegram / WhatsApp / Discord.
7. Scheduler — exécute le pipeline selon une planification (cron / GitHub Actions).

## Prérequis

- Node.js >= 18 (ou conteneur Docker)
- Accès aux dépôts (token GitHub/GitLab avec scopes de lecture)
- Clé API IA (OpenAI ou Google Gemini selon l’implémentation)
- Optional : comptes/credentials pour les canaux de distribution (SMTP, Slack webhook, Telegram bot token, etc.)

## Installation rapide

Option 1 — Docker (recommandé)
1. Copier le fichier d’exemple d’environnement : cp .env.example .env
2. Éditer .env pour ajouter les tokens et la configuration.
3. Lancer : docker compose up --build -d

Option 2 — Local (Node)
1. Installer les dépendances : npm ci
2. Configurer les variables d’environnement (voir section suivante).
3. Lancer manuellement : npm start
4. Pour exécuter une seule collecte et génération (mode one-shot) : npm run run:once

## Configuration (variables d’environnement)

Exemple .env (résumé) :
GITHUB_TOKEN=ghp_xxx
GITHUB_ORG=my-org
REPO_LIST=repo-a,repo-b
AI_PROVIDER=openai           # openai | gemini
AI_API_KEY=sk-xxx
REPORT_SCHEDULE=0 18 * * *   # cron (UTC) pour rapport quotidien
EXPORT_FORMATS=pdf,docx,txt
NOTIFIERS=email,slack
SMTP_HOST=smtp.example.com
SMTP_USER=user@example.com
SMTP_PASS=secret
SLACK_WEBHOOK=https://hooks.slack.com/services/XXX/YYY/ZZZ
TELEGRAM_TOKEN=123456:ABC-DEF
DISCORD_WEBHOOK=https://discord.com/api/webhooks/...

Remarques :
- REPO_LIST peut être utilisé à la place de GITHUB_ORG pour cibler des dépôts précis.
- REPORT_SCHEDULE suit la syntaxe cron ; pour exécutions ponctuelles, utiliser la commande one-shot.
- AI_PROVIDER choisit le backend d’IA ; adaptez la configuration au fournisseur choisi.

## Utilisation

- Mode développement : npm run dev (watch + reload)
- Générer un rapport immédiatement : npm run report:now
- Exécuter en mode dry-run (ne pas envoyer, juste preview) : npm run report:dry
- Voir les logs : docker compose logs -f

## Templates et personnalisation

Les templates de rapport sont basés sur Markdown. Vous pouvez personnaliser :
- Sections (par auteur, par projet, par gravité)
- Ton du résumé (formel, concis, narratif) via option AI_TONE
- Filtrage (ex : ignore commits contenant [ci skip])

## Sécurité et bonnes pratiques

- Ne stockez jamais de clés en clair dans le dépôt : utilisez des secrets (GitHub secrets, Vault, etc.).
- Limitez le scope du token GitHub à lecture seulement.
- Surveillez la consommation d’API IA et mettez en place des quotas/alertes.

## Développement et contribution

Contributions bienvenues : issues, PRs, idées d’intégration (MS Teams, Mattermost, etc.).  
Processus :
1. Ouvrez une issue décrivant la demande ou le bug.
2. Fork -> branch(feature/...) -> commit -> PR -> review.
3. Respectez le style de code et ajoutez des tests pour les nouvelles fonctionnalités.

## Roadmap (exemples)
- Support complet de Gemini + streaming
- Intégration MS Teams, Jira, Confluence
- UI web pour visualiser/valider les rapports avant envoi
- Plugins analytiques (heatmap des fichiers modifiés, churn)

## Licence

MIT — voir le fichier LICENSE pour les détails.

## Contact

Pour questions ou intégrations particulières : ouvrir une issue ou contacter le mainteneur principal via le profil GitHub.

---

Merci d’utiliser CommitAutoRapporti — si vous voulez, je peux :
- Générer un fichier .env.example prêt à l’emploi,
- Proposer des templates Markdown pour les rapports (journalier / hebdo),
- Ajouter des exemples de commandes Docker Compose et GitHub Action pour scheduler l’exécution.
