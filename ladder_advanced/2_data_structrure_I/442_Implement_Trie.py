'''Description
Implement a trie with insert, search, and startsWith methods.

 Notice
You may assume that all inputs are consist of lowercase letters a-z.
Example
insert("lintcode")
search("code")
>>> false
startsWith("lint")
>>> true
startsWith("linterror")
>>> false
insert("linterror")
search("lintcode)
>>> true
startsWith("linterror")
>>> true
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False

class Trie:
    
    def __init__(self):
        # do intialization if necessary
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        # write your code here
        if not word:
            return
        
        currNode = self.root
        for c in word:
            child = currNode.children.get(c)
            if not child:
                child = TrieNode()
                currNode.children[c] = child
            currNode = child
            
        currNode.isword = True
        

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        # write your code here
        if not word:
            return False
            
        currNode = self.root    
        for c in word:
            currNode = currNode.children.get(c)
            if not currNode:
                return False
                
        return currNode.isword

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        # write your code here
        if not prefix:
            return False
            
        currNode = self.root    
        for c in prefix:
            currNode = currNode.children.get(c)
            if not currNode:
                return False
                
        return True



'''Summary
算法武器：trie树

# Trie树的结构

class TrieNode:
  def __init__(self):
    # Initialize your data structure here.
    # 孩子集合，这个是一个字典，key为字符，value为孩子节点的引用
    self.childs = dict()
    # 标记是否是叶子节点/是否是单词结尾
    self.isWord = False

class Trie:
  def __init__(self):
    self.root = TrieNode()

  # @param {string} word
  # @return {void}
  # Inserts a word into the trie.
  # 插入单词到trie树中
  def insert(self, word):
    curNode = self.root
    # 遍历单词中的每一个字符
    for letter in word:
      # 取出当前节点curNode的孩子列表，查看单词中该字符是否在trie树curNode节点的列表中    
      child = curNode.childs.get(letter)
      # 如果不在，那么构建trie树curNode节点，将该节点加入到curNode节点的孩子列表
      # key为字符，value为trie curNode节点的引用
      if child is None:
        child = TrieNode()
        curNode.childs[letter] = child
      # 将curNode节点指向child节点，就是将当前游标指针下移
      curNode = child
    # 当for循环退出时，curNode指向单词的最后一个trie Node  
    # 将单词末尾的Trie Node置位：isWord = True  
    curNode.isWord = True

  # @param {string} word
  # @return {boolean}
  # Returns if the word is in the trie.
  # 在Trie树种查找单词
  def search(self, word):
    curNode = self.root
    # 扫描单词中的每个字符，一次在trie树中搜索
    for letter in word:
      curNode = curNode.childs.get(letter)
      if curNode is None:
        # 如果单词中的当前字符不在trie数当前节点的孩子集合中，则代表该单词不在trie树中，返回False  
        return False
    # 如果单词中的所有字符都在trie树中，那么最后判断单词最后一位的trie node是否是单词isWord是否为True
    return curNode.isWord

  # @param {string} prefix
  # @return {boolean}
  # Returns if there is any word in the trie
  # that starts with the given prefix.
  # 在trie树种搜索是否从在前缀，这个搜索和搜单词几乎一样，就是不用在末尾判断是否trie node的单词布尔变量是否为True
  def startsWith(self, prefix):
    node = self.root
    for letter in prefix:
      node = node.childs.get(letter)
      if node is None:
        return False
    return True
'''
