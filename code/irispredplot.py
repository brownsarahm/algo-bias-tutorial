for mu,cov,color,c in zip(qda.means_,qda.covariance_,["Reds","Blues","Greens"],['r','b','g']):
    x = np.random.multivariate_normal(mu,cov,size=1000)
    ax = sns.kdeplot(x[:,0], x[:,1],
                 cmap=color, shade=True, shade_lowest=False)
    plt.plot(x[:100,0],x[:100,1],c+'.')
plt.legend(qda.classes_)