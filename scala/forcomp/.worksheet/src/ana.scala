object ana {

  import forcomp.Anagrams;import org.scalaide.worksheet.runtime.library.WorksheetSupport._; def main(args: Array[String])=$execute{;$skip(83); 
  println("Welcome to the Scala worksheet");$skip(25); 
  val s: String = "Test";System.out.println("""s  : String = """ + $show(s ));$skip(72); val res$0 = 
  s.map(c => c.toLower).groupBy(c => c).mapValues(s => s.length).toList
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
  type Occurrences = List[(Char, Int)];System.out.println("""res0: List[(Char, Int)] = """ + $show(res$0));$skip(766); 

  def wordOccurrences(w: Word): Occurrences = { w.map(c => c.toLower).groupBy(c => c).mapValues(s => s.length).toList.sortBy((elem: (Char, Int)) => elem._1) };System.out.println("""wordOccurrences: (w: ana.Word)ana.Occurrences""");$skip(36); 
  val sentence = List("abcd", "ae");System.out.println("""sentence  : List[String] = """ + $show(sentence ));$skip(20); val res$1 = 
  sentence.apply(0);System.out.println("""res1: String = """ + $show(res$1));$skip(125); 

  def sentenceToString(s: Sentence): String = s match {
    case Nil => ""
    case y :: ys => y + sentenceToString(ys)
  };System.out.println("""sentenceToString: (s: ana.Sentence)String""");$skip(157); 
  def sentenceOccurrences(s: Sentence): Occurrences = s match {
    case Nil => List()
    case y :: ys => wordOccurrences(y) ++ sentenceOccurrences(ys)
  };System.out.println("""sentenceOccurrences: (s: ana.Sentence)ana.Occurrences""");$skip(274); 
  //sentenceOccurrences(sentence)
  //lazy val dictionaryByOccurrences: Map[Occurrences, List[Word]] = {

  //}
  def reduceOccurences(value: List[(Occurrences, Word)]): List[Word] = value match {
    case Nil => List()
    case y :: ys => y._2 :: reduceOccurences(ys)

  };System.out.println("""reduceOccurences: (value: List[(ana.Occurrences, ana.Word)])List[ana.Word]""");$skip(36); 
  val t1 = List(('a', 2), ('b', 3));System.out.println("""t1  : List[(Char, Int)] = """ + $show(t1 ));$skip(270); 
  //forcomp.Anagrams.dictionary.map((w: Word) => (wordOccurrences(w), w)).groupBy((elem: (Occurrences, Word)) => elem._1).mapValues(reduceOccurences)

  
	def generate(p: (Char, Int)): Seq[(Char, Int)] = {
		for {
    	integer <- 1 to p._2
  	} yield (p._1, integer)
	};System.out.println("""generate: (p: (Char, Int))Seq[(Char, Int)]""");$skip(197); 
	
	def generatePairComb(list: List[(Char, Int)]): List[List[(Char, Int)]] = list match {
			case Nil => List(List())
			case y :: ys => generate(list.head).toList :: generatePairComb(list.tail)
	};System.out.println("""generatePairComb: (list: List[(Char, Int)])List[List[(Char, Int)]]""");$skip(142); 
	
	def generateSlices(list: List[(Char, Int)]): Seq[List[(Char, Int)]] = {
		for {
			len <- 0 to list.length
		} yield list.slice(0, len)
	};System.out.println("""generateSlices: (list: List[(Char, Int)])Seq[List[(Char, Int)]]""");$skip(64); 
	
	val t2 = generatePairComb(List(('a', 2), ('b', 2), ('c',3)));System.out.println("""t2  : List[List[(Char, Int)]] = """ + $show(t2 ));$skip(23); 
	
	val t3 = t2.flatten;System.out.println("""t3  : List[(Char, Int)] = """ + $show(t3 ));$skip(267); 
	
	
	/*def generateLists(l1: List[(Char, Int)], l2: List[List[(Char, Int)]]): List[List[(Char, Int)]] = {
		for {
			s1 <- generateSlices(l1).toList
		} yield s1 ++ l2
	}*/
	def generateLists(list: List[List[(Char, Int)]]): List[List[(Char, Int)]] = {
		
		List()
	};System.out.println("""generateLists: (list: List[List[(Char, Int)]])List[List[(Char, Int)]]""");$skip(189); val res$2 = 
  //generateLists(List(('a',1), ('a',2)), List(('c',1), ('c',2), ('c',3)))
  
  //t2.fold(List[List[(Char, Int)]]())(generateLists)
    
    generateSlices(List(('c',1), ('c',2), ('c',3)));System.out.println("""res2: Seq[List[(Char, Int)]] = """ + $show(res$2))}
	
	//List(('a', 2), ('b', 2), ('c',3)).combinations(0).toList
	
  //generateLists(List(('a', 2), ('b', 2)))
  
	//combinationsHelper(List(('a', 2), ('b', 2), ('c',3)))
}
