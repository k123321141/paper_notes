
### RCNN

RCNN 總共分四個步驟做訓練，而且都是分開的。</br>
1. [selective search](#selective_search)，首先利用CV的方式切出候選區域。</br>
2. deep learning，利用 CNN+FCN 取出各ROI特徵並使用softmax分類。</br>
3. SVM，利用步驟2的network，將softmax前一層的輸出取出，另外訓練一個SVM做分類，對於類別樣本不平均問題，SVM表現更好。</br>
4. deep learning，bounding box regression，


>另一個相似的[Inverted List 倒排索引](#inverted_list)</br>


使用unsupervise learning找出在高維度空間的latent topic。

### 介紹

![Alt text][1]

latent sematic是高階抽象的類別，各種機器學習的目標都在專注在將低階的資訊，轉換成可閱讀的高階資訊。</br>
hidden latent sematic就是這些模型想要了解的。
透過為資料分類topic，像是Word2Vec、skip-thought模型，透過unsupervised learning理解個低階資訊之間的關係。(對比於ont-hot encoding)


### LSA

最初觀察，每篇文章會出現的詞彙頻率並不相同，其一定程度上的代表了這篇文章的類別。</br>
透過觀察低階的資訊(word)，推估高階資訊(topic)。</br>

簡單的做法，利用term-by-document</br>
row代表了每個文章中，特定詞彙出現的次數，而row-wise dot表示兩篇文章的相似度。</br>
顯而易見的缺點是，不能好好處理同義字以及多義字。</br>

>另一個相似的[Inverted List 倒排索引](#inverted_list)</br>


利用SVD分解</br>

![Alt text][2]</br>

<a href="https://www.codecogs.com/eqnedit.php?latex=X&space;\approx&space;U_t\Sigma_t&space;V_t\trps" target="_blank"><img src="https://latex.codecogs.com/gif.latex?X&space;\approx&space;U_t\Sigma_t&space;V_t\trps" title="X \approx U_t\Sigma_t V_t\trps" /></a></br>


意義上N的rank代表資料中有幾種topic，剩下分解的矩陣數值則對應各種關係。</br>
U column 為各個doc對應的topic的程度，V column為各個word對應的topic的程度，奇異值則代表topic間的比重。</br>
而一篇文章則是被分解：
1. word跟每個topic的係數，V</br>
2. 每個topic在資料間的比重，奇異值</br>
3. doc跟每個topic的係數轉換，U</br>

如此一來就可以透過unsupervised learning理解word之間的關係。</br>

> V表示word在各topic的係數，內積則能表示word在topic間的相似度。</br>
> U表示doc在各topic的係數，內積則能表示文章在topic的相似度。</br>
也可搜尋文章的相似度，這次則是利用U。</br>

降維</br>
奇異值表示了topic的比重程度，可以考慮將係數較小的topic，設為零。</br>
![alt text](https://github.com/k123321141/paper_notes/blob/master/class/img3.png)</br>
缺點在於這個模型並不是很好的利用頻率，考慮的微小差異的column會影響到rank，也就是說雜訊會影響SVD找到topic的能力，所以還原的差異很大。</br>
以及難以描述機率來做generate的應用。</br>

### Probabilistic Topic Models, pLSA

與LSA的觀察一樣，既然與字頻率與topic有關，那麼如果使用機率模型，則模型的產出應該要與觀察到的資料有max-likehood性質。</br>
各個topic出現每個字的機率不同。</br>
<a href="https://www.codecogs.com/eqnedit.php?latex=\\z_i&space;\in&space;Z,for&space;\&space;1\leq&space;i\leq&space;N&space;\\&space;d_i&space;\in&space;D,for&space;\&space;1\leq&space;i\leq&space;M&space;\\&space;w_i&space;\in&space;V,V&space;=&space;vocabulary" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\\z_i&space;\in&space;Z,for&space;\&space;1\leq&space;i\leq&space;N&space;\\&space;d_i&space;\in&space;D,for&space;\&space;1\leq&space;i\leq&space;M&space;\\&space;w_i&space;\in&space;V,V&space;=&space;vocabulary" title="\\z_i \in Z,for \ 1\leq i\leq N \\ d_i \in D,for \ 1\leq i\leq M \\ w_i \in V,V = vocabulary" /></a></br>
pLSA假設每篇文章只有一個topic。</br>
pLSA模型產生文章的流程：</br>

>1. 為了產生M篇文章，擲骰子選出M個topic，每篇文章都有對應的topic, z</br>
>2. 利用poisson distribution或是其他分佈選出文章的長度, N</br>
>3. 根據選出的z,擲N次骰子選出w</br>
![alt text][4]</br>

有了模型產生的流程就可以計算maximum likelihood，可是這種式子不好計算。</br>
透過符合某些統計特性，可以相當程度地表示likelihood，例如P(d,w)，表示P(d and w)。</br>
pLSA與LSA相同，希望透過unsupervised learning計算word與topic間的相似度，以及doc在topic間的相似度。</br>
假設d與z獨立:</br>
<a href="https://www.codecogs.com/eqnedit.php?latex=P(w|d)&space;=&space;\sum^Z&space;P(w&space;|&space;z_i)&space;P(z_i&space;|&space;d)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(w|d)&space;=&space;\sum^Z&space;P(w&space;|&space;z_i)&space;P(z_i&space;|&space;d)" title="P(w|d) = \sum^Z P(w | z_i) P(z_i | d)" /></a></br>
P(d,w) = P(d)P(w|d), 由於P(d)是未知的項，利用抽樣的訓練資料表示P(d)並且利用KL-divergence可以衡量訓練資料與模型的差異。</br>
Q(d,w)表示訓練資料裡w出現在d的頻率，藉此代表P(d,w)</br>
![alt text][5]</br>
![alt-text][7]</br>

最終objective function就會是兩個矩陣乘績，各項次的KL差異。</br>
![alt-text][8]</br>
利用EM algorithm 可以解上述式子。</br>

如此就可以利用P(w|z)以及P(z|d)表示相似度。</br>

基於</br>
<a href="https://www.codecogs.com/eqnedit.php?latex=P(w|d)&space;=&space;\sum^Z&space;P(w&space;|&space;z_i)&space;P(z_i&space;|&space;d)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(w|d)&space;=&space;\sum^Z&space;P(w&space;|&space;z_i)&space;P(z_i&space;|&space;d)" title="P(w|d) = \sum^Z P(w | z_i) P(z_i | d)" /></a></br>
其中的P(w|z)相當於topic空間中的basis，是維度為K-1的subspace，稱為simplex。<\br>
summation 機率合為1的關係，P(w|d)會落在各basis組成的simplex上。</br>
而KL-divergence則描述了實際上P(w|d)與complex的residual。(可以選用其他objective function)</br>
![alt-text][9]</br>


#### LSA 與 pLSA 的比較

LSA利用eigen value係數做降維，設定需要的topic量。</br>
pLSA則設定適合大小的topic k，衡量效能。</br>

### LDA 待補

![alt-text][10]</br>
相對於pLSA每個文章只用一個主題去描述組成文章d的w關係。</br>
LDA多了一個選擇P(w|c)的方式，描述了\theta是組成doc的topic成分，P(c|d)。</br>
而選擇doc中word的時候，並沒有單純使用P(w|c)，加入了一個我還不清楚概念Dirichlet-multinomial distributio</br>
透過讓doc由多種topic組合，選用word的方式更複雜了點。</br>


### 補充資料

<h2 id="selective_search">Selective Search<h2>
簡單的概念，維基有很簡單易懂的範例。</br>
https://zh.wikipedia.org/wiki/倒排索引</br>
透過直接標註word出現在哪些文章，然後有新的文章D出現時，對D所有出現過的word，查詢每個word出現在哪些文章過，取交集。

<h2 id="inverted_list">Inverted List</h2>
簡單的概念，維基有很簡單易懂的範例。</br>
https://zh.wikipedia.org/wiki/倒排索引</br>
透過直接標註word出現在哪些文章，然後有新的文章D出現時，對D所有出現過的word，查詢每個word出現在哪些文章過，取交集。









### 資料來源
https://blog.csdn.net/pipisorry/article/details/42560693</br>
https://cs.stanford.edu/~ppasupat/a9online/1140.html</br>
https://en.wikipedia.org/wiki/Dirichlet-multinomial_distribution</br>
http://www.inf.ed.ac.uk/teaching/courses/tnlp/2016/Merce.pdf</br>
https://blog.csdn.net/lmm6895071/article/details/74999129</br>

[1]: https://github.com/k123321141/paper_notes/blob/master/class/img6.png
[2]: https://github.com/k123321141/paper_notes/blob/master/class/img2.png
[4]: https://github.com/k123321141/paper_notes/blob/master/class/img4.png
[5]: https://github.com/k123321141/paper_notes/blob/master/class/img5.png
[7]: https://github.com/k123321141/paper_notes/blob/master/class/img7.png
[8]: https://github.com/k123321141/paper_notes/blob/master/class/img8.png
[9]: https://github.com/k123321141/paper_notes/blob/master/class/img9.png
[10]: https://github.com/k123321141/paper_notes/blob/master/class/img10.png
