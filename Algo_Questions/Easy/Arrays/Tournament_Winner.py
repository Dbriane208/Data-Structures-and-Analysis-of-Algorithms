# time O(n) | space O(k)
def tournamentWinner(competions, results):
    currentBestTeam = ""
    scores = {currentBestTeam:0}
    Home_team_won = 1

    for idx, competion  in enumerate(competions):

        result = results[idx]
        awayTeam, homeTeam = competion

        winningTeam = homeTeam if result == Home_team_won else awayTeam

        updateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam

        return currentBestTeam    

def updateScores(team,points,scores):
    if team not in  scores:
        scores[team] = 0

        scores[team] += points       


