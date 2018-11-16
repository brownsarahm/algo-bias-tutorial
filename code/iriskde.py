f, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect("equal")
setosa = iris_df[iris_df['species']=='setosa']
virginica= iris_df[iris_df['species']=='virginica']
versicolor = iris_df[iris_df['species']=='versicolor']

# Draw the two density plots
ax = sns.kdeplot(setosa['petal width (cm)'], setosa['petal length (cm)'],
                 cmap="Reds", shade=True, shade_lowest=False)
ax = sns.kdeplot(virginica['petal width (cm)'], virginica['petal length (cm)'],
                 cmap="Blues", shade=True, shade_lowest=False)
ax = sns.kdeplot(versicolor['petal width (cm)'], versicolor['petal length (cm)'],
                 cmap="Greens", shade=True, shade_lowest=False)

# Add labels to the plot
red = sns.color_palette("Reds")[-2]
blue = sns.color_palette("Blues")[-2]
ax.text(2.5, 8.2, "virginica", size=16, color=blue)
ax.text(3.8, 4.5, "setosa", size=16, color=red)