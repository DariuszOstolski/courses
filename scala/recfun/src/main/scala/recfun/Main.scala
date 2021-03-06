package recfun
import common._

object Main {
  def main(args: Array[String]) {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
  }

  /**
   * Exercise 1
   */
  def pascal(c: Int, r: Int): Int = {
		  if (c==0 || c==r) 
			 1 
		  else 
		    pascal(c-1, r-1)+pascal(c,r-1)  
  }

  /**
   * Exercise 2
   */
  def balance(chars: List[Char]): Boolean = {
    
    def count(parentCount: Int, chars: List[Char]): Boolean = if (chars.isEmpty) parentCount == 0
    else if (chars.head == '(') count(1 + parentCount, chars.tail)
    else if (chars.head == ')')
      if (parentCount > 0) count(parentCount-1, chars.tail)
      else
        false
    else count(parentCount, chars.tail)

    //def stop(parentCount: Int,  chars: List[Char]): Boolean = if(chars.isEmpty) parentCount==0 else count(parentCount, )

    count(0, chars)
  }

  /**
   * Exercise 3
   */
  def countChange(money: Int, coins: List[Int]): Int = {
    if(money==0)
    	1
    else if (money<0 || coins.isEmpty)
    	0
    else
      countChange(money-coins.head, coins)+countChange(money, coins.tail)
    	  
  }
}
