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




補充：</br>
基尼不純度指標[編輯]
在CART算法中, 基尼不純度表示一個隨機選中的樣本在子集中被分錯的可能性。基尼不純度為這個樣本被選中的機率乘以它被分錯的機率。當一個節點中所有樣本都是一個類時，基尼不純度為零。
假設y的可能取值為{1, 2, ..., m},令fi是樣本被賦予i的機率，則基尼指數可以通過如下計算：
ID3, C4.5 和 C5.0 決策樹的生成使用信息增益。信息增益 是基於資訊理論中 信息熵的理論.


訓練一棵最優的決策樹是一個完全NP問題。[9][10] 因此, 實際應用時決策樹的訓練採用啟發式搜索算法例如 貪心算法 來達到局部最優。這樣的算法沒辦法得到最優的決策樹。
決策樹創建的過度複雜會導致無法很好的預測訓練集之外的數據。這稱作過擬合.[11] 剪枝機制可以避免這種問題。
有些問題決策樹沒辦法很好的解決,例如 異或問題。解決這種問題的時候，決策樹會變得過大。 要解決這種問題，只能改變問題的領域[12] 或者使用其他更為耗時的學習算法 (例如統計關係學習 或者 歸納邏輯編程).
對那些有類別型屬性的數據, 信息增益 會有一定的偏置

　　優點：

　　1)　可以生成可以理解的規則；

　　2)　計算量相對來說不是很大；

　　3) 可以處理連續和種類欄位；

　　4) 決策樹可以清晰的顯示哪些欄位比較重要。

　　缺點：

　　1) 對連續性的欄位比較難預測；

　　2) 對有時間順序的數據，需要很多預處理的工作；

　　3) 當類別太多時，錯誤可能就會增加的比較快；

　　4) 一般的演算法分類的時候，只是根據一個欄位來分類。

    5)在处理特征关联性比较强的数据时表现得不是太
### split measure 
我認為最一開始都是為了找出(0.,0.5)這樣的資料 比(0.9, 0.1)更糟的表示法

### gini index

gini index 源自機率的描述，假設共有k個類別，而在Node_m時P_k為類別k在Node_m的比例。</br>
則在Node_m判斷為k類別且k類別判斷錯誤的機率為P_k * (1-P_k)</br>
加總每個類別的錯誤即是gini index

Among decision support tools, decision trees (and influence diagrams) have several advantages. Decision trees:

Are simple to understand and interpret. People are able to understand decision tree models after a brief explanation
Have value even with little hard data. Important insights can be generated based on experts describing a situation (its alternatives, probabilities, and costs) and their preferences for outcomes.
Allow the addition of new possible scenarios.
Help determine worst, best and expected values for different scenarios.
Use a white box model. If a given result is provided by a model.
Can be combined with other decision techniques.
Disadvantages of decision trees:

They are unstable, meaning that a small change in the data can lead to a large change in the structure of the optimal decision tree.
They are often relatively inaccurate. Many other predictors perform better with similar data. This can be remedied by replacing a single decision tree with a random forest of decision trees, but a random forest is not as easy to interpret as a single decision tree.
For data including categorical variables with different number of levels, information gain in decision trees is biased in favor of those attributes with more levels.[6]
Calculations can get very complex, particularly if many values are uncertain and/or if many outcomes are linked.

### drawback conclusion
分類效能不夠好
缺乏高維度線性或非線性轉換
難以理解的線性關係(需要從多層的condition找出)
information gain 容易受到含有大量數值的屬性影響，例如信用卡號</br>
卡號這個屬性可以直接將樹切到leaf，所以information gain會首先取用這個屬性。</br>

Information gain ratio is sometimes used instead. This biases the decision tree against considering attributes with a large number of distinct values. However, attributes with very low information values then appeared to receive an unfair advantage.
相對於每個屬性做normalize，對於沒有夾帶太多資訊的屬性，會過份重視。
no online, overfit
忽略了數據之間的相關性(線性或非線性關係)；

對於那些各類別樣本數量不一致的數據，在決策樹當中,信息增益的結果偏向於那些具有更多數值的特徵（只要是使用了信息增益，都有這個缺點，如RF）


原文網址：https://kknews.cc/zh-tw/tech/o8jo4q.html

最一開始DT的假設沒有考慮的離散數值的差異，像是用每一攝氏溫度離散處理，當切分體溫38度，但是在38度附近的分佈可能有許多雜訊是介於有發燒徵狀，或是其實沒有。而另一種非連續數值像是有糖尿病的患者與沒有糖尿病的樣本之間，介於輕微心臟病或是沒有心臟病的雜訊就相對小，DT處理體溫這種連續數值就算是比較難以處理的問題。
