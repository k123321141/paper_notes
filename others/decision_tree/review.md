It's an overview through many classic paper about Decision Tree algorithm.

## Basic issues

It's an NP-complete problem to construct an optimal binary decision tree.

There is two major phase about DT, the growth phase and the pruning phase.</br>

The growth phase iteratively split data with test question, until the leave contain only one class or error rate of leave node is under an specified threshold.(pre-pruning)</br>
The pruning phase merge some similar node to prevent overfitting and keep the ability of model to generalize.</br>

### Splitting measure

Since how to construct an decision tree is NP-complete problem, how to split a node is important to algorithm.</br>
By spitting measure to evalute a split is a greedy strategy.</br>

![alt text](https://github.com/k123321141/paper_notes/blob/master/others/decision_tree/fig2.png)</br>


