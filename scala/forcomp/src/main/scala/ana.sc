object ana {


  import forcomp.Anagrams
  println("Welcome to the Scala worksheet")       //> Welcome to the Scala worksheet
  val s: String = "Test"                          //> s  : String = Test
  s.map(c => c.toLower).groupBy(c => c).mapValues(s => s.length).toList
                                                  //> res0: List[(Char, Int)] = List((e,1), (t,2), (s,1))
  type Word = String
  type Sentence = List[Word]

  /**
   * `Occurrences` is a `List` of pairs of characters and positive integers saying
   *  how often the character appears.
   *  This list is sorted alphabetically w.r.t. to the character in each pair.
   *  All characters in the occurrence list are lowercase.
   *
   *  Any list of pairs of lowercase characters and their frequency which is not sorted
   *  is **not** an occurrence list.
   *
   *  Note: If the frequency of some character is zero, then that character should not be
   *  in the list.
   */
  type Occurrences = List[(Char, Int)]

  def wordOccurrences(w: Word): Occurrences = { w.map(c => c.toLower).groupBy(c => c).mapValues(s => s.length).toList.sortBy((elem: (Char, Int)) => elem._1) }
                                                  //> wordOccurrences: (w: ana.Word)ana.Occurrences
  val sentence = List("abcd", "ae")               //> sentence  : List[String] = List(abcd, ae)
  sentence.apply(0)                               //> res1: String = abcd

  def sentenceToString(s: Sentence): String = s match {
    case Nil => ""
    case y :: ys => y + sentenceToString(ys)
  }                                               //> sentenceToString: (s: ana.Sentence)String
  def sentenceOccurrences(s: Sentence): Occurrences = s match {
    case Nil => List()
    case y :: ys => wordOccurrences(y) ++ sentenceOccurrences(ys)
  }                                               //> sentenceOccurrences: (s: ana.Sentence)ana.Occurrences

  //sentenceOccurrences(sentence)
  //lazy val dictionaryByOccurrences: Map[Occurrences, List[Word]] = {

  //}
  def reduceOccurences(value: List[(Occurrences, Word)]): List[Word] = value match {
    case Nil => List()
    case y :: ys => y._2 :: reduceOccurences(ys)

  }                                               //> reduceOccurences: (value: List[(ana.Occurrences, ana.Word)])List[ana.Word]
  val t1 = List(('a', 2), ('b', 3))               //> t1  : List[(Char, Int)] = List((a,2), (b,3))
  //forcomp.Anagrams.dictionary.map((w: Word) => (wordOccurrences(w), w)).groupBy((elem: (Occurrences, Word)) => elem._1).mapValues(reduceOccurences)

  
	def generate(p: (Char, Int)): Seq[(Char, Int)] = {
		for {
    	integer <- 1 to p._2
  	} yield (p._1, integer)
	}                                         //> generate: (p: (Char, Int))Seq[(Char, Int)]
	
	def generatePairComb(list: List[(Char, Int)]): List[List[(Char, Int)]] = list match {
			case Nil => List(List())
			case y :: ys => generate(list.head).toList :: generatePairComb(list.tail)
	}                                         //> generatePairComb: (list: List[(Char, Int)])List[List[(Char, Int)]]
	
	def generateSlices(list: List[(Char, Int)]): Seq[List[(Char, Int)]] = {
		for {
			len <- 0 to list.length
		} yield list.slice(0, len)
	}                                         //> generateSlices: (list: List[(Char, Int)])Seq[List[(Char, Int)]]
	
	val t2 = generatePairComb(List(('a', 2), ('b', 2), ('c',3)))
                                                  //> t2  : List[List[(Char, Int)]] = List(List((a,1), (a,2)), List((b,1), (b,2))
                                                  //| , List((c,1), (c,2), (c,3)), List())
	
	val t3 = t2.flatten                       //> t3  : List[(Char, Int)] = List((a,1), (a,2), (b,1), (b,2), (c,1), (c,2), (c
                                                  //| ,3))
	
	
	/*def generateLists(l1: List[(Char, Int)], l2: List[List[(Char, Int)]]): List[List[(Char, Int)]] = {
		for {
			s1 <- generateSlices(l1).toList
		} yield s1 ++ l2
	}*/
	def generateLists(list: List[List[(Char, Int)]]): List[List[(Char, Int)]] = {
		
		List()
	}                                         //> generateLists: (list: List[List[(Char, Int)]])List[List[(Char, Int)]]
  //generateLists(List(('a',1), ('a',2)), List(('c',1), ('c',2), ('c',3)))
  
  //t2.fold(List[List[(Char, Int)]]())(generateLists)
    
    generateSlices(List(('c',1), ('c',2), ('c',3)))
                                                  //> res2: Seq[List[(Char, Int)]] = Vector(List(), List((c,1)), List((c,1), (c,2
                                                  //| )), List((c,1), (c,2), (c,3)))
	
	//List(('a', 2), ('b', 2), ('c',3)).combinations(0).toList
	
  //generateLists(List(('a', 2), ('b', 2)))
  
	//combinationsHelper(List(('a', 2), ('b', 2), ('c',3)))
}