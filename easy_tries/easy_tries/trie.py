import collections
class Trie(object):
    def __init__(self):
        """
        Initializing Default Trie class which is a defaultdict of type Trie
        """
        self.child=collections.defaultdict(Trie)
        self.isword =False


class Word_Dictionary(object):

    
    def __init__(self):
        """
        Initializing Data Structure
        """
        self.root=Trie()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        val=self.root
        for w in word:
            val=val.child[w]
        val.isword =True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. 
        :type word: str
        :rtype: bool
        """
        val=self.root
        return self.dfs(val,word)
        
    
    def dfs(self,curr,word):
        """
        Returns if the word is in the data structure. Has logic to find exact matches as well as regular expressions
        :type word: str
        :type curr: An instance of Trie Class
        :rtype: bool
        """
        if not word:
            if curr.isword:
                return True
            return False
        if word[0]=='.':
            return any(self.dfs(val,word[1:])  
                        for val in curr.child.values())
        else:
            if word[0] in curr.child.keys():
                return self.dfs(curr.child[word[0]],word[1:])
            else:
                return False
                
