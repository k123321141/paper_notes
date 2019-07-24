### A formal study of information retrieval heuristics.
##### Fang, H., Tao, T., Zhai, C.: A formal study of information retrieval heuristics. In: Proceedings of the 27th annual international ACM SIGIR conference on Research and development in information retrieval. pp. 49–56. ACM (2004)

### Abstract
*Empirical studies of information retrieval methods show that good retrieval performance is closely related to the use of various retrieval heuristics, such as TF-IDF weighting. One basic research question is thus what exactly are these “nec- essary” heuristics that seem to cause good retrieval perfor- mance. In this paper, we present a formal study of retrieval heuristics. We formally define a set of basic desirable con- straints that any reasonable retrieval function should satisfy, and check these constraints on a variety of representative re- trieval functions. We find that none of these retrieval func- tions satisfies all the constraints unconditionally. Empirical results show that when a constraint is not satisfied, it often indicates non-optimality of the method, and when a con- straint is satisfied only for a certain range of parameter val- ues, its performance tends to be poor when the parameter is out of the range. In general, we find that the empiri- cal performance of a retrieval formula is tightly related to how well it satisfies these constraints. Thus the proposed constraints provide a good explanation of many empirical observations and make it possible to evaluate any existing or new retrieval formula analytically.
*
### Goal
Claim that IR methods **should**  hold the 6 heuristic to perform well.
### Strategy
訂出六個符合直覺的 IR heuristic function 然後探討三個方法
- Pivoted Normalization Method
- Okapi Method (BM25)
- Dirichlet Prior Method

在控制hyper-parameter的條件下，檢查是否符合 heuristic，並且檢視其performance。
其中需要注意的是，裡面說明了Okapia遇到負數 *IDF* 的問題。
當 *IDF* 是負值時，違反了幾項heuristic，造成即便增加了幾個match word其score仍比較低。
這會在query出現非常高DF的時候，所以在長query時表現比較差，在實驗結果也證明了這項觀察。
作者透過替換成 Pivoted normalization formula 裡面的 IDF term證明。


