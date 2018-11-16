means_recid = df.groupby(['two_year_recid','race']).size().unstack()
means_recid = means_recid/means_recid.sum()
print(means_recid)
# compute disparte impact
AA_with_high_score_recid = means_recid.loc[1,'African-American']
C_with_high_score_recid = means_recid.loc[1,'Caucasian']
percentage_diff_recid = 100*(AA_with_high_score_recid/C_with_high_score_recid -1)
print(percentage_diff_recid)