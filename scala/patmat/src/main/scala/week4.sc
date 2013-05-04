object week4 {

	import patmat.Huffman
  //val map = l.groupBy((elem: Char) => elem).mapValues((k: List[Char]) => k.length).toList
  //l.groupBy((elem: Char) => elem).mapValues((k: List[Char]) => k.length).toList
  //TestMap.map
  //map.mapValues((k: List[Char]) => k.length).toList
  val t = List()                                  //> t  : List[Nothing] = List()
  t++List(1)                                      //> res0: List[Int] = List(1)
  val t1 = Huffman.times(List('h','u','f','f','m','a','n'))
                                                  //> t1  : List[(Char, Int)] = List((n,1), (u,1), (a,1), (m,1), (h,1), (f,2))
  val t2 = Huffman.makeOrderedLeafList(t1)        //> t2  : List[patmat.Huffman.Leaf] = List(Leaf(n,1), Leaf(u,1), Leaf(a,1), Leaf
                                                  //| (m,1), Leaf(h,1), Leaf(f,2))
  
  val t3 = Huffman.combine(t2)                    //> t3  : List[patmat.Huffman.CodeTree] = List(Leaf(a,1), Leaf(m,1), Leaf(h,1), 
                                                  //| Fork(Leaf(n,1),Leaf(u,1),List(n, u),2), Leaf(f,2))
                                                  
  val t4 = Huffman.until(Huffman.singleton, Huffman.combine)(t2)
                                                  //> t4  : List[patmat.Huffman.CodeTree] = List(Fork(Fork(Leaf(h,1),Fork(Leaf(a,1
                                                  //| ),Leaf(m,1),List(a, m),2),List(h, a, m),3),Fork(Fork(Leaf(n,1),Leaf(u,1),Lis
                                                  //| t(n, u),2),Leaf(f,2),List(n, u, f),4),List(h, a, m, n, u, f),7))
  
  val a1 =  Huffman.times(Huffman.string2Chars("aaaaaaaabbbcdefgh"))
                                                  //> a1  : List[(Char, Int)] = List((e,1), (f,1), (g,1), (c,1), (h,1), (d,1), (b,
                                                  //| 3), (a,8))
  val a2 = Huffman.makeOrderedLeafList(a1)        //> a2  : List[patmat.Huffman.Leaf] = List(Leaf(e,1), Leaf(f,1), Leaf(g,1), Leaf
                                                  //| (c,1), Leaf(h,1), Leaf(d,1), Leaf(b,3), Leaf(a,8))
}