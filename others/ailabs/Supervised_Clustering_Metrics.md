# Supervised Clustering Metrics

最近工作上需要對新聞文本做unsupervised clustering，標注了幾天的資料量以後，可以開始衡量各個方法的好壞了，所以需要做一下研究metric的行為。
所以呢，幹，來吧，先從幾個sklearn上有的開始。

**NOTE**：只討論hard cluster，一個sample只分到一個cluster label


---


## Candidate metrics

- [Mutual Info](#mutual-info-score)
- [Normalized Mutual Info](#normalized-mutual-info)
- [Adjusted Mutual Info](#adjusted-mutual-info)
- [Rand index](#rand-index)
- [Adjusted Rand index](#adjusted-rand-index)
- [Fowlkes-Mallows scores](#fowlkes-mallows-scores)
- [Homogeneity](#homogeneity)
- [Completeness](#completeness)
- [V-measure](#v-measure)


---


### Mutual Info score

先從 [mutual information](https://zh.wikipedia.org/wiki/互信息) 開始吧。其實只是MI的discrete format而已。
白話文是，當知道了X的資訊了以後，揭露了多少有關Y的資訊。

$I(X;Y)=\int_Y\int_Xp(x,y)log(\frac{p(x,y)}{(p(x)p(y)})dxdy$

當X跟Y相互獨立的時候，$p(x,y)=p(x)p(y)$

$I(X;Y)=\int_Y\int_Xp(x,y)log(1)dxdy=0$

應用在cluster label的物理意義是「兩兩比對，cluster獨立的程度」。
cluster的離散表示如下：


$p(x,y)=\frac{\mid U_i \cap V_j\mid}{N}, p(x)=\frac{\mid U_i \mid}{N}, p(y)=\frac{\mid V_j \mid}{N}$




$MI(U,V)=\sum_{i=1}^{|U|} \sum_{j=1}^{|V|} \frac{|U_i\cap V_j|}{N}
\log\frac{N|U_i \cap V_j|}{|U_i||V_j|}$

所以當cluster都聚類不同群的時候，其相當於獨立分布，那麼分數就會很低。
這會回傳一個非負值。

---

### Normalized Mutual Info

當cluster數量增加的時候，MI也會上升。

利用entropy(U)跟entropy(V)是MI的upper bound

定義要使用的average_method去normalizate MI

回傳一個0-1的值

---

### Adjusted Mutual Info

這數學很殘念的我看不懂。
考慮了random的部分，除了normalize以外，還減去了期望值。

$H(X)=entropy(X)$
$AMI(U,V)=\frac{MI(U,V)-E\{MI(U,V)\}}{max\{H(U),H(V)\}-E\{MI(U,V)\}}$



---

### Rand index

做法是，每次從資料裡取2個資料點出來，共有四種可能：
1. 2個被U都是分到同一群，也被V分到同一群。TP
2. 2個被U都是分到不同群，也被V分到不同群。TN
3. 2個在U是同一群，在V則否。FP
4. 2個在U是不同群，在V則被分到同一群。FN

$RI=\frac{TP+TN}{TP+FP+TN+FN}$

而RI的分母其實是$\binom{N}{2}$

所以就變成了

$RI=\frac{TP+TN}{\binom{N}{2}}$

這會回傳一個0-1的值

---

### Adjusted Rand index

RI並沒有確保在random permutation下，數值接近0。
於是出現了用期望值做normalize的版本。

$\text{ARI} = \frac{\text{RI} - E[\text{RI}]}{\max(\text{RI}) - E[\text{RI}]}$

這邊可以注意一下，所謂$E[\text{RI}]$應該是根據不同的演算法會有不同的期望值算法。
sklearn應該是採用最簡單的對label做random permutation，所以k不變。

如果pred K小於true K，則ARI有可能會出現負值。


---

### Fowlkes-Mallows scores

待補。

$\text{FMI} = \frac{\text{TP}}{\sqrt{(\text{TP} + \text{FP}) (\text{TP} + \text{FN})}}$

這邊節錄了一下sklearn的結論：
```
Random(uniform) label assignments have a FMI score close to 0.0 for any value of n_clusters and n_samples (which is not the case for raw Mutual Information or the V-measure for instance).

```

---

### Homogeneity

Homogeneity定義：
pred cluster裡面所有的sample都是同一個true_label


Homogeneity score:
根據pred_label統計每個cluster，符合Homogeneity的程度。

物理意義是，切出來的cluster裡面的precision高不高，是否每個cluster的確都是同一個true_label。
如果追求 Homogeneity score會傾向切出很多破碎、很小而很純的cluster。

詳細算法待補。


---

### Completeness

Completeness：
true cluster裡面所有的sample都是同一個pred_label


Completeness score:
根據true_label統計每個cluster，符合Completeness的程度。

物理意義是與Homogeneity是相反的。
如果追求 Completeness score 會傾向切出很大但是主題分界很籠統的cluster。

---

### V-measure


$v = \frac{(1 + \beta) \times \text{homogeneity} \times \text{completeness}}{(\beta \times \text{homogeneity} + \text{completeness})}$

這有點像F-score，利用$\beta$調整 Homogeneity 跟 Completeness。



---


