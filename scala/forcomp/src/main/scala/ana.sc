object ana {
	
	import forcomp.Anagrams
  println("Welcome to the Scala worksheet")       //> Welcome to the Scala worksheet
  val s:  String = "Test"                         //> s  : String = Test
  s.map(c => c.toLower).groupBy(c => c).mapValues( s => s.length).toList
                                                  //> res0: List[(Char, Int)] = List((e,1), (t,2), (s,1))
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
                                                  //> wordOccurrences: (w: ana.Word)ana.Occurrences
  val sentence = List("abcd", "ae")               //> sentence  : List[String] = List(abcd, ae)
  sentence.apply(0)                               //> res1: String = abcd
  
  def sentenceToString(s: Sentence): String = s match {
  	case Nil =>  ""
  	case y::ys => y+sentenceToString(ys)
  }                                               //> sentenceToString: (s: ana.Sentence)String
  def sentenceOccurrences(s: Sentence): Occurrences = s match {
  	case Nil => List()
  	case y::ys => wordOccurrences(y) ++ sentenceOccurrences(ys)
  }                                               //> sentenceOccurrences: (s: ana.Sentence)ana.Occurrences
  //sentenceOccurrences(sentence)
  //lazy val dictionaryByOccurrences: Map[Occurrences, List[Word]] = {
  	
  //}
  def reduceOccurences(value: List[(Occurrences, Word)]): List[Word] = value match {
  	case Nil => List()
  	case y::ys => y._2 :: reduceOccurences(ys)
  	
  }                                               //> reduceOccurences: (value: List[(ana.Occurrences, ana.Word)])List[ana.Word]
  forcomp.Anagrams.dictionary.map((w: Word) => (wordOccurrences(w), w)).groupBy((elem: (Occurrences, Word)) => elem._1).mapValues(reduceOccurences)
                                                  //> res2: scala.collection.immutable.Map[ana.Occurrences,List[ana.Word]] = Map(
                                                  //| List((e,1), (i,1), (l,1), (r,1), (t,2)) -> List(litter), List((a,1), (d,1),
                                                  //|  (e,1), (g,2), (l,1), (r,1)) -> List(gargled), List((a,1), (e,1), (h,1), (i
                                                  //| ,1), (k,1), (n,1), (s,3)) -> List(shakiness), List((e,2), (g,1), (n,1)) -> 
                                                  //| List(gene), List((a,2), (n,1), (t,1), (y,1)) -> List(Tanya), List((a,1), (d
                                                  //| ,1), (e,2), (h,1), (m,1), (n,2), (o,1), (s,3)) -> List(handsomeness), List(
                                                  //| (a,2), (c,1), (e,2), (k,1), (l,1), (m,1), (p,1), (r,1), (t,1)) -> List(mark
                                                  //| etplace), List((a,1), (i,1), (l,2), (s,1), (v,1)) -> List(villas), List((d,
                                                  //| 2), (e,1), (h,2), (n,1), (r,1), (t,1), (u,1)) -> List(hundredth), List((a,3
                                                  //| ), (b,1), (c,1), (h,1), (i,2), (l,1), (o,1), (p,2), (r,1), (t,1), (y,1)) ->
                                                  //|  List(approachability), List((d,1), (e,2), (l,1), (s,1), (t,2)) -> List(set
                                                  //| tled), List((a,1), (g,1), (i,3), (l,1), (n,2), (t,1), (z,1)) -> List(Latini
                                                  //| zing), List((a,1), (m,1
                                                  //| Output exceeds cutoff limit.
}