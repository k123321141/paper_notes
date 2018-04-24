
## 目標

使用unsupervise learning找出在高維度空間的latent topic。

### 介紹

歷史發展<圖片來源:https://blog.csdn.net/pipisorry/article/details/42560693></br>
![alt text](https://github.com/k123321141/paper_notes/blob/master/class/img6.png)


### 用途

可以用來做index, similarity comparation or even generation.

###

## 以圖片作為例子</br>

### 圖片 SIFT

1. SIFT利用moving window選擇關鍵點的個數，取出local feature描述關鍵點的維度。</br>假設圖片取出1k個資料點各128維度。</br>

2. 對每一個關鍵點，利用k-means做分群，得到圖片的類別。</br>假設有N張圖片，共有1k個分群問題，每個分群問題要做128維度N筆資料的分群。</br>
由於N的大小，有可能採用hierarchy k-means。</br>
下圖顯示出hard quantum或是soft quantum。</br>![alt text](https://github.com/k123321141/paper_notes/blob/master/class/img1.png)

3. 最後就可以使用k-means分出來的群，代表不同的latent topic。

### Text latent

簡單的做法，利用term-by-document(inverted list)，挑出特定的term(word)就可以表示一個document。</br>配合使用交集就可以用來做retrieval。</br>
顯而易見的缺點是，不能好好處理同義字以及多義字。</br>

#### LSA

首先是對問題的觀察：每篇文章會出現的字的頻率，與該文章的主題有關。</br>

接下來是如何根據觀察，提出適合的模型。</br>![alt text](https://github.com/k123321141/paper_notes/blob/master/class/img2.png)</br>
利用SVD分解，column為term，意義上N的rank代表資料中有幾種topic，剩下分解的矩陣數值則對應各種關係。</br>

降維 要去除topic(term)的數量，可以考慮將係數較小的topic，設為零。</br>![alt text](https://github.com/k123321141/paper_notes/blob/master/class/img3.png)</br>
缺點在於這個模型並不是很好的利用頻率，考慮的微小差異的column會影響到rank，以及難以描述機率來做generate的應用。</br>

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















