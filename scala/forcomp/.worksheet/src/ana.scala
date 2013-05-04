object ana {
	
	import forcomp.Anagrams;import org.scalaide.worksheet.runtime.library.WorksheetSupport._; def main(args: Array[String])=$execute{;$skip(83); 
  println("Welcome to the Scala worksheet");$skip(26); 
  val s:  String = "Test";System.out.println("""s  : String = """ + $show(s ));$skip(73); val res$0 = 
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
  type Occurrences = List[(Char, Int)];System.out.println("""res0: List[(Char, Int)] = """ + $show(res$0));$skip(768); 
  
  def wordOccurrences(w: Word): Occurrences = {  w.map(c => c.toLower).groupBy(c => c).mapValues( s => s.length).toList.sortBy(( elem: (Char, Int) )  => elem._1) };System.out.println("""wordOccurrences: (w: ana.Word)ana.Occurrences""");$skip(36); 
  val sentence = List("abcd", "ae");System.out.println("""sentence  : List[String] = """ + $show(sentence ));$skip(20); val res$1 = 
  sentence.apply(0);System.out.println("""res1: String = """ + $show(res$1));$skip(122); 
  
  def sentenceToString(s: Sentence): String = s match {
  	case Nil =>  ""
  	case y::ys => y+sentenceToString(ys)
  };System.out.println("""sentenceToString: (s: ana.Sentence)String""");$skip(153); 
  def sentenceOccurrences(s: Sentence): Occurrences = s match {
  	case Nil => List()
  	case y::ys => wordOccurrences(y) ++ sentenceOccurrences(ys)
  };System.out.println("""sentenceOccurrences: (s: ana.Sentence)ana.Occurrences""");$skip(276); 
  //sentenceOccurrences(sentence)
  //lazy val dictionaryByOccurrences: Map[Occurrences, List[Word]] = {
  	
  //}
  def reduceOccurences(value: List[(Occurrences, Word)]): List[Word] = value match {
  	case Nil => List()
  	case y::ys => y._2 :: reduceOccurences(ys)
  	
  };System.out.println("""reduceOccurences: (value: List[(ana.Occurrences, ana.Word)])List[ana.Word]""");$skip(148); val res$2 = 
  forcomp.Anagrams.dictionary.map((w: Word) => (wordOccurrences(w), w)).groupBy((elem: (Occurrences, Word)) => elem._1).mapValues(reduceOccurences);System.out.println("""res2: scala.collection.immutable.Map[ana.Occurrences,List[ana.Word]] = """ + $show(res$2))}
}
