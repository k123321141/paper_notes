It's an overview through many classic paper about Decision Tree algorithm.

## Basic issues

It's an NP-complete problem to construct an optimal binary decision tree.</br>

There is two major phase about DT, the growth phase and the pruning phase.</br>

The growth phase iteratively split data with test question, until the leave contain only one class or error rate of leave node is under an specified threshold.(pre-pruning)</br>

The pruning phase merge some similar node to prevent overfitting and keep the ability of model to generalize.</br>

### Splitting measure

Since how to construct an decision tree is NP-complete problem, how to split a node is important to algorithm.</br>
By spitting measure to evalute a split is a greedy strategy.</br>

![alt text](https://github.com/k123321141/paper_notes/blob/master/others/decision_tree/fig2.png)</br>

如果使用information gain, 得出的attributes會比較sparse, 容易被值域大的attribute給主導, extreme case : ID code。</br>


### Multivariate splits

相較於利用單一fearture做split，考慮多項feature做linear weight的條件可能更加準確。</br>
而nonlinear model的確強大，但是在decision tree裡面也容易造成overfitting。</br>
由於complexity隨著深度降低，僅在root node附近使用nonlinear是比較好的策略。</br>

### 附註資料 ensemble model

ref: http://www.cmlab.csie.ntu.edu.tw/~cyy/learning/tutorials/EnsembleLearning.pdf

一般來說，輸出結果只產生一個假說的學習演算法普遍都會遭遇三個嚴重的問題:統計問題、計算問題和代表性問題。然而，這些問題通常是可以透過整體學習的方法加以解決的。</br>
當學習演算法搜尋一個訓練資料(train data)數量過於龐大的假說空間時，就會產生所謂的統計問題。</br>
在這種情況下，由於可取得的資訓練料過多以致於可能會有數個不同的假說皆提供訓練資料數據上相當程度的準確度，但學習演算法卻又被強迫必須冒著風險從這些可能性極高的假說中挑選一個。</br>
於是，被選取的假說就具有某程度以上的偏頗，因此將導致可能無法準確地預測未來每一個新的資料點。所以，一種針對所有分類器所進行之簡單、平等的投票機制，將可有效的降低這種風險。</br>

計算問題常出現的時機，常常是因為在學習演算法不能保證能從假說空間裡找到一個最好的假說的時候。</br>
例如在神經網路(neural network)和決定樹演算法中，要尋找一個最符合(best fit)訓練資料數據的假說，從計算機計算能力的角度來評估，絕對是不可能實現的(intractable)，因此勢必要採用所謂的啟發式探索方法來達成。</br>
然而，有一些像坡度降下(gradient descent)的探索方法，又常會被卡在本地最小量(local minima)的地方，也就是說，很多啟發式探索方法，理論上是無法找到最好的假說。</br>
就像統計問題一樣，如果利用加權方式，將多種不同的本地最小量結合起來作為輸出，事實上是可以有效降低選擇錯誤而陷入本地最小量的危險。</br>

最後，當假說空間不包含任何近似真實函式 f 的好假說時，代表性問題就出現了。</br>
有時候，給予個別假說不同的權重，透過加總的效果所擴大的函式空間，是可以產生具有代表性的假說。</br>
換句話說，假若提供不同權重的投票方式給每一個假說，整體學習演算法是很有機會在一個沒有代表性的假說空間裡，找到一個非常準確且逼近真實函式f的近似值。

若學習演算法有統計問題時，我們就說這個方法具有高的"變異(variance)"。</br>
如果有計算問題的話，我們則描述它是一個有高的"計算量變異(computational variance)"。</br>
另外，若是學習演算法有代表性問題，我們即稱它具有高的"偏差 (bias)"。</br>
大致來說，多數的研究報告中證實了整體方法能降低學習演算法的偏差和變異。</br>



