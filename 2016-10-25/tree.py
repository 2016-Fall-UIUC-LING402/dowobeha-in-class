#!/usr/bin/python3

class Tree:
	
	def __init__(self, l, c):
		self.label = l
		self.children = c
	
	def __str__(self):
		if len(self.children)==0:
			return self.label
		else:
			s  = "[ "
			s += self.label + "(" + str(self.count("the")) + ")" + " "
			for child in self.children:
				s += str(child) + " "
			s += "]"
			return s

	def count(self, label):
		
		if self.label==label:
			n = 1
		else:
			n = 0
			
		for child in self.children:
			n += child.count(label)
		
		return n


def sample_tree():
        the1 = Tree("the", [])
        man = Tree("man", [])
        walked = Tree("walked", [])
        the2 = Tree("the", [])
        dog = Tree("dogs", [])
        thru = Tree("through", [])
        the3 = Tree("the", [])
        park = Tree("park", [])
        
        dt1 = Tree("DT", [the1])
        nn1 = Tree("NN", [man])
        vb = Tree("VBD", [walked])
        dt2 = Tree("DT", [the2])
        nns = Tree("NNS", [dog])
        p = Tree("P", [thru])
        dt3 = Tree("DT", [the3])
        nn2 = Tree("NN", [park])
        
        np1 = Tree("NP", [dt1, nn1])
        np2 = Tree("NP", [dt2, nns])
        np3 = Tree("NP", [dt3, nn2])
        pp = Tree("PP", [p, np3])
        vp = Tree("VP", [vb, np2, pp])
        
        s = Tree("S", [np1, vp])

        return s

if __name__ == '__main__':
        s = sample_tree()
        print(s)

