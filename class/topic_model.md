
## 目標

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

如此一來就可以透過unsupervised learning理解word之間的關係，V表示word在各topic的係數，內積則能表示相似度。</br>
也可搜尋文章的相似度，這次則是利用U。</br>

降維</br>
奇異值表示了topic的比重程度，可以考慮將係數較小的topic，設為零。</br>
![alt text](https://github.com/k123321141/paper_notes/blob/master/class/img3.png)</br>
缺點在於這個模型並不是很好的利用頻率，考慮的微小差異的column會影響到rank，也就是說雜訊會影響SVD找到topic的能力，所以還原的差異很大。</br>
以及難以描述機率來做generate的應用。</br>

#### Probabilistic Topic Models

與LSA的觀察一樣，既然與字頻率與topic有關，那麼如果使用機率模型，則模型的產出應該要與觀察到的資料有max-likehood性質。</br>
使用貝氏網路來描述一個模型。</br>

#### pLSA

![alt text](https://github.com/k123321141/paper_notes/blob/master/class/img4.png)</br>
document每一個字都會照圖中選出，d種topic，N種word，M個document。</br>

![alt text](https://github.com/k123321141/paper_notes/blob/master/class/img5.png)</br>
既然summation P(z|d) = 1 , 則P(w|d)相當於以P(w|z)為基底，且係數總和為1的線性組合。</br>
以上條件讓P(w|d)落在P(w|z)基底組成的subspace，如果共有N種word，則P(w|d)會是維度為N-1的subspace，稱為simplex。</br>

那麼最後使用Minimize KL divergence作為objective function。</br>
演算法請參考EM algorithm解法。</br>

#### LSA 與 pLSA 的比較

LSA利用eigen value係數做降維，設定需要的topic量。</br>
pLSA則設定適合大小的topic k，衡量效能。</br>




<h2 id="inverted_list">Inverted List</h2>
簡單的概念，維基有很簡單易懂的範例。</br>
https://zh.wikipedia.org/wiki/倒排索引</br>
透過直接標註word出現在哪些文章，然後有新的文章D出現時，對D所有出現過的word，查詢每個word出現在哪些文章過，取交集。









### 資料來源
歷史發展<圖片來源:https://blog.csdn.net/pipisorry/article/details/42560693></br>
https://cs.stanford.edu/~ppasupat/a9online/1140.html</br>

[1]: https://github.com/k123321141/paper_notes/blob/master/class/img6.png
[2]: https://github.com/k123321141/paper_notes/blob/master/class/img2.png
