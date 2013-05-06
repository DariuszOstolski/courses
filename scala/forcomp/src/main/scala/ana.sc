object ana {
	
	import forcomp.Anagrams
  println("Welcome to the Scala worksheet")
  val s:  String = "Test"
  s.map(c => c.toLower).groupBy(c => c).mapValues( s => s.length).toList
  type Word = String
  type Sentence = List[Word]

  /** `Occurrences` is a `List` of pairs of characters and positive integers saying
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
  
  def wordOccurrences(w: Word): Occurrences = {  w.map(c => c.toLower).groupBy(c => c).mapValues( s => s.length).toList.sortBy(( elem: (Char, Int) )  => elem._1) }
  val sentence = List("abcd", "ae")
  sentence.apply(0)
  
  def sentenceToString(s: Sentence): String = s match {
  	case Nil =>  ""
  	case y::ys => y+sentenceToString(ys)
  }
  def sentenceOccurrences(s: Sentence): Occurrences = s match {
  	case Nil => List()
  	case y::ys => wordOccurrences(y) ++ sentenceOccurrences(ys)
  }
  //sentenceOccurrences(sentence)
  //lazy val dictionaryByOccurrences: Map[Occurrences, List[Word]] = {
  	
  //}
  def reduceOccurences(value: List[(Occurrences, Word)]): List[Word] = value match {
  	case Nil => List()
  	case y::ys => y._2 :: reduceOccurences(ys)
  	
  }
  //forcomp.Anagrams.dictionary.map((w: Word) => (wordOccurrences(w), w)).groupBy((elem: (Occurrences, Word)) => elem._1).mapValues(reduceOccurences)
  
  	def combinationsHelper(occur:  List[(Char, Int)]): Set[List[(Char, Int)]] = {
  			if(occur.isEmpty)
  		 		Set(List[(Char, Int)]())
  		 	else {
  		 		val prev = combinationsHelper(occur.tail)
  		 		for {
  		 			p <- prev
  		 			char <- 'a' until occur.head._1
  		 			int <- 1 until occur.head._2
  		 		} yield prev
  	 		}
  		}
  
  def combination(occurrences: Occurrences): List[Occurrences] = {
  		combinationsHelper(occurrences).toList
  }
  
  def compare(elem1: List[(Char, Int)], elem2: List[(Char, Int)]) = (elem1.length < elem2.length)
  combinationsHelper(List(('a', 2), ('b', 2), ('c',3))).toList.sortWith(compare)
}