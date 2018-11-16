# The correlation is not that high. Let's measure the disparate impact according to the EEOC rule
means_scores = df.groupby(['score_text_quant','race']).size().unstack()
means_scores = means_scores/means_scores.sum()
print(means_scores)
# compute disparte impact
AA_with_high_score_scores = means_scores.loc[1,'African-American']
C_with_high_score_scores = means_scores.loc[1,'Caucasian']