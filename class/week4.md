
### 尚未分類

可以用來做index, similarity comparation or even generation.

###

## 以圖片作為例子</br>

### 圖片 SIFT

1. SIFT利用moving window選擇關鍵點的個數，取出local feature描述關鍵點的維度。</br>假設圖片取出1k個資料點各128維度。</br>

2. 對每一個關鍵點，利用k-means做分群，得到圖片的類別。</br>假設有N張圖片，共有1k個分群問題，每個分群問題要做128維度N筆資料的分群。</br>
由於N的大小，有可能採用hierarchy k-means。</br>
下圖顯示出hard quantum或是soft quantum。</br>![alt text](https://github.com/k123321141/paper_notes/blob/master/class/img1.png)

3. 最後就可以使用k-means分出來的群，代表不同的latent topic。

