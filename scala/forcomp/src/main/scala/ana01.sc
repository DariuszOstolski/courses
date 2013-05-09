object ana01 {
  import forcomp.Anagrams
//  Set(List[(Char, Int)]())
  val sentence = List("Yes", "man")               //> sentence  : List[String] = List(Yes, man)
  Anagrams.sentenceAnagrams(sentence)             //> res0: List[forcomp.Anagrams.Sentence] = List(List(as, en, my), List(as, my, 
                                                  //| en), List(en, as, my), List(en, my, as), List(my, as, en), List(my, en, as),
                                                  //|  List(my, sane, Sean), List(man, yes), List(men, say), List(yes, man), List(
                                                  //| say, men), List(sane, Sean, my))
 
    /* def generate(p: (Char, Int)): Seq[(Char, Int)] = {
      {
        for {
          integer <- 1 to p._2
        } yield (p._1, integer)
      }
    }

    def combineList(list: List[(Char, Int)]): Set[List[(Char, Int)]] = {
      if (list.isEmpty)
        Set(List[(Char, Int)]())
      else {
        {
          for {
            new_list <- generate(list.head)
            rest <- combineList(list.tail)
          } yield new_list :: rest
        }.toSet+List[(Char, Int)]()
      }
    }
 
 combineList(List(('a',2)))
  
  val oc = Anagrams.combinations(List(('a',2), ('b',2)))*/
  
  /*val occur = Anagrams.sentenceOccurrences(sentence)
  
	Anagrams.sentenceAnagrams(sentence)
	
	
	

  
  	
   
	
  //Anagrams.dictionaryByOccurrences.get(occur)

  
  
	for {
    c <- oc
    words <- Anagrams.dictionaryByOccurrences.get(c)
    //word <- Anagrams.wordAnagrams(words)
  } yield words
	/*val t1 = {
  for {
    c <- oc
    words <- Anagrams.dictionaryByOccurrences.get(c)
    //word <- Anagrams.wordAnagrams(words)
  } yield words
            }.toList
            
 for {
 	 words <- t1
 	 word <- words
 	} yield Anagrams.wordAnagrams(word)

  Anagrams.sentenceAnagrams(sentence)
  */
 */
 
}