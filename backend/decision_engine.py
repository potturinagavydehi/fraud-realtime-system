def rule_score(tx):
    score = 0

    if tx["amount"] > 3000:
        score += 0.2

    if tx["velocity"] > 5:
        score += 0.3

    if tx["is_foreign"]:
        score += 0.3

    return min(score, 1.0)


def final_decision(ml_score, rule_score):
    final_score = 0.7 * ml_score + 0.3 * rule_score
    decision = "BLOCK" if final_score > 0.65 else "APPROVE"
    return final_score, decision