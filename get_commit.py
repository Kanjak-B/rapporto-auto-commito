# Script to get day commits and generate a professional report

from git import Repo
from datetime import datetime
import locale

# Try to set locale to French for date formatting
try:
    locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_TIME, 'fr_FR')
    except locale.Error:
        pass # Fallback to default if French locale not available

def generate_report():
    repo_path = "/home/kanjak/Bureau/INT/Projects/rapporto-auto-commito"
    repo = Repo(repo_path)
    
    # Get all commits reachable from HEAD
    commits = list(repo.iter_commits())
    
    today = datetime.now().date()
    todays_commits = [c for c in commits if c.committed_datetime.date() == today]
    
    # Format date nicely (e.g., "11 décembre 2025")
    date_str = today.strftime("%d %B %Y")
    
    # Header
    print(f"# Rapport d'Avancement Quotidien")
    print(f"**Date** : {date_str}")
    print(f"**Projet** : rapporto-auto-commito")
    print("")
    
    # Summary
    count = len(todays_commits)
    print(f"## Synthèse")
    if count == 0:
        print("Aucune intervention technique n'a été réalisée ce jour.")
    else:
        intervention_word = "intervention" if count == 1 else "interventions"
        print(f"L'équipe technique a réalisé **{count}** {intervention_word} aujourd'hui.")
    print("")
    
    # Details
    if todays_commits:
        print(f"## Détail des Réalisations")
        print("Voici la liste des fonctionnalités et correctifs déployés ce jour :")
        print("")
        
        for commit in todays_commits:
            message = commit.message.strip()
            # Capitalize first letter
            if message:
                message = message[0].upper() + message[1:]
            
            print(f"*   {message}")
        
        print("")
        print("Restant à votre disposition pour tout complément d'information.")
        print("")
        print("Cordialement,")
        print("L'équipe de Développement")

if __name__ == "__main__":
    generate_report()
