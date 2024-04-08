# Funcion reemplazo
def sustitucion_nulos(row):
    tournament = row['TOURNAMENT']
    winner_prize = row['WINNER_PRIZE']
    if pd.isnull(winner_prize) and any(t in tournament for t in tournament_means.key()):
        return tournament_means(next(t for t in tournament_means.key() if t in tournament))
    else:
        return winner_prize